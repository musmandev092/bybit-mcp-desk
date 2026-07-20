"""Response models for position management actions (leverage, margin, stops)."""

from pydantic import BaseModel

from .common import BaseApiResponse


class SetLeverageResult(BaseModel):
    pass


class SetLeverageResponse(BaseApiResponse):
    result: SetLeverageResult


class SwitchMarginModeResult(BaseModel):
    pass


class SwitchMarginModeResponse(BaseApiResponse):
    result: SwitchMarginModeResult


class SwitchPositionModeResult(BaseModel):
    pass


class SwitchPositionModeResponse(BaseApiResponse):
    result: SwitchPositionModeResult


class SetTradingStopResult(BaseModel):
    pass


class SetTradingStopResponse(BaseApiResponse):
    result: SetTradingStopResult


class SetAutoAddMarginResult(BaseModel):
    pass


class SetAutoAddMarginResponse(BaseApiResponse):
    result: SetAutoAddMarginResult


class AddReduceMarginResult(BaseModel):
    positionIdx: int
    riskId: int
    riskLimitValue: str
    symbol: str
    side: str
    size: str
    avgPrice: str
    liqPrice: str
    bustPrice: str
    positionValue: str
    leverage: str
    autoAddMargin: int
    positionStatus: str
    positionIM: str
    positionMM: str
    unrealisedPnl: str
    cumRealisedPnl: str
    createdTime: str
    updatedTime: str


class AddReduceMarginResponse(BaseApiResponse):
    result: AddReduceMarginResult
