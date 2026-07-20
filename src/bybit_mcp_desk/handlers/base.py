"""Shared helpers for API handlers: the session, response unwrapping, and the
trading-disabled fallback used as a second guard on write operations.
"""

from typing import Any, Type, TypeVar

from bybit_mcp_desk.config import TRADING_ENABLED, session
from bybit_mcp_desk.models.common import BaseApiResponse
from bybit_mcp_desk.models.orders import (
    AmendOrderResponse,
    BatchAmendOrderResponse,
    BatchCancelOrderResponse,
    BatchPlaceOrderResponse,
    CancelAllOrdersResponse,
    CancelOrderResponse,
    OrderItemResult,
    PlaceOrderResponse,
)

__all__ = ["TRADING_ENABLED", "session", "unwrap", "trading_disabled_response"]

TRADING_DISABLED_RET_CODE = 40300
TRADING_DISABLED_RET_MSG = "Trading operations are disabled by server configuration."

T = TypeVar("T", bound=BaseApiResponse)


def unwrap(response: Any) -> Any:
    """pybit occasionally returns a (result, elapsed, ...) tuple; take the payload."""
    if isinstance(response, tuple):
        return response[0]
    return response


def trading_disabled_response(response_model: Type[T]) -> T:
    """Build a synthetic 'trading disabled' response for the given model."""
    kwargs: dict[str, Any] = {"retCode": TRADING_DISABLED_RET_CODE, "retMsg": TRADING_DISABLED_RET_MSG}
    if response_model in (PlaceOrderResponse, AmendOrderResponse, CancelOrderResponse):
        kwargs["result"] = OrderItemResult(orderId="", orderLinkId="")
    elif response_model == CancelAllOrdersResponse:
        kwargs["result"] = {"list": []}
    elif response_model in (BatchPlaceOrderResponse, BatchAmendOrderResponse, BatchCancelOrderResponse):
        kwargs["result"] = {"list": []}
    return response_model(**kwargs)
