from logging import getLogger

import colorlog

__all__ = "logger"

handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter("%(log_color)s%(levelname)s:%(name)s:%(message)s")
)

logger = getLogger(__name__)
logger.addHandler(handler)
