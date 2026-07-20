"""MCP resources exposed by the server."""

from typing import List

from mcp.types import Resource
from pydantic import AnyUrl

MARKET_INFO_URI = "bybit://market/info"

_MARKET_INFO = """
# ByBit MCP Desk

Access to Bybit's v5 API through the Model Context Protocol.

## Categories
- linear: USDT/USDC perpetuals and futures
- inverse: coin-margined perpetuals and futures
- option: options
- spot: spot trading

## Tool groups
- Market data: server time, tickers, order book, trades, klines, instruments,
  funding, open interest, insurance, risk limits, long/short ratio.
- Account (read-only): orders, order/trade history, balances, account info,
  positions, closed PnL, spot borrow quota.
- Trading (only when BYBIT_TRADING_ENABLED=true): place/amend/cancel orders,
  batch operations, trigger orders, leverage, margin mode, position mode,
  trading stops, auto-add-margin, margin changes.

Each tool's parameters are described in its input schema. Required parameters
are marked there; most support optional filtering by symbol, category, time
range and pagination.
"""


def list_resources() -> List[Resource]:
    return [
        Resource(
            uri=AnyUrl(MARKET_INFO_URI),
            name="ByBit MCP Desk Information",
            description="Overview of available Bybit endpoints and capabilities",
            mimeType="text/plain",
        )
    ]


def read_resource(uri: AnyUrl) -> str:
    if str(uri) == MARKET_INFO_URI:
        return _MARKET_INFO.strip()
    raise ValueError(f"Unknown resource: {uri}")
