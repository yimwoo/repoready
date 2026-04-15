# RepoReady Scoring

RepoReady uses a lightweight launch-readiness score to estimate how strong a repository's first impression may be.

## What the score is for
- catching obvious packaging gaps
- helping maintainers prioritize README and repo improvements
- making launch quality more visible

## What the score is not
- a guarantee of stars
- a substitute for product usefulness
- a replacement for distribution

## Readiness Bands
- 85%+ = Strong launch readiness
- 65%+ = Promising but still rough
- 45%+ = Early draft quality
- below 45% = Weak launch readiness

## Current Signals
RepoReady currently looks at:
- README basics
- install and example signals
- trust signals like LICENSE and CONTRIBUTING
- packaging support files like pyproject/package.json
- visual/demo hints
- tests and docs/examples directories

The system should expand over time as we learn which repo qualities correlate with attention and stars.
