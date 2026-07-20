"""Position risk handlers: trading stops (TP/SL), auto-add-margin, margin changes."""

from typing import Any, Dict, Optional

from bybit_mcp_desk.handlers.base import TRADING_ENABLED, session, trading_disabled_response, unwrap
from bybit_mcp_desk.models.positions_manage import (
    AddReduceMarginResponse,
    SetAutoAddMarginResponse,
    SetTradingStopResponse,
)


def set_trading_stop(
    category: str,
    symbol: str,
    positionIdx: Optional[int] = None,
    takeProfit: Optional[str] = None,
    stopLoss: Optional[str] = None,
    trailingStop: Optional[str] = None,
    tpTriggerBy: Optional[str] = None,
    slTriggerBy: Optional[str] = None,
    activePrice: Optional[str] = None,
    tpslMode: Optional[str] = None,
    tpLimitPrice: Optional[str] = None,
    slLimitPrice: Optional[str] = None,
    tpOrderType: Optional[str] = None,
    slOrderType: Optional[str] = None,
) -> SetTradingStopResponse:
    if not TRADING_ENABLED:
        return trading_disabled_response(SetTradingStopResponse)
    params: Dict[str, Any] = {"category": category, "symbol": symbol}
    optional = {
        "positionIdx": str(positionIdx) if positionIdx is not None else None,
        "takeProfit": takeProfit,
        "stopLoss": stopLoss,
        "trailingStop": trailingStop,
        "tpTriggerBy": tpTriggerBy,
        "slTriggerBy": slTriggerBy,
        "activePrice": activePrice,
        "tpslMode": tpslMode,
        "tpLimitPrice": tpLimitPrice,
        "slLimitPrice": slLimitPrice,
        "tpOrderType": tpOrderType,
        "slOrderType": slOrderType,
    }
    params.update({k: v for k, v in optional.items() if v is not None})
    return SetTradingStopResponse(**unwrap(session.set_trading_stop(**params)))


def set_auto_add_margin(category: str, symbol: str, autoAddMargin: int, positionIdx: Optional[int] = None) -> SetAutoAddMarginResponse:
    if not TRADING_ENABLED:
        return trading_disabled_response(SetAutoAddMarginResponse)
    params: Dict[str, Any] = {"category": category, "symbol": symbol, "autoAddMargin": autoAddMargin}
    if positionIdx is not None:
        params["positionIdx"] = str(positionIdx)
    return SetAutoAddMarginResponse(**unwrap(session.set_auto_add_margin(**params)))


def modify_position_margin(category: str, symbol: str, margin: str, positionIdx: Optional[int] = None) -> AddReduceMarginResponse:
    if not TRADING_ENABLED:
        return trading_disabled_response(AddReduceMarginResponse)
    params: Dict[str, Any] = {"category": category, "symbol": symbol, "margin": margin}
    if positionIdx is not None:
        params["positionIdx"] = str(positionIdx)
    return AddReduceMarginResponse(**unwrap(session.add_or_reduce_margin(**params)))
