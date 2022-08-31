from logging import getLogger

import colorlog

__all__ = "logger"

handler = colorlog.StreamHandler()
handler.setFormatter(
    colorlog.ColoredFormatter("%(log_color)s%(levelname)s: %(message)s")
)


def logger(module):
    logger = getLogger(module)
    logger.addHandler(handler)
    return logger
