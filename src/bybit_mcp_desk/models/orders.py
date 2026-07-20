"""Response models for order placement, amendment, cancellation and history."""

from typing import List, Optional

from pydantic import BaseModel

from .common import BaseApiResponse


class OrderItemResult(BaseModel):
    orderId: str
    orderLinkId: str


class SingleOrderItemApiResponse(BaseApiResponse):
    result: OrderItemResult


class PlaceOrderResponse(SingleOrderItemApiResponse):
    pass


class AmendOrderResponse(SingleOrderItemApiResponse):
    pass


class CancelOrderResponse(SingleOrderItemApiResponse):
    pass


class Order(BaseModel):
    orderId: str
    orderLinkId: str
    blockTradeId: str
    symbol: str
    price: str
    qty: str
    side: str
    isLeverage: str
    positionIdx: int
    orderStatus: str
    createType: Optional[str] = None
    cancelType: str
    rejectReason: str
    avgPrice: str
    leavesQty: str
    leavesValue: str
    cumExecQty: str
    cumExecValue: str
    cumExecFee: str
    timeInForce: str
    orderType: str
    stopOrderType: str
    orderIv: str


class PaginatedOrderListResult(BaseModel):
    category: str
    nextPageCursor: str
    list: List[Order]


class OpenClosedOrdersResponse(BaseApiResponse):
    result: PaginatedOrderListResult


class OrderHistoryResponse(BaseApiResponse):
    result: PaginatedOrderListResult


class CancelAllResultItem(OrderItemResult):
    success: Optional[str] = None


class CancelAllOrdersResult(BaseModel):
    list: List[CancelAllResultItem]


class CancelAllOrdersResponse(BaseApiResponse):
    result: CancelAllOrdersResult


class BatchOperationItemBase(OrderItemResult):
    category: str
    symbol: str
    code: Optional[int] = None
    msg: Optional[str] = None


class BatchPlaceOrderItem(BatchOperationItemBase):
    createAt: Optional[str] = None


class BatchPlaceOrderResult(BaseModel):
    list: List[BatchPlaceOrderItem]


class BatchPlaceOrderResponse(BaseApiResponse):
    result: BatchPlaceOrderResult


class BatchAmendOrderItemResult(BatchOperationItemBase):
    pass


class BatchAmendOrderResult(BaseModel):
    list: List[BatchAmendOrderItemResult]


class BatchAmendOrderResponse(BaseApiResponse):
    result: BatchAmendOrderResult


class BatchCancelOrderItemResult(BatchOperationItemBase):
    pass


class BatchCancelOrderResult(BaseModel):
    list: List[BatchCancelOrderItemResult]


class BatchCancelOrderResponse(BaseApiResponse):
    result: BatchCancelOrderResult


class SpotBorrowQuotaResult(BaseModel):
    symbol: str
    side: str
    maxTradeQty: str
    maxTradeAmount: str
    spotMaxTradeQty: str
    spotMaxTradeAmount: str
    borrowCoin: str


class SpotBorrowQuotaResponse(BaseApiResponse):
    result: SpotBorrowQuotaResult
