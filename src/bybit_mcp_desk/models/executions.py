"""Response models for trade executions (fills) history."""

from typing import List, Optional, Union

from pydantic import BaseModel, field_validator

from .common import BaseApiResponse


class TradeExecutionItem(BaseModel):
    symbol: str
    orderId: str
    orderLinkId: Optional[str] = None
    side: str
    orderPrice: str
    orderQty: str
    leavesQty: Optional[str] = None
    createType: Optional[str] = None
    orderType: str
    stopOrderType: Optional[str] = None
    execFee: str
    execId: str
    execPrice: str
    execQty: str
    execType: Optional[str] = None
    execValue: Optional[str] = None
    execTime: str
    feeCurrency: Optional[str] = None
    isMaker: bool
    feeRate: Optional[str] = None
    tradeIv: Optional[str] = None
    markIv: Optional[str] = None
    markPrice: Optional[str] = None
    indexPrice: Optional[str] = None
    underlyingPrice: Optional[str] = None
    blockTradeId: Optional[str] = None
    closedSize: Optional[str] = None
    seq: Optional[Union[str, int]] = None
    extraFees: Optional[str] = None

    @field_validator("seq", mode="before")
    @classmethod
    def convert_seq_to_str(cls, v):
        """The API returns seq as int or str; normalise to str."""
        if v is not None and isinstance(v, int):
            return str(v)
        return v


class TradeHistoryResult(BaseModel):
    category: str
    list: List[TradeExecutionItem]
    nextPageCursor: Optional[str] = None


class TradeHistoryResponse(BaseApiResponse):
    result: TradeHistoryResult
