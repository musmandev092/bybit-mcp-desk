"""Bybit API call handlers, grouped by domain and re-exported for the registry."""

from .account import get_account_info, get_single_coin_balance, get_spot_borrow_quota, get_wallet_balance
from .klines import get_index_price_kline, get_kline, get_mark_price_kline, get_premium_index_price_kline
from .market import (
    get_funding_rate_history,
    get_instruments_info,
    get_insurance,
    get_long_short_ratio,
    get_open_interest,
    get_order_book,
    get_recent_trades,
    get_risk_limit,
    get_server_time,
    get_tickers,
)
from .orders import amend_order, cancel_all_orders, cancel_order, place_order
from .orders_batch import batch_amend_order, batch_cancel_order, batch_place_order, place_trigger_order
from .orders_query import get_open_closed_orders, get_order_history, get_trade_history
from .positions import get_closed_pnl, get_position_info
from .positions_manage import set_leverage, switch_cross_isolated_margin, switch_position_mode
from .positions_stops import modify_position_margin, set_auto_add_margin, set_trading_stop

__all__ = [
    "amend_order",
    "batch_amend_order",
    "batch_cancel_order",
    "batch_place_order",
    "cancel_all_orders",
    "cancel_order",
    "get_account_info",
    "get_closed_pnl",
    "get_funding_rate_history",
    "get_index_price_kline",
    "get_instruments_info",
    "get_insurance",
    "get_kline",
    "get_long_short_ratio",
    "get_mark_price_kline",
    "get_open_closed_orders",
    "get_open_interest",
    "get_order_book",
    "get_order_history",
    "get_position_info",
    "get_premium_index_price_kline",
    "get_recent_trades",
    "get_risk_limit",
    "get_server_time",
    "get_single_coin_balance",
    "get_spot_borrow_quota",
    "get_tickers",
    "get_trade_history",
    "get_wallet_balance",
    "modify_position_margin",
    "place_order",
    "place_trigger_order",
    "set_auto_add_margin",
    "set_leverage",
    "set_trading_stop",
    "switch_cross_isolated_margin",
    "switch_position_mode",
]
