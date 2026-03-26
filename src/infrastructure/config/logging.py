import logging
from logging.config import dictConfig


def configure_logging() -> None:
    dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": {
                    "format": "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
                }
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "formatter": "standard",
                }
            },
            "root": {
                "handlers": ["default"],
                "level": "INFO",
            },
            "loggers": {
                "uvicorn": {"level": "INFO", "propagate": True},
                "uvicorn.error": {"level": "INFO", "propagate": True},
                "uvicorn.access": {"level": "INFO", "propagate": True},
                "fastapi": {"level": "INFO", "propagate": True},
            },
        }
    )


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)