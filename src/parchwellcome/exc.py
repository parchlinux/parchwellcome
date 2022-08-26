from parchwellcome.logger import logger


class SomeFilesNotFoundError(Exception):
    def __call__(self):
        logger.error(
            "Some config files are lost. for more informtion "
            "please see https://parchlinux.ir/parchwellcome/lostfiles"
        )
