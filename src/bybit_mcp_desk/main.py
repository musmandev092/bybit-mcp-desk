"""Async entrypoint for the ByBit MCP Desk server (stdio transport)."""

import asyncio
import logging
from importlib.metadata import PackageNotFoundError, version

from mcp.server.lowlevel import NotificationOptions
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server

from bybit_mcp_desk.server import server

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bybit-mcp-desk")

try:
    __version__ = version("bybit-mcp-desk")
except PackageNotFoundError:  # running from source without an install
    __version__ = "0.1.0"


async def main() -> None:
    logger.info("Starting ByBit MCP Desk server...")
    async with stdio_server() as (read_stream, write_stream):
        logger.info("Server initialized and ready for connections")
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="bybit-mcp-desk",
                server_version=__version__,
                capabilities=server.get_capabilities(NotificationOptions(), {}),
            ),
        )


def cli_main() -> None:
    """Console-script entrypoint that runs the async server."""
    asyncio.run(main())


if __name__ == "__main__":
    cli_main()
