"""Response models for reading positions and closed PnL."""

from typing import List, Optional

from pydantic import BaseModel, ConfigDict

from .common import BaseApiResponse


class PositionInfoItem(BaseModel):
    positionIdx: int
    riskId: int
    riskLimitValue: str
    symbol: str
    side: str
    size: str
    avgPrice: str
    positionValue: str
    tradeMode: int
    autoAddMargin: int
    positionStatus: str
    leverage: str
    markPrice: str
    liqPrice: str
    bustPrice: str
    positionIM: str
    positionMM: str
    positionBalance: str
    takeProfit: str
    stopLoss: str
    trailingStop: str
    sessionAvgPrice: Optional[str] = None  # USDC contracts
    delta: Optional[str] = None  # options only
    gamma: Optional[str] = None  # options only
    vega: Optional[str] = None  # options only
    theta: Optional[str] = None  # options only
    unrealisedPnl: str
    curRealisedPnl: str
    cumRealisedPnl: str
    adlRankIndicator: int
    createdTime: str
    updatedTime: str
    tpslMode: Optional[str] = None
    tpLimitPrice: Optional[str] = None
    slLimitPrice: Optional[str] = None
    tpTriggerBy: Optional[str] = None
    slTriggerBy: Optional[str] = None
    seq: Optional[int] = None
    isReduceOnly: Optional[bool] = None
    mmrSysUpdatedTime: Optional[str] = None
    leverageSysUpdatedTime: Optional[str] = None

    model_config = ConfigDict(extra="allow")


class PositionInfoResult(BaseModel):
    category: str
    nextPageCursor: str
    list: List[PositionInfoItem]


class GetPositionInfoResponse(BaseApiResponse):
    result: PositionInfoResult


class ClosedPnlItem(BaseModel):
    symbol: str
    orderId: str
    side: str
    qty: str
    orderPrice: str
    orderType: str
    execType: str
    closedSize: str
    cumEntryValue: str
    avgEntryPrice: str
    cumExitValue: str
    avgExitPrice: str
    closedPnl: str
    fillCount: str
    leverage: str
    createdTime: str


class ClosedPnlResult(BaseModel):
    nextPageCursor: str
    category: str
    list: List[ClosedPnlItem]


class GetClosedPnlResponse(BaseApiResponse):
    result: ClosedPnlResult
