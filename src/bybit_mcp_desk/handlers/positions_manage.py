"""Position management write handlers: leverage and margin/position modes."""

from typing import Any, Dict, Optional

from bybit_mcp_desk.handlers.base import TRADING_ENABLED, session, trading_disabled_response, unwrap
from bybit_mcp_desk.models.positions_manage import (
    SetLeverageResponse,
    SwitchMarginModeResponse,
    SwitchPositionModeResponse,
)


def set_leverage(category: str, symbol: str, buyLeverage: str, sellLeverage: str) -> SetLeverageResponse:
    if not TRADING_ENABLED:
        return trading_disabled_response(SetLeverageResponse)
    response = session.set_leverage(category=category, symbol=symbol, buyLeverage=buyLeverage, sellLeverage=sellLeverage)
    return SetLeverageResponse(**unwrap(response))


def switch_cross_isolated_margin(
    category: str,
    symbol: str,
    tradeMode: int,
    buyLeverage: str,
    sellLeverage: str,
) -> SwitchMarginModeResponse:
    if not TRADING_ENABLED:
        return trading_disabled_response(SwitchMarginModeResponse)
    response = session.switch_margin_mode(
        category=category,
        symbol=symbol,
        tradeMode=tradeMode,
        buyLeverage=buyLeverage,
        sellLeverage=sellLeverage,
    )
    return SwitchMarginModeResponse(**unwrap(response))


def switch_position_mode(
    category: str,
    symbol: Optional[str] = None,
    coin: Optional[str] = None,
    mode: int = 0,
) -> SwitchPositionModeResponse:
    if not TRADING_ENABLED:
        return trading_disabled_response(SwitchPositionModeResponse)
    params: Dict[str, Any] = {"category": category, "mode": mode}
    if symbol:
        params["symbol"] = symbol
    if coin:
        params["coin"] = coin
    return SwitchPositionModeResponse(**unwrap(session.switch_position_mode(**params)))
