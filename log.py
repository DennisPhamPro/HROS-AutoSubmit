import logging
from config import log_config
from logging import config

class Log:
    def __init__(self, path) -> None:
        log_config["handlers"]["file"]["filename"] = path
        config.dictConfig(log_config)
        self._log = logging.getLogger("log-submit")
        # self._log["handlers"]["file"]["filename"] = path

    def Write_Debug(self, s: str):
        self._log.debug(s)

    def Write_Info(self, s: str):
        self._log.info(s)

    def Write_Warning(self, s: str):
        self._log.warning(s)

    def Write_Error(self, s: str):
        self._log.error(s)

    def Write_Critical(self, s: str):
        self._log.critical(s)