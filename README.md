# ByBit MCP Desk

> ⚠️ **TRADING WARNING**
> This MCP server can execute **REAL trading operations** on Bybit when `BYBIT_TRADING_ENABLED=true`.
> Trading uses **real money** and can cause **financial loss**. Test on testnet first
> (`BYBIT_TESTNET=true`). **Trading is disabled by default.**

A personal [Model Context Protocol](https://modelcontextprotocol.io) server that exposes the
Bybit v5 API to MCP-capable AI clients — market data, order execution, positions, and account
information. Runs directly over stdio.

## Features

**Market data (always available, no trading flag needed)**
- Server time, tickers, order book, recent trades
- Klines: standard, mark price, index price, premium index
- Instruments info, funding rate history, open interest
- Risk limits, insurance fund, long/short ratio

**Account & read-only (needs API keys)**
- Wallet balance, single-coin balance, account info
- Open/closed orders, order history, trade history
- Position info, closed PnL, spot borrow quota

**Trading (needs `BYBIT_TRADING_ENABLED=true`)**
- Place / amend / cancel orders, cancel-all, batch place/amend/cancel
- Trigger (conditional) orders
- Set leverage, switch cross/isolated margin, switch position mode
- Trading stops (TP/SL), auto-add-margin, modify position margin

Trading tools are **not even listed** to the client unless trading is enabled, and each
trading function re-checks the flag server-side as a second guard.

## Requirements

- Python 3.13+ (developed on 3.14)
- Bybit API key/secret (only needed for account/trading tools; public market data works without)

## Setup

This repo is used directly from a virtual environment (no Docker).

```bash
cd ~/Projects/bybit-mcp-desk
python3 -m venv .venv
.venv/bin/python -m pip install -e .
```

> Prefer [uv](https://docs.astral.sh/uv/)? `uv sync` then `uv run bybit-mcp-desk` also works
> once uv is installed.

## Configuration

Copy `.env.example` to `.env` and fill in your credentials:

```bash
# Bybit API credentials
BYBIT_API_KEY=your-key
BYBIT_API_SECRET=your-secret

# Use the Bybit testnet (recommended while testing)
BYBIT_TESTNET=true

# Enable REAL trading operations (leave false unless you mean it)
BYBIT_TRADING_ENABLED=false
```

## Running

```bash
.venv/bin/bybit-mcp-desk
```

The server speaks MCP over stdio and waits for a client to connect.

### MCP client config

Point your MCP client at the venv's console script. Example (Claude Desktop /
`claude_desktop_config.json`, or any MCP client that takes a command):

```json
{
  "mcpServers": {
    "bybit-mcp-desk": {
      "command": "/var/home/mosman092/Projects/bybit-mcp-desk/.venv/bin/bybit-mcp-desk",
      "env": {
        "BYBIT_API_KEY": "your-key",
        "BYBIT_API_SECRET": "your-secret",
        "BYBIT_TESTNET": "true",
        "BYBIT_TRADING_ENABLED": "false"
      }
    }
  }
}
```

Environment variables set in the client config override the `.env` file.

## Development

```bash
.venv/bin/python -m pip install pytest ruff   # dev tools
.venv/bin/ruff check src/ tests/              # lint
.venv/bin/python -m pytest tests/             # tests
```

Note: `tests/test_market.py` hits the live Bybit public API, and the trade tests only run when
`BYBIT_TESTNET=true`. `tests/test_position_models.py` is a pure offline unit test.

## Safety

- Trading disabled by default; enable explicitly via `BYBIT_TRADING_ENABLED=true`.
- Always validate on testnet (`BYBIT_TESTNET=true`) before touching a live account.
- Keep your API keys out of version control — `.env` is gitignored.

## License

MIT
