"""Load MCP Tool definitions from the declarative JSON schema files.

Schemas directly under ``schemas/`` are always available. Schemas under
``schemas/trading/`` describe write operations and are only exposed when trading
is enabled.
"""

import json
from functools import lru_cache
from pathlib import Path
from typing import List, Tuple

from mcp.types import Tool

_SCHEMA_DIR = Path(__file__).parent / "schemas"


def _load_file(path: Path) -> List[Tool]:
    entries = json.loads(path.read_text())
    return [Tool(name=e["name"], description=e["description"], inputSchema=e["inputSchema"]) for e in entries]


@lru_cache(maxsize=2)
def _cached_tools(trading_enabled: bool) -> Tuple[Tool, ...]:
    tools: List[Tool] = []
    for path in sorted(_SCHEMA_DIR.glob("*.json")):
        tools.extend(_load_file(path))
    if trading_enabled:
        for path in sorted((_SCHEMA_DIR / "trading").glob("*.json")):
            tools.extend(_load_file(path))
    return tuple(tools)


def load_tools(trading_enabled: bool) -> List[Tool]:
    """Return the Tool list (schemas are parsed once per flag value, then cached)."""
    return list(_cached_tools(trading_enabled))
