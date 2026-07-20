"""MCP server instance and protocol handler registration."""

import logging
from typing import Any, Dict, List

from mcp.server import Server
from mcp.types import Resource, TextContent, Tool
from pydantic import AnyUrl

from bybit_mcp_desk import resources
from bybit_mcp_desk.config import TRADING_ENABLED
from bybit_mcp_desk.registry import dispatch
from bybit_mcp_desk.tools import load_tools

logger = logging.getLogger("bybit-mcp-desk")

server = Server("bybit-mcp-desk")


@server.list_tools()
async def handle_list_tools() -> List[Tool]:
    return load_tools(TRADING_ENABLED)


@server.call_tool()
async def handle_call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    try:
        return await dispatch(name, arguments)
    except Exception as exc:  # surface the error to the client instead of crashing
        logger.error("Error calling tool %s with %s: %s", name, arguments, exc, exc_info=True)
        return [TextContent(type="text", text=f"Error calling {name}: {exc}")]


@server.list_resources()
async def handle_list_resources() -> List[Resource]:
    return resources.list_resources()


@server.read_resource()
async def handle_read_resource(uri: AnyUrl) -> str:
    return resources.read_resource(uri)
