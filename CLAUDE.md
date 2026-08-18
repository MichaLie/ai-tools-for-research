# CLAUDE.md

The complete maintenance protocol for this repo lives in **[AGENTS.md](AGENTS.md)**.
Read it before changing anything — it is binding, and it is short.

The two commands that matter:

```bash
python3 scripts/validate.py
python3 scripts/build.py
```

Never hand-edit `README.md`, `docs/`, or `exports/` — they are generated.
Source of truth is `tools/*.yml` + `categories.yml`.
