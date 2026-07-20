"""Response models for reference/statistics market endpoints."""

from pydantic import BaseModel


class LeverageFilter(BaseModel):
    minLeverage: str
    maxLeverage: str
    leverageStep: str


class PriceFilter(BaseModel):
    minPrice: str
    maxPrice: str
    tickSize: str


class LotSizeFilter(BaseModel):
    maxOrderQty: str
    minOrderQty: str
    qtyStep: str
    postOnlyMaxOrderQty: str | None = None
    maxMktOrderQty: str | None = None
    minNotionalValue: str | None = None


class RiskParameters(BaseModel):
    priceLimitRatioX: str | None = None
    priceLimitRatioY: str | None = None


class InstrumentInfoItem(BaseModel):
    symbol: str
    contractType: str
    status: str
    baseCoin: str
    quoteCoin: str
    launchTime: str
    deliveryTime: str
    deliveryFeeRate: str | None = None
    priceScale: str
    leverageFilter: LeverageFilter
    priceFilter: PriceFilter
    lotSizeFilter: LotSizeFilter
    unifiedMarginTrade: bool | None = None
    fundingInterval: int | None = None
    settleCoin: str
    copyTrading: str | None = None
    upperFundingRate: str | None = None
    lowerFundingRate: str | None = None
    isPreListing: bool | None = None
    preListingInfo: dict | None = None
    riskParameters: RiskParameters | None = None
    optionType: str | None = None
    volScale: str | None = None


class InstrumentsInfoResponse(BaseModel):
    category: str
    list: list[InstrumentInfoItem]
    nextPageCursor: str | None = None


class FundingRateHistoryItem(BaseModel):
    symbol: str
    fundingRate: str
    fundingRateTimestamp: str


class FundingRateHistoryResponse(BaseModel):
    category: str
    list: list[FundingRateHistoryItem]
    nextPageCursor: str | None = None


class OpenInterestItem(BaseModel):
    openInterest: str
    timestamp: str


class OpenInterestResponse(BaseModel):
    symbol: str
    category: str
    list: list[OpenInterestItem]
    nextPageCursor: str | None = None


class InsuranceItem(BaseModel):
    coin: str
    symbols: str
    balance: str
    value: str


class InsuranceResponse(BaseModel):
    updatedTime: str
    list: list[InsuranceItem]


class RiskLimitItem(BaseModel):
    id: int
    symbol: str
    riskLimitValue: str


class RiskLimitResponse(BaseModel):
    category: str
    list: list[RiskLimitItem]
    nextPageCursor: str | None = None


class LongShortRatioItem(BaseModel):
    symbol: str
    buyRatio: str
    sellRatio: str
    timestamp: str


class LongShortRatioResponse(BaseModel):
    list: list[LongShortRatioItem]
    nextPageCursor: str | None = None
