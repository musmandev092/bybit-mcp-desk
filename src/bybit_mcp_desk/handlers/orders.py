"""Single-order write handlers: place, amend, cancel and cancel-all."""

from typing import Any, Dict, Union

from bybit_mcp_desk.handlers.base import TRADING_ENABLED, session, trading_disabled_response, unwrap
from bybit_mcp_desk.models.orders import (
    AmendOrderResponse,
    CancelAllOrdersResponse,
    CancelOrderResponse,
    PlaceOrderResponse,
)


def place_order(
    category: str,
    symbol: str,
    side: str,
    orderType: str,
    qty: str,
    price: Union[str, None] = None,
    isLeverage: Union[int, None] = None,
    orderLinkId: Union[str, None] = None,
) -> PlaceOrderResponse:
    if not TRADING_ENABLED:
        return trading_disabled_response(PlaceOrderResponse)
    response = session.place_order(
        category=category,
        symbol=symbol,
        side=side,
        orderType=orderType,
        qty=qty,
        price=price,
        isLeverage=isLeverage,
        orderLinkId=orderLinkId,
    )
    return PlaceOrderResponse(**unwrap(response))


def amend_order(
    category: str,
    symbol: str,
    orderId: Union[str, None] = None,
    orderLinkId: Union[str, None] = None,
    orderIv: Union[str, None] = None,
    triggerPrice: Union[str, None] = None,
    qty: Union[str, None] = None,
    price: Union[str, None] = None,
    tpslMode: Union[str, None] = None,
    takeProfit: Union[str, None] = None,
    stopLoss: Union[str, None] = None,
    tpTriggerBy: Union[str, None] = None,
    slTriggerBy: Union[str, None] = None,
    triggerBy: Union[str, None] = None,
    tpLimitPrice: Union[str, None] = None,
    slLimitPrice: Union[str, None] = None,
) -> AmendOrderResponse:
    if not TRADING_ENABLED:
        return trading_disabled_response(AmendOrderResponse)
    params: Dict[str, Any] = {"category": category, "symbol": symbol}
    optional = {
        "orderId": orderId,
        "orderLinkId": orderLinkId,
        "orderIv": orderIv,
        "triggerPrice": triggerPrice,
        "qty": qty,
        "price": price,
        "tpslMode": tpslMode,
        "takeProfit": takeProfit,
        "stopLoss": stopLoss,
        "tpTriggerBy": tpTriggerBy,
        "slTriggerBy": slTriggerBy,
        "triggerBy": triggerBy,
        "tpLimitPrice": tpLimitPrice,
        "slLimitPrice": slLimitPrice,
    }
    params.update({k: v for k, v in optional.items() if v is not None})
    return AmendOrderResponse(**unwrap(session.amend_order(**params)))


def cancel_order(
    category: str,
    symbol: str,
    orderId: Union[str, None] = None,
    orderLinkId: Union[str, None] = None,
    orderFilter: Union[str, None] = None,
) -> CancelOrderResponse:
    if not TRADING_ENABLED:
        return trading_disabled_response(CancelOrderResponse)
    params: Dict[str, Any] = {"category": category, "symbol": symbol}
    for key, value in [("orderId", orderId), ("orderLinkId", orderLinkId), ("orderFilter", orderFilter)]:
        if value:
            params[key] = value
    return CancelOrderResponse(**unwrap(session.cancel_order(**params)))


def cancel_all_orders(
    category: str,
    symbol: Union[str, None] = None,
    baseCoin: Union[str, None] = None,
    settleCoin: Union[str, None] = None,
    orderFilter: Union[str, None] = None,
    stopOrderType: Union[str, None] = None,
) -> CancelAllOrdersResponse:
    if not TRADING_ENABLED:
        return trading_disabled_response(CancelAllOrdersResponse)
    params: Dict[str, Any] = {"category": category}
    optional = {"symbol": symbol, "baseCoin": baseCoin, "settleCoin": settleCoin, "orderFilter": orderFilter, "stopOrderType": stopOrderType}
    params.update({k: v for k, v in optional.items() if v is not None})
    return CancelAllOrdersResponse(**unwrap(session.cancel_all_orders(**params)))
