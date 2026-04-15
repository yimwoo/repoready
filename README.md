# RepoReady

Turn a rough codebase into a star-ready GitHub repo.

RepoReady is a lightweight CLI that audits the basics of repo packaging so you can quickly spot weak README structure and improve first impressions before launch.

## Why this exists
Many repos are better than their GitHub presentation. RepoReady helps you catch the obvious gaps that reduce clarity, credibility, and star potential.

## What it checks today
- README exists
- title is present
- Overview section exists
- Quick Start section exists
- Demo section exists
- Roadmap section exists

## Quick Start
```bash
python3 repoready.py .
```

Audit another local repo:
```bash
python3 repoready.py /path/to/repo
```

Generate a markdown report:
```bash
python3 repoready.py . --output REPREADY-REPORT.md
```

JSON output:
```bash
python3 repoready.py . --json
```

## Example Output
```text
# RepoReady Report: my-repo

Score: 4/6

## Checks
- ✅ Exists
- ✅ Has Title
- ✅ Has Overview
- ❌ Has Quick Start
- ❌ Has Demo
- ✅ Has Roadmap
```

## Demo
Current demo is CLI-based. Next step is to add richer scoring, more checks, and better actionable recommendations.

## Roadmap
- [x] Basic README structure audit
- [ ] Better packaging heuristics
- [ ] README hook quality checks
- [ ] Launch-readiness checklist output
- [ ] Example repo comparisons

## Positioning
RepoReady is optimized for fast packaging feedback, especially for indie hackers and open-source maintainers who want their repos to look more star-worthy.
