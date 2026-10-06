"""Check segmentation schema, provenance links, draft state and artifact anchors."""
import csv
import re
from pathlib import Path
from datetime import date

ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'30_disease_market'
def read(name):
    with (DATA/name).open(newline='') as f:
        records=list(csv.reader(f))
    header,*values=records
    assert len(header)==len(set(header)),f'{name}: duplicate fields'
    assert values,f'{name}: no records'
    assert all(len(r)==len(header) for r in values),f'{name}: malformed CSV'
    rows=[dict(zip(header,r)) for r in values]
    ids=[r[header[0]] for r in rows]
    assert all(ids) and len(set(ids))==len(ids),f'{name}: missing/duplicate IDs'
    return header,rows

ledger_header,claims=read('evidence_ledger_jha_146.csv')
canonical=next(csv.reader((ROOT/'10_framework/evidence_ledger_template.csv').open()))
assert ledger_header==canonical,'Canonical ledger schema changed'
map_header,mappings=read('evidence_ledger_artifact_mapping_jha_146.csv')
assert map_header==next(csv.reader((ROOT/'10_framework/evidence_ledger_artifact_mapping_template.csv').open()))
by_id={r['claim_id']:r for r in claims}
required=['claim_id','claim_text','claim_type','evidence_status','evidence_directness','disease_relevance','source_id','source_type','source_title','source_publisher','source_url','publication_date','publication_date_precision','access_date','evidence_location','confidence','verification_state','reverification_trigger','geography','population','denominator','intervention','comparator','outcome','timepoint']
for r in claims:
    assert all(r[k] for k in required),r['claim_id']
    assert r['claim_type'] in {'fact','analyst_inference','company_interpretation'}
    assert r['evidence_status'] in {'positive','negative','mixed','not_found','not_reported','not_studied','not_evaluable','not_applicable'}
    assert r['verification_state'] in {'draft','source_checked'},'No independent approval completed'
    assert r['source_url'].startswith('https://')
    assert r['confidence'] in {'low','moderate'},'Current evidence limitations preclude high'
    if r['parent_claim_id']:assert r['parent_claim_id'] in by_id
    if r['claim_type']=='analyst_inference' or r['evidence_directness']=='indirect':
        assert r['analyst_interpretation']
        for c in re.findall(r'JHA-146-CLM-\d{4}',r['analyst_interpretation']):assert c in by_id
    if r['claim_type']=='fact':assert r['quoted_evidence']
    if r['verification_state']=='source_checked':assert r['verified_by'] and r['verified_date']
    precision=r['publication_date_precision']; value=r['publication_date']
    assert re.fullmatch({'year':r'\d{4}','month':r'\d{4}-\d{2}','day':r'\d{4}-\d{2}-\d{2}','not_reported':'not_reported'}[precision],value)
    if precision!='not_reported':
        assert date.fromisoformat(value+{'year':'-01-01','month':'-01','day':''}[precision])<=date(2026,10,4)

anchor_sets={}
usage=set()
for name,key in [('patient_segments_jha_146.csv','segment_id'),('segmentation_variables_jha_146.csv','variable_id'),('biomarker_hypotheses_jha_146.csv','hypothesis_id')]:
    _,rows=read(name);anchor_sets[name]={r[key] for r in rows}
    for r in rows:
        assert all(r.values()),(name,r[key])
        for c in r['claim_ids'].split(';'):
            assert c in by_id,(name,c)
            usage.add((name,r[key],c))
        if name=='patient_segments_jha_146.csv':assert r['commercial_missingness']=='not_evaluable'
        if name=='biomarker_hypotheses_jha_146.csv':assert r['evidence_status']=='not_evaluable'

def heading_anchor(h):
    return re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-')
for name in ['patient_segmentation_framework.md','segmentation_verification_jha_146.md']:
    text=(DATA/name).read_text()
    anchor_sets[name]={heading_anchor(h) for h in re.findall(r'^#{1,6} (.+)$',text,re.M)}
    assert '2026-10-04' in text and '2026-10-06' in text
mapped=set()
for r in mappings:
    assert r['claim_id'] in by_id
    assert r['artifact_anchor'] in anchor_sets[r['artifact_id']],r
    mapped.add((r['artifact_id'],r['artifact_anchor'],r['claim_id']))
assert usage<=mapped,'Missing claim use mapping'
assert {r['claim_id'] for r in mappings}==set(by_id),'Unmapped evidence row'
_,gaps=read('segmentation_gaps_jha_146.csv')
for r in gaps:
    assert r['evidence_state']=='not_evaluable'
    assert r['owner_issue'] in {'JHA-146','JHA-147','JHA-148','JHA-166'}
    assert r['closure_action'] and r['release_effect']
print(f'PASS: {len(claims)} working claims; {len(mappings)} mappings; {len(gaps)} owned gaps; canonical schemas and cross-file links valid')
