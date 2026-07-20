"""Candlestick (kline) handlers: standard, mark, index and premium index prices."""

from bybit_mcp_desk.handlers.base import session, unwrap
from bybit_mcp_desk.models.market import KlineResponse


def get_kline(symbol: str, interval: str, category: str = "linear", limit: int = 200) -> KlineResponse:
    response = session.get_kline(symbol=symbol, interval=interval, category=category, limit=limit)
    return KlineResponse(**unwrap(response)["result"])


def get_mark_price_kline(symbol: str, interval: str, category: str = "linear", limit: int = 200) -> KlineResponse:
    response = session.get_mark_price_kline(symbol=symbol, interval=interval, category=category, limit=limit)
    return KlineResponse(**unwrap(response)["result"])


def get_index_price_kline(symbol: str, interval: str, category: str = "linear", limit: int = 200) -> KlineResponse:
    response = session.get_index_price_kline(symbol=symbol, interval=interval, category=category, limit=limit)
    return KlineResponse(**unwrap(response)["result"])


def get_premium_index_price_kline(symbol: str, interval: str, category: str = "linear", limit: int = 200) -> KlineResponse:
    response = session.get_premium_index_price_kline(symbol=symbol, interval=interval, category=category, limit=limit)
    return KlineResponse(**unwrap(response)["result"])
