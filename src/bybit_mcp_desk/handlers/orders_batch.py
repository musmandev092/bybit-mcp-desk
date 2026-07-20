"""Batch order handlers and conditional (trigger) order placement."""

from typing import Any, Dict, List, Union

from bybit_mcp_desk.handlers.base import TRADING_ENABLED, session, trading_disabled_response, unwrap
from bybit_mcp_desk.models.orders import (
    BatchAmendOrderResponse,
    BatchCancelOrderResponse,
    BatchPlaceOrderResponse,
    PlaceOrderResponse,
)


def batch_place_order(category: str, request: List[dict]) -> BatchPlaceOrderResponse:
    if not TRADING_ENABLED:
        return trading_disabled_response(BatchPlaceOrderResponse)
    return BatchPlaceOrderResponse(**unwrap(session.place_batch_order(category=category, request=request)))


def batch_amend_order(category: str, request: List[dict]) -> BatchAmendOrderResponse:
    if not TRADING_ENABLED:
        return trading_disabled_response(BatchAmendOrderResponse)
    return BatchAmendOrderResponse(**unwrap(session.amend_batch_order(category=category, request=request)))


def batch_cancel_order(category: str, request: List[dict]) -> BatchCancelOrderResponse:
    if not TRADING_ENABLED:
        return trading_disabled_response(BatchCancelOrderResponse)
    return BatchCancelOrderResponse(**unwrap(session.cancel_batch_order(category=category, request=request)))


def place_trigger_order(
    category: str,
    symbol: str,
    side: str,
    orderType: str,
    qty: str,
    triggerPrice: str,
    triggerDirection: int,
    triggerBy: Union[str, None] = None,
    price: Union[str, None] = None,
    orderFilter: Union[str, None] = None,
    timeInForce: Union[str, None] = None,
    reduceOnly: Union[bool, None] = None,
    closeOnTrigger: Union[bool, None] = None,
    positionIdx: Union[int, None] = None,
    orderLinkId: Union[str, None] = None,
) -> PlaceOrderResponse:
    """Place a conditional order that activates when the trigger price is reached."""
    if not TRADING_ENABLED:
        return trading_disabled_response(PlaceOrderResponse)
    params: Dict[str, Any] = {
        "category": category,
        "symbol": symbol,
        "side": side,
        "orderType": orderType,
        "qty": qty,
        "triggerPrice": triggerPrice,
        "triggerDirection": triggerDirection,
    }
    optional = {
        "triggerBy": triggerBy,
        "price": price,
        "orderFilter": orderFilter,
        "timeInForce": timeInForce,
        "reduceOnly": reduceOnly,
        "closeOnTrigger": closeOnTrigger,
        "positionIdx": positionIdx,
        "orderLinkId": orderLinkId,
    }
    params.update({k: v for k, v in optional.items() if v is not None})
    return PlaceOrderResponse(**unwrap(session.place_order(**params)))
