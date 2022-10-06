import logging
import os
from config import log_config
from logging import config
from datetime import datetime

class Log:
    def __init__(self, path: str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)
        log_config["handlers"]["file"]["filename"] = path + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + ".log"
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
        self._log.error(s, exc_info=True)

    def Write_Critical(self, s: str):
        self._log.critical(s)