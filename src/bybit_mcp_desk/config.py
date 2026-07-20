"""Environment configuration and the shared Bybit HTTP session.

All reads of environment/config go through this module so credentials and feature
flags live in exactly one place.
"""

import os

from dotenv import load_dotenv
from pybit.unified_trading import HTTP

load_dotenv()

BYBIT_API_KEY = os.getenv("BYBIT_API_KEY")
BYBIT_API_SECRET = os.getenv("BYBIT_API_SECRET")
USE_TESTNET = os.getenv("BYBIT_TESTNET", "false").lower() in ("true", "1")
TRADING_ENABLED = os.getenv("BYBIT_TRADING_ENABLED", "false").lower() in ("true", "1")

# Single shared session reused by every handler.
session = HTTP(
    testnet=USE_TESTNET,
    api_key=BYBIT_API_KEY,
    api_secret=BYBIT_API_SECRET,
)
