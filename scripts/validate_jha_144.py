"""Validate the preliminary asset package and its PR #5 review corrections."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / '20_competitive'

def read(name):
    with (DATA / name).open(newline='') as stream:
        records = list(csv.reader(stream))
    header, *values = records
    assert len(header) == len(set(header)), f'{name}: duplicate columns'
    for line, row in enumerate(values, 2):
        assert len(row) == len(header), f'{name}:{line}: expected {len(header)} fields, got {len(row)}'
    rows = [dict(zip(header, row)) for row in values]
    ids = [row[header[0]] for row in rows]
    assert all(ids) and len(ids) == len(set(ids)), f'{name}: missing or duplicate ID'
    return rows

assets = read('preliminary_asset_universe.csv')
claims = read('evidence_ledger_jha_144.csv')
mapping = read('evidence_ledger_artifact_mapping_jha_144.csv')
gaps = read('initial_evidence_gaps.csv')
events = read('program_status_log.csv')
asset_by_id = {r['asset_id']: r for r in assets}
claim_by_id = {r['claim_id']: r for r in claims}
gap_by_id = {r['gap_id']: r for r in gaps}
assert len(assets) == 37 and len(events) == 55
method = (DATA / 'asset_universe_method.md').read_text()
statuses = set(re.findall(r'`([a-z_]+)`', method.split('## Program-status protocol')[1].split('## Interpretation guardrails')[0]))
evidence_states = {'positive', 'negative', 'mixed', 'not_found', 'not_reported', 'not_studied', 'not_evaluable', 'not_applicable'}
for row in assets:
    assert row['program_status'] in statuses, row['asset_id']
    assert row['status_as_of'] == '2026-10-04'
    assert row['inclusion_rationale'] and row['primary_status_source']
    if row['program_status'] == 'adjacent_active':
        assert row['registry_source'] not in {'not_found', 'not_reported', 'not_applicable'}
        assert row['trial_ids'] not in {'not_found', 'not_reported', 'not_applicable'}
for row in claims:
    required = ['claim_id', 'claim_text', 'claim_type', 'evidence_status', 'evidence_directness', 'disease_relevance', 'source_id', 'source_type', 'source_title', 'source_publisher', 'source_url', 'publication_date', 'publication_date_precision', 'access_date', 'evidence_location', 'confidence', 'verification_state', 'reverification_trigger', 'geography', 'population', 'denominator', 'intervention', 'comparator', 'outcome', 'timepoint']
    assert all(row[k] for k in required), row['claim_id']
    assert row['evidence_status'] in evidence_states
    assert row['claim_type'] in {'fact', 'company_interpretation', 'analyst_inference'}
    assert row['evidence_directness'] in {'direct', 'indirect'}
    assert row['source_url'].startswith('https://')
    assert row['verified_by'] and row['verified_date']
    if row['parent_claim_id']:
        assert row['parent_claim_id'] in claim_by_id
    if row['evidence_directness'] == 'indirect':
        assert row['analyst_interpretation']
    precision = row['publication_date_precision']
    date_pattern = {'year': r'\d{4}', 'month': r'\d{4}-\d{2}', 'day': r'\d{4}-\d{2}-\d{2}', 'not_reported': 'not_reported'}
    assert re.fullmatch(date_pattern[precision], row['publication_date']), row['claim_id']
    if precision != 'not_reported':
        assert row['publication_date'] <= '2026-10-04'
covered = set()
for row in mapping:
    assert row['claim_id'] in claim_by_id
    if row['mapping_status'] == 'active':
        assert claim_by_id[row['claim_id']]['verification_state'] != 'superseded'
        if row['artifact_id'] == 'JHA-144-ASSET-UNIVERSE':
            assert row['artifact_anchor'] in asset_by_id
            covered.add(row['artifact_anchor'])
assert covered == set(asset_by_id)
for row in events:
    assert row['asset_id'] in asset_by_id
    assert row['event_date'] <= '2026-10-04'
for row in gaps:
    assert row['evidence_state'] in evidence_states
    assert row['asset_id_or_modality'] and row['owner_issue']
    assert row['priority'] in {'high', 'medium', 'low'}

# Regressions exercise the affected fields as downstream CSV readers consume them.
for n, kind, state, owner, priority in [
    (16, 'broader_non_reset_competitors', 'not_found', 'JHA-161', 'high'),
    (17, 'global_trial_registry_coverage', 'not_evaluable', 'JHA-172', 'medium'),
    (18, 'post_cutoff_changes', 'not_applicable', 'JHA-163', 'high'),
]:
    row = gap_by_id[f'JHA-144-GAP-{n:03d}']
    assert [row[k] for k in ['asset_id_or_modality', 'gap_type', 'evidence_state', 'owner_issue', 'priority']] == ['universe_wide', kind, state, owner, priority]
for key in {'A010', 'A015'}:
    assert asset_by_id[key]['program_status'] == 'planned_not_started'
assert asset_by_id['A019']['program_status'] == 'unknown_stale_registry'
for key in {'A026', 'A027', 'A033', 'A034', 'A036', 'A037'}:
    assert asset_by_id[key]['program_status'] == 'adjacent_activity_unconfirmed'
assert asset_by_id['A035']['program_status'] == 'adjacent_completed_status_unclear'
for n in (23, 24, 25):
    assert claim_by_id[f'JHA-144-CLM-{n:04d}']['evidence_status'] == 'positive'
assert claim_by_id['JHA-144-CLM-0037']['verification_state'] == 'superseded'
direct = claim_by_id['JHA-144-CLM-0039']
adjacent = claim_by_id['JHA-144-CLM-0040']
assert (direct['evidence_directness'], direct['disease_relevance']) == ('direct', 'sjogren_direct')
assert (adjacent['evidence_directness'], adjacent['disease_relevance']) == ('indirect', 'adjacent_autoimmune')
assert direct['source_url'] != adjacent['source_url']
for row in (direct, adjacent):
    assert any(m['claim_id'] == row['claim_id'] and m['artifact_anchor'] == 'A037' and m['mapping_status'] == 'active' for m in mapping)
print(f'PASS: {len(assets)} assets, {len(events)} events, {len(claims)} claims, {len(mapping)} mappings, {len(gaps)} gaps; all six review regressions passed.')
