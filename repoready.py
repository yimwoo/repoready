#!/usr/bin/env python3
from pathlib import Path
import argparse
import json

README_SECTIONS = {
    'overview': '## overview',
    'quick_start': '## quick start',
    'demo': '## demo',
    'roadmap': '## roadmap',
}


def read_text(path: Path) -> str:
    return path.read_text(errors='ignore') if path.exists() else ''


def check_repo(repo_path: Path):
    readme = repo_path / 'README.md'
    license_file = repo_path / 'LICENSE'
    contributing = repo_path / 'CONTRIBUTING.md'
    gitignore = repo_path / '.gitignore'

    readme_text = read_text(readme)
    lower = readme_text.lower()

    checks = {
        'readme_exists': readme.exists(),
        'readme_has_title': readme_text.lstrip().startswith('# '),
        'readme_has_one_line_hook': bool(readme_text.splitlines()[2:3]) if readme.exists() else False,
        'has_overview': README_SECTIONS['overview'] in lower,
        'has_quick_start': README_SECTIONS['quick_start'] in lower,
        'has_demo': README_SECTIONS['demo'] in lower,
        'has_roadmap': README_SECTIONS['roadmap'] in lower,
        'has_license': license_file.exists(),
        'has_contributing': contributing.exists(),
        'has_gitignore': gitignore.exists(),
        'mentions_install': 'install' in lower,
        'mentions_examples': 'example' in lower,
    }
    return checks


def score(checks):
    total = sum(1 for v in checks.values() if v)
    return total, len(checks)


def suggestions(checks):
    tips = []
    if not checks['readme_exists']:
        tips.append('Add a README.md immediately.')
        return tips
    if not checks['readme_has_title']:
        tips.append('Add a strong README title.')
    if not checks['readme_has_one_line_hook']:
        tips.append('Add a one-line hook directly below the title.')
    if not checks['has_overview']:
        tips.append('Add an Overview section explaining what the repo does and who it is for.')
    if not checks['has_quick_start']:
        tips.append('Add a Quick Start section with copy-pasteable commands.')
    if not checks['has_demo']:
        tips.append('Add a Demo section with output, screenshot, or GIF.')
    if not checks['has_roadmap']:
        tips.append('Add a Roadmap section so visitors can see momentum.')
    if not checks['has_license']:
        tips.append('Add a LICENSE file to improve trust and reuse clarity.')
    if not checks['has_contributing']:
        tips.append('Add CONTRIBUTING.md to make collaboration easier.')
    if not checks['mentions_install']:
        tips.append('Mention install/setup instructions explicitly in the README.')
    if not checks['mentions_examples']:
        tips.append('Add an example section or example usage snippet.')
    return tips[:6]


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

    lines += ['', '## Suggestions']
    for tip in suggestions(checks):
        lines.append(f'- {tip}')

    lines += [
        '',
        '## Interpretation',
        '- A higher score suggests the repo is more likely to make a strong first impression.',
        '- This does not guarantee stars, but it helps catch common packaging weaknesses.',
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
    checks = check_repo(repo_path)

    if args.json:
        print(json.dumps({'repo': repo_name, 'checks': checks, 'score': score(checks), 'suggestions': suggestions(checks)}, indent=2))
        return

    report = markdown_report(repo_name, checks)
    if args.output:
        Path(args.output).write_text(report)
    print(report)


if __name__ == '__main__':
    main()
