"""Project configuration.

All settings are read from environment variables.
For local development, you can use a `.env` file (see `.env.example`).
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv


# Load .env if present (no-op in most hosted environments)
load_dotenv()


def _get_required(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(
            f"Missing required environment variable: {name}. "
            f"Set it in your environment or in a .env file."
        )
    return value


# Telegram / Pyrogram
API_ID: int = int(os.getenv("API_ID", "33323751"))
API_HASH: str = os.getenv("API_HASH", "6e59ca67a879556faea7e30e868e6d78")
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "7987111241:AAFEHA77h-gr4AAVB9psX9NCdVcbbwwd9aE")

# If you prefer to hard-fail when running the bot without credentials,
# validate in main.py at startup.


# Classplus API base URL
# NOTE: The actual endpoints depend on your integration. Keep this configurable.
CLASSPLUS_API_BASE: str = os.getenv("CLASSPLUS_API_BASE", "https://example.com/api")


# Temp directory for generated HTML files
_BASE_DIR = Path(__file__).resolve().parent
TMP_DIR: str = os.getenv("TMP_DIR", str(_BASE_DIR / "tmp"))
