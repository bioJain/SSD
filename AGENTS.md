# Repository instructions for Codex

## Source of truth

- Linear workspace: `JHa_Res`
- Linear project: `Sjögren B-cell Reset CI & Decision Map`
- Linear team key: `JHA`
- GitHub repository: `bioJain/SSD`
- Default branch: `main`

Before changing files, identify the Linear issue that authorizes the work. Use its
`JHA-###` identifier in the work branch, commit subject, and pull request. If no
issue exists for a material change, create or request one before implementation.

## Workflow

1. Read the full Linear issue, including acceptance criteria and linked material.
2. Work on an issue branch using Linear's suggested branch name when available.
3. Keep commits scoped and prefix each subject with the issue identifier.
4. Run checks appropriate to the files changed and report what was verified.
5. Open or update a pull request that links the Linear issue.
6. Add the resulting commit or pull-request URL to Linear and update its status.

The initial repository setup may be committed directly to `main`; subsequent
research or implementation changes should use pull requests.

## Evidence and data handling

- Use public information only unless a Linear issue explicitly authorizes another
  source and its handling requirements.
- Preserve claim-level citations and distinguish fact, interpretation, inference,
  extrapolation, and unknown.
- Separate Sjögren-direct evidence from adjacent-autoimmune evidence.
- Never commit credentials, private data, or large scientific binaries.
- Treat any future `00_source/` directory as immutable source material unless the
  authorizing Linear issue explicitly says otherwise.

## 세션 기록

세션을 마무리할 때(사용자가 "마무리", "정리", "여기까지"라고 할 때) 또는 산출물을 전달한 직후 세션 기록 한 행을 남긴다.

- Claude: 계정 skill `daily-log-append`를 따른다.
- 그 외 agent: 사용자가 따로 준 세션 기록 지침을 따른다. 지침이 없으면 한 일, 산출물 경로, 결정, 후속 작업을 탭으로 구분한 한 줄로 출력하고, 어디에 기록할지 사용자에게 묻는다.
- 금지: 자격증명, 개인 정보, 대화 원문의 긴 인용.
