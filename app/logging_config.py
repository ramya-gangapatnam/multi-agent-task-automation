import logging
from app.config import LOG_LEVEL


def setup_logging() -> None:
    """
    Configure application-wide logging.
    """
    logging.basicConfig(
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    # Reduce noisy third-party logs so orchestration output stays readable.
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("autogen_core").setLevel(logging.WARNING)
    logging.getLogger("autogen_agentchat").setLevel(logging.WARNING)