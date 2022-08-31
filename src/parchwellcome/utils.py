from __future__ import annotations

import gettext
import os
import sys
from pathlib import Path
from shutil import copy
from webbrowser import open

from exc import SomeFilesNotFoundError
from logger import logger

HOME = Path().home()
AUTOSTART_PATH = HOME / ".config/autostart/parchwellcome.desktop"
CONFIG_PATH = HOME / ".parch/wellcome"

gettext.bindtextdomain(
    "parchwellcome", Path(os.path.dirname(os.path.abspath(__file__))) / "locales"
)
gettext.textdomain("parchwellcome")
_ = gettext.gettext


def open_broswer(url: str) -> None:
    open(url)
    logger.info(_("%s is opened" % url))


def add_remove_autostart(add: bool = True) -> None:
    if not isinstance(add, bool):
        logger.error(_("add must be bool not %s" % type(add)))
        sys.exit(1)

    if not (CONFIG_PATH / "autostart.desktop").exists():
        raise SomeFilesNotFoundError

    if add:
        copy((CONFIG_PATH / "autostart.desktop").as_posix(), AUTOSTART_PATH.as_posix())
        logger.info(_("autostart is enable"))
        return None

    if not CONFIG_PATH.exists():
        logger.warning("autostart was disabled")
        return None

    AUTOSTART_PATH.unlink()
    logger.info(_("autostart is disable"))
    return None
