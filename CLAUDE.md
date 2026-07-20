# CLAUDE.md

Guidance for working in this repository.

## Project

**ByBit MCP Desk** — a personal [Model Context Protocol](https://modelcontextprotocol.io)
server exposing the Bybit v5 API (market data, orders, positions, account) over stdio.
Python package: `bybit_mcp_desk`.

## Git rules

- **Never attribute commits, PRs, or any repo content to an AI tool.** No
  `Co-Authored-By` for AI assistants, no "Generated with …" trailers, no AI mentions
  in commit messages, comments, or docs. Commits are authored solely by the human owner.
- Keep commit messages short and imperative ("add borrow-quota tool", "split trade handlers").
- Do not commit secrets. `.env` is gitignored; only `.env.example` is tracked.

## Architecture

Declarative schemas + registry dispatch — no monolith, no giant `if/elif`.

```
src/bybit_mcp_desk/
  config.py              env + shared Bybit HTTP session + feature flags
  main.py                async entrypoint (stdio run) + cli_main
  __main__.py            `python -m bybit_mcp_desk`
  server.py              MCP Server instance + handler registration
  registry.py            tool-name -> handler map (dispatch); result formatting
  resources.py           MCP resource(s)
  tools/
    loader.py            load Tool objects from JSON schema files
    schemas/*.json       declarative tool definitions (name, description, inputSchema)
  handlers/              Bybit API call functions, grouped by domain (market, orders, ...)
  models/                Pydantic response models, grouped by domain
```

- **Tool schemas are data**, not code: they live in `tools/schemas/*.json`. Files under
  `schemas/trading/` are only listed when trading is enabled.
- **Handlers** call pybit and return validated Pydantic models. Every write handler
  re-checks `TRADING_ENABLED` as a second guard.
- **Dispatch** is a dict lookup in `registry.py`. Add a tool = add its JSON schema + a
  handler + one registry entry. Never grow an `if/elif` chain.

## Coding rules

- **File size: aim for ≤150 lines per module; hard cap ~200.** Split by responsibility
  (not arbitrarily) when a file grows past this. JSON schema files are data, not subject
  to this cap.
- One clear responsibility per module; group related functions, keep public surface small.
- Full type hints on all function signatures. Prefer explicit over clever.
- All external API responses are parsed into Pydantic models in `models/`.
- Read config (env vars, session) only through `config.py` — no scattered `os.getenv`.
- Match existing style; let `ruff` format. Line length is 180 (see `pyproject.toml`).

## Dev workflow

This toolbox has no `uv`/system `pip`; use a venv:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -e .
.venv/bin/python -m pip install pytest ruff   # dev tools

.venv/bin/ruff check src/ tests/              # lint
.venv/bin/python -m pytest tests/             # tests
.venv/bin/bybit-mcp-desk                      # run the server (stdio)
```

- `tests/test_market.py` hits the live Bybit public API.
- Trade tests run only with `BYBIT_TESTNET=true`.
- `tests/test_position_models.py` is a pure offline unit test.

## Safety

Trading is disabled by default. Enable only via `BYBIT_TRADING_ENABLED=true`, and validate
on testnet (`BYBIT_TESTNET=true`) before touching a live account.
