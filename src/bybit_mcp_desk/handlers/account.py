"""Read-only account handlers: wallet/coin balances, account info, borrow quota."""

from typing import Any, Dict, Union

from bybit_mcp_desk.handlers.base import session, unwrap
from bybit_mcp_desk.models.account import (
    AccountInfoResponse,
    SingleCoinBalanceResponse,
    WalletBalanceResponse,
)
from bybit_mcp_desk.models.orders import SpotBorrowQuotaResponse


def get_wallet_balance(accountType: str, coin: Union[str, None] = None) -> WalletBalanceResponse:
    params: Dict[str, Any] = {"accountType": accountType}
    if coin:
        params["coin"] = coin
    return WalletBalanceResponse(**unwrap(session.get_wallet_balance(**params)))


def get_single_coin_balance(
    accountType: str,
    coin: str,
    memberId: Union[str, None] = None,
    toAccountType: Union[str, None] = None,
    toMemberId: Union[str, None] = None,
    withBonus: Union[int, None] = None,
) -> SingleCoinBalanceResponse:
    params: Dict[str, Any] = {"accountType": accountType, "coin": coin}
    optional = {"memberId": memberId, "toAccountType": toAccountType, "toMemberId": toMemberId, "withBonus": withBonus}
    params.update({k: v for k, v in optional.items() if v is not None})
    return SingleCoinBalanceResponse(**unwrap(session.get_coin_balance(**params)))


def get_account_info() -> AccountInfoResponse:
    return AccountInfoResponse(**unwrap(session.get_account_info()))


def get_spot_borrow_quota(category: str, symbol: str, side: str) -> SpotBorrowQuotaResponse:
    """Query available balance / borrow quota for spot & margin trading."""
    response = session.get_borrow_quota(category=category, symbol=symbol, side=side)
    return SpotBorrowQuotaResponse(**unwrap(response))
