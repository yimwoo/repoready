#!/usr/bin/env python3
from pathlib import Path
import argparse
import json


def check_readme(repo_path: Path):
    readme = repo_path / 'README.md'
    checks = {
        'exists': readme.exists(),
        'has_title': False,
        'has_overview': False,
        'has_quick_start': False,
        'has_demo': False,
        'has_roadmap': False,
    }
    if readme.exists():
        text = readme.read_text(errors='ignore')
        checks['has_title'] = text.lstrip().startswith('# ')
        lower = text.lower()
        checks['has_overview'] = '## overview' in lower
        checks['has_quick_start'] = '## quick start' in lower
        checks['has_demo'] = '## demo' in lower
        checks['has_roadmap'] = '## roadmap' in lower
    return checks


def score(checks):
    total = sum(1 for v in checks.values() if v)
    return total, len(checks)


def markdown_report(repo_name, checks):
    total, max_score = score(checks)
    lines = [
        f'# RepoReady Report: {repo_name}',
        '',
        f'Score: **{total}/{max_score}**',
        '',
        '## Checks',
    ]
    for key, value in checks.items():
        label = key.replace('_', ' ').title()
        icon = '✅' if value else '❌'
        lines.append(f'- {icon} {label}')
    lines += [
        '',
        '## Suggestions',
        '- Add a crisp README title and one-sentence hook if missing.',
        '- Add Overview, Quick Start, Demo, and Roadmap sections.',
        '- Make the repo understandable in under 10 seconds.',
    ]
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description='Audit a repo for star-readiness basics.')
    parser.add_argument('repo_path', nargs='?', default='.')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--output', help='Write markdown report to file')
    args = parser.parse_args()

    repo_path = Path(args.repo_path).resolve()
    repo_name = repo_path.name
    checks = check_readme(repo_path)

    if args.json:
        print(json.dumps({'repo': repo_name, 'checks': checks, 'score': score(checks)}, indent=2))
        return

    report = markdown_report(repo_name, checks)
    if args.output:
        Path(args.output).write_text(report)
    print(report)


if __name__ == '__main__':
    main()
