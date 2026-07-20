"""Response models for wallet balance, single-coin balance and account info."""

from typing import List

from pydantic import BaseModel

from .common import BaseApiResponse


class CoinBalance(BaseModel):
    coin: str
    equity: str
    usdValue: str
    walletBalance: str
    borrowAmount: str
    availableToBorrow: str
    availableToWithdraw: str
    accruedInterest: str
    totalOrderIM: str
    totalPositionIM: str
    totalPositionMM: str
    unrealisedPnl: str
    cumRealisedPnl: str
    bonus: str
    collateralSwitch: bool
    marginCollateral: bool
    locked: str
    spotHedgingQty: str


class WalletBalance(BaseModel):
    accountType: str
    totalEquity: str
    totalWalletBalance: str
    totalMarginBalance: str
    totalAvailableBalance: str
    totalPerpUPL: str
    totalInitialMargin: str
    totalMaintenanceMargin: str
    accountIMRate: str
    accountMMRate: str
    accountLTV: str
    coin: List[CoinBalance]


class WalletBalanceResult(BaseModel):
    list: List[WalletBalance]


class WalletBalanceResponse(BaseApiResponse):
    result: WalletBalanceResult


class SingleCoinBalanceResult(BaseModel):
    accountType: str
    bizType: int
    accountId: str
    memberId: str
    balance: CoinBalance


class SingleCoinBalanceResponse(BaseApiResponse):
    result: SingleCoinBalanceResult


class AccountInfo(BaseModel):
    unifiedMarginStatus: int
    marginMode: str
    dcpStatus: str
    timeWindow: int
    smpGroup: int
    isMasterTrader: bool
    spotHedgingStatus: str
    updatedTime: str


class AccountInfoResponse(BaseApiResponse):
    result: AccountInfo
