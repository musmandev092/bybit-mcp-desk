"""Read-only position handlers: current positions and closed PnL."""

from typing import Any, Dict, Optional

from bybit_mcp_desk.handlers.base import session, unwrap
from bybit_mcp_desk.models.positions import GetClosedPnlResponse, GetPositionInfoResponse


def get_position_info(
    category: str,
    symbol: Optional[str] = None,
    baseCoin: Optional[str] = None,
    settleCoin: Optional[str] = None,
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
) -> GetPositionInfoResponse:
    params: Dict[str, Any] = {"category": category}
    if symbol:
        params["symbol"] = symbol
    if baseCoin:
        params["baseCoin"] = baseCoin
    if settleCoin:
        params["settleCoin"] = settleCoin
    if limit is not None:
        params["limit"] = str(limit)
    if cursor:
        params["cursor"] = cursor
    return GetPositionInfoResponse(**unwrap(session.get_positions(**params)))


def get_closed_pnl(
    category: str,
    symbol: Optional[str] = None,
    startTime: Optional[int] = None,
    endTime: Optional[int] = None,
    limit: Optional[int] = None,
    cursor: Optional[str] = None,
) -> GetClosedPnlResponse:
    params: Dict[str, Any] = {"category": category}
    for key, value in [("symbol", symbol), ("startTime", startTime), ("endTime", endTime), ("limit", limit), ("cursor", cursor)]:
        if value is not None:
            params[key] = str(value) if key in ("startTime", "endTime", "limit") else value
    return GetClosedPnlResponse(**unwrap(session.get_closed_pnl(**params)))
