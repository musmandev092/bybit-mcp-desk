"""Read-only order/trade query handlers (open & closed orders, history, executions)."""

from typing import Any, Dict, Union

from bybit_mcp_desk.handlers.base import session, unwrap
from bybit_mcp_desk.models.executions import TradeHistoryResponse
from bybit_mcp_desk.models.orders import OpenClosedOrdersResponse, OrderHistoryResponse


def get_open_closed_orders(
    category: str,
    symbol: Union[str, None] = None,
    baseCoin: Union[str, None] = None,
    settleCoin: Union[str, None] = None,
    orderId: Union[str, None] = None,
    orderLinkId: Union[str, None] = None,
    openOnly: Union[int, None] = None,
    orderFilter: Union[str, None] = None,
    limit: Union[int, None] = None,
    cursor: Union[str, None] = None,
) -> OpenClosedOrdersResponse:
    params: Dict[str, Any] = {"category": category}
    optional = {
        "symbol": symbol,
        "baseCoin": baseCoin,
        "settleCoin": settleCoin,
        "orderId": orderId,
        "orderLinkId": orderLinkId,
        "openOnly": openOnly,
        "orderFilter": orderFilter,
        "limit": limit,
        "cursor": cursor,
    }
    params.update({k: v for k, v in optional.items() if v is not None})
    return OpenClosedOrdersResponse(**unwrap(session.get_open_orders(**params)))


def get_order_history(
    category: str,
    symbol: Union[str, None] = None,
    baseCoin: Union[str, None] = None,
    settleCoin: Union[str, None] = None,
    orderId: Union[str, None] = None,
    orderLinkId: Union[str, None] = None,
    orderFilter: Union[str, None] = None,
    orderStatus: Union[str, None] = None,
    startTime: Union[int, None] = None,
    endTime: Union[int, None] = None,
    limit: Union[int, None] = None,
    cursor: Union[str, None] = None,
) -> OrderHistoryResponse:
    params: Dict[str, Any] = {"category": category}
    optional = {
        "symbol": symbol,
        "baseCoin": baseCoin,
        "settleCoin": settleCoin,
        "orderId": orderId,
        "orderLinkId": orderLinkId,
        "orderFilter": orderFilter,
        "orderStatus": orderStatus,
        "startTime": startTime,
        "endTime": endTime,
        "limit": limit,
        "cursor": cursor,
    }
    params.update({k: v for k, v in optional.items() if v is not None})
    return OrderHistoryResponse(**unwrap(session.get_order_history(**params)))


def get_trade_history(
    category: str,
    symbol: Union[str, None] = None,
    orderId: Union[str, None] = None,
    orderLinkId: Union[str, None] = None,
    baseCoin: Union[str, None] = None,
    startTime: Union[int, None] = None,
    endTime: Union[int, None] = None,
    execType: Union[str, None] = None,
    limit: Union[int, None] = None,
    cursor: Union[str, None] = None,
) -> TradeHistoryResponse:
    params: Dict[str, Any] = {"category": category}
    optional = {
        "symbol": symbol,
        "orderId": orderId,
        "orderLinkId": orderLinkId,
        "baseCoin": baseCoin,
        "startTime": startTime,
        "endTime": endTime,
        "execType": execType,
        "limit": limit,
        "cursor": cursor,
    }
    params.update({k: v for k, v in optional.items() if v is not None})
    return TradeHistoryResponse(**unwrap(session.get_executions(**params)))
