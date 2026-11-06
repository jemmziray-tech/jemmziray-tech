"""Preview metadata by default; --apply uses the user's authenticated GitHub CLI."""
import argparse
import json
from pathlib import Path
import subprocess

OWNER = 'jemmziray-tech'

def gh(*args, payload=None):
    command = ['gh', 'api', *args]
    if payload is not None: command += ['--input', '-']
    result = subprocess.run(command, input=None if payload is None else json.dumps(payload),
                            text=True, capture_output=True, check=True)
    return json.loads(result.stdout) if result.stdout else {}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    plan = json.loads((Path(__file__).parent/'public-repository-metadata.json').read_text())
    if not args.apply:
        print(json.dumps(plan, indent=2))
        print('Preview only. No network requests or changes. Use --apply with an authenticated gh CLI.')
        return
    if gh('user')['login'].lower() != OWNER:
        raise SystemExit('Sign in as jemmziray-tech before applying this plan.')
    for name, item in plan.items():
        endpoint = f'repos/{OWNER}/{name}'
        current = gh(endpoint)
        if current.get('private'):
            print(f'Skipped {name}: visibility changed; review privately.')
            continue
        # Preserve existing descriptions, especially upstream fork attribution.
        if not current.get('description'):
            gh(endpoint, '--method', 'PATCH', payload={'description': item['description']})
        topics = sorted(set(current.get('topics', [])) | set(item['topics']))
        if len(topics) > 20:
            print(f'Skipped topics for {name}: merged list exceeds 20; review manually.')
            continue
        gh(endpoint+'/topics', '--method', 'PUT', payload={'names': topics})
        updated = gh(endpoint)
        if not set(item['topics']).issubset(updated.get('topics', [])):
            raise RuntimeError(f'Topic verification failed for {name}')
        print(f'Updated and verified {name}')

if __name__ == '__main__':
    main()
