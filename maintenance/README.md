# Repository metadata plan

The JSON file proposes descriptions and topics for the 38 public repositories reviewed in November 2026. Forks retain their current descriptions and attribution. Private repositories are deliberately absent from this public file.

The GitHub connection used for the review could edit files and pull requests but did not expose description/topic updates. These settings have **not** been applied by committing this plan.

With Python and GitHub CLI installed:

```sh
python maintenance/apply_metadata.py
# Review the preview, authenticate gh as jemmziray-tech, then:
python maintenance/apply_metadata.py --apply
```

The script previews without network access by default. Applying fills only empty descriptions, preserves existing topics, checks the authenticated account, skips repositories that became private, and reads back topics to verify them. It does not change repository visibility, remove forks or archive projects.
