"""Read-only market-data handlers (everything except klines)."""

from typing import Any, Dict, Union

from bybit_mcp_desk.handlers.base import session, unwrap
from bybit_mcp_desk.models.market import OrderBookResponse, RecentTradesResponse, TickerResponse
from bybit_mcp_desk.models.market_ref import (
    FundingRateHistoryResponse,
    InstrumentsInfoResponse,
    InsuranceResponse,
    LongShortRatioResponse,
    OpenInterestResponse,
    RiskLimitResponse,
)


def get_server_time() -> Dict[str, Any]:
    return session.get_server_time()


def get_tickers(
    symbol: Union[str, None] = None,
    category: str = "linear",
    baseCoin: Union[str, None] = None,
    limit: int | None = None,
    cursor: str | None = None,
) -> TickerResponse:
    params: Dict[str, Any] = {"category": category}
    for key, value in [("symbol", symbol), ("baseCoin", baseCoin), ("limit", str(limit) if limit else None), ("cursor", cursor)]:
        if value:
            params[key] = value
    return TickerResponse(**unwrap(session.get_tickers(**params))["result"])


def get_order_book(symbol: str, category: str = "linear", limit: int = 50, baseCoin: Union[str, None] = None) -> OrderBookResponse:
    params: Dict[str, Any] = {"symbol": symbol, "category": category, "limit": limit}
    if baseCoin:
        params["baseCoin"] = baseCoin
    return OrderBookResponse(**unwrap(session.get_orderbook(**params))["result"])


def get_recent_trades(
    symbol: str,
    category: str = "linear",
    baseCoin: Union[str, None] = None,
    optionType: Union[str, None] = None,
    limit: int = 50,
) -> RecentTradesResponse:
    params: Dict[str, Any] = {"symbol": symbol, "category": category, "limit": limit}
    if baseCoin:
        params["baseCoin"] = baseCoin
    if optionType:
        params["optionType"] = optionType
    return RecentTradesResponse(**unwrap(session.get_public_trade_history(**params))["result"])


def get_instruments_info(category: str = "linear", symbol: Union[str, None] = None) -> InstrumentsInfoResponse:
    params: Dict[str, Any] = {"category": category}
    if symbol:
        params["symbol"] = symbol
    return InstrumentsInfoResponse(**unwrap(session.get_instruments_info(**params))["result"])


def get_funding_rate_history(symbol: str, category: str = "linear", limit: int = 200) -> FundingRateHistoryResponse:
    response = session.get_funding_rate_history(symbol=symbol, category=category, limit=limit)
    return FundingRateHistoryResponse(**unwrap(response)["result"])


def get_open_interest(symbol: str, category: str = "linear", interval: str = "5min", limit: int = 200) -> OpenInterestResponse:
    response = session.get_open_interest(symbol=symbol, category=category, intervalTime=interval, limit=limit)
    return OpenInterestResponse(**unwrap(response)["result"])


def get_insurance(
    category: str = "linear",
    baseCoin: Union[str, None] = None,
    quoteCoin: Union[str, None] = None,
    startTime: Union[str, None] = None,
    endTime: Union[str, None] = None,
) -> InsuranceResponse:
    params: Dict[str, Any] = {"category": category}
    for key, value in [("baseCoin", baseCoin), ("quoteCoin", quoteCoin), ("startTime", startTime), ("endTime", endTime)]:
        if value:
            params[key] = value
    return InsuranceResponse(**unwrap(session.get_insurance(**params))["result"])


def get_risk_limit(symbol: str, category: str = "linear") -> RiskLimitResponse:
    return RiskLimitResponse(**unwrap(session.get_risk_limit(symbol=symbol, category=category))["result"])


def get_long_short_ratio(symbol: str, category: str = "linear", interval: str = "5min", limit: int = 200) -> LongShortRatioResponse:
    response = session.get_long_short_ratio(symbol=symbol, category=category, period=interval, limit=limit)
    return LongShortRatioResponse(**unwrap(response)["result"])
