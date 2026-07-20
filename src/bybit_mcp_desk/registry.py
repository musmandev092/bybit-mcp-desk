"""Tool dispatch: map each tool name to its handler and format the result.

Adding a tool means adding one entry here plus its JSON schema and handler — no
growing if/elif chain.
"""

import asyncio
import json
from typing import Any, Callable, Dict, List

from mcp.types import TextContent

from bybit_mcp_desk import handlers as h

HANDLERS: Dict[str, Callable[..., Any]] = {
    # Market data
    "get_server_time": h.get_server_time,
    "get_tickers": h.get_tickers,
    "get_order_book": h.get_order_book,
    "get_recent_trades": h.get_recent_trades,
    "get_kline": h.get_kline,
    "get_mark_price_kline": h.get_mark_price_kline,
    "get_index_price_kline": h.get_index_price_kline,
    "get_premium_index_price_kline": h.get_premium_index_price_kline,
    "get_instruments_info": h.get_instruments_info,
    "get_funding_rate_history": h.get_funding_rate_history,
    "get_open_interest": h.get_open_interest,
    "get_insurance": h.get_insurance,
    "get_risk_limit": h.get_risk_limit,
    "get_long_short_ratio": h.get_long_short_ratio,
    # Account / read-only
    "get_open_closed_orders": h.get_open_closed_orders,
    "get_order_history": h.get_order_history,
    "get_trade_history": h.get_trade_history,
    "get_wallet_balance": h.get_wallet_balance,
    "get_single_coin_balance": h.get_single_coin_balance,
    "get_account_info": h.get_account_info,
    "get_spot_borrow_quota": h.get_spot_borrow_quota,
    "get_position_info": h.get_position_info,
    "get_closed_pnl": h.get_closed_pnl,
    # Trading (gated)
    "place_order": h.place_order,
    "amend_order": h.amend_order,
    "cancel_order": h.cancel_order,
    "cancel_all_orders": h.cancel_all_orders,
    "batch_place_order": h.batch_place_order,
    "batch_amend_order": h.batch_amend_order,
    "batch_cancel_order": h.batch_cancel_order,
    "place_trigger_order": h.place_trigger_order,
    "set_leverage": h.set_leverage,
    "switch_cross_isolated_margin": h.switch_cross_isolated_margin,
    "switch_position_mode": h.switch_position_mode,
    "set_trading_stop": h.set_trading_stop,
    "set_auto_add_margin": h.set_auto_add_margin,
    "modify_position_margin": h.modify_position_margin,
}


def _format(name: str, result: Any) -> str:
    """Serialize a handler result. Pydantic models use the fast Rust JSON encoder;
    get_server_time returns a plain dict, which falls back to json.dumps."""
    if hasattr(result, "model_dump_json"):
        body = result.model_dump_json(indent=2)
    else:
        body = json.dumps(result, indent=2, default=str)
    return f"{name}:\n{body}"


async def dispatch(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    handler = HANDLERS.get(name)
    if handler is None:
        return [TextContent(type="text", text=f"Unknown tool: {name}")]
    # pybit performs blocking network I/O; run it off the event loop so the
    # server stays responsive to other protocol messages while a call is in flight.
    result = await asyncio.to_thread(handler, **arguments)
    return [TextContent(type="text", text=_format(name, result))]
