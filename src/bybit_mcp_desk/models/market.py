"""Response models for core market-data endpoints (tickers, book, trades, klines)."""

from pydantic import BaseModel


class ServerTimeResponse(BaseModel):
    timeSecond: str


class TickerItem(BaseModel):
    symbol: str
    bid1Price: str
    bid1Size: str
    ask1Price: str
    ask1Size: str
    lastPrice: str
    prevPrice24h: str
    price24hPcnt: str


class TickerResponse(BaseModel):
    category: str
    list: list[TickerItem]


class OrderBookItem(BaseModel):
    price: str
    size: str


class OrderBookResponse(BaseModel):
    s: str  # symbol
    b: list[list[str]]  # bids: [[price, size], ...]
    a: list[list[str]]  # asks: [[price, size], ...]
    ts: int
    u: int
    seq: int
    cts: int


class RecentTradeItem(BaseModel):
    execId: str
    symbol: str
    price: str
    size: str
    side: str
    time: str
    isBlockTrade: bool
    isRPITrade: bool
    # Option-only fields
    mP: str | None = None
    iP: str | None = None
    mIv: str | None = None
    iv: str | None = None


class RecentTradesResponse(BaseModel):
    category: str
    list: list[RecentTradeItem]


class KlineItem(BaseModel):
    startTime: str
    openPrice: str
    highPrice: str
    lowPrice: str
    closePrice: str
    volume: str
    turnover: str


class KlineResponse(BaseModel):
    category: str
    symbol: str
    list: list[list[str]]
