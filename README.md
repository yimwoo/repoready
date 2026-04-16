# RepoReady

Turn a rough codebase into a star-ready GitHub repo.

RepoReady is a lightweight CLI for maintainers, indie hackers, and open-source builders who want to improve repo packaging before launch. It audits the basics that shape first impressions and gives actionable suggestions to make a repository clearer, more credible, and more star-worthy.

## Overview
Many repos are more useful than they look. RepoReady helps identify missing structure in README and repo setup so visitors can understand the value faster.

## Who this is for
- open-source maintainers launching new repos
- indie hackers polishing public projects
- developers who want stronger README and repo presentation
- anyone who wants a lightweight repo-readiness checklist

## What it checks today
- README presence
- README title
- one-line hook under the title
- Overview section
- Quick Start section
- Demo section
- Roadmap section
- LICENSE file
- CONTRIBUTING.md
- .gitignore
- install/setup mentions
- example mentions

## Why this exists
A lot of repos fail to convert interest into stars because the packaging is weak, not because the underlying idea is bad. RepoReady helps catch the obvious gaps early.

## Installation
### Run directly
```bash
python3 repoready.py .
```

### Install as a local CLI
```bash
pip install -e .
repoready .
```

## Quick Start
Audit the current repo:
```bash
python3 repoready.py .
```

Audit another local repo:
```bash
python3 repoready.py /path/to/repo
```

Generate a markdown report:
```bash
python3 repoready.py . --output REPOREADY-REPORT.md
```

JSON output:
```bash
python3 repoready.py . --json
```

## Example Output
```text
# RepoReady Report: my-repo

Score: 8/12

## Checks
- ✅ Readme Exists
- ✅ Readme Has Title
- ❌ Readme Has One Line Hook
- ✅ Has Overview
- ✅ Has Quick Start
- ❌ Has Demo
```

## Demo
![RepoReady demo](assets/demo.svg)

RepoReady gives immediate packaging feedback in one command so you can tighten the README, examples, and proof before launch.

```bash
repoready /path/to/repo
```

You can also generate a shareable Markdown audit for a launch checklist or pull request:

```bash
repoready /path/to/repo --output REPOREADY-REPORT.md
```

## Before You Launch Checklist
- Can someone understand the repo in under 10 seconds?
- Is there a strong README hook?
- Are setup steps easy to copy and run?
- Is there at least one concrete example?
- Does the repo look maintained and intentional?

## Positioning
RepoReady is optimized for fast packaging feedback. It is intentionally lightweight and meant to help you tighten the basics before asking people to care.

## Roadmap
- [x] Basic repo-readiness audit
- [x] Actionable packaging suggestions
- [x] Launch-readiness scoring bands
- [x] Example reports for real repositories
- [ ] Better README hook quality checks
- [ ] Badge and social proof checks
- [ ] Repo category-specific scoring
- [ ] Example fix suggestions by missing section

## Visual Example
See [`assets/demo.svg`](assets/demo.svg) for a lightweight preview image that can be reused in social posts, docs, and launch threads.

## Visual Demo Ideas
- Terminal screenshot of a before/after repo audit
- Sample report excerpt for a weak repo vs a polished repo
- GIF showing RepoReady run and scoring output
