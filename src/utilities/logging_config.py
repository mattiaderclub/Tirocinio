import logging

from rich.logging import RichHandler


def setup_logging(
    log_level=logging.INFO, log_format: str = "%(message)s"
) -> logging.Logger:
    logger = logging.getLogger()

    logger.setLevel(log_level)

    if not any(isinstance(handler, RichHandler) for handler in logger.handlers):
        console_handler = RichHandler(
            rich_tracebacks=True, show_time=False, show_path=False
        )

        formatter = logging.Formatter(log_format)
        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger
