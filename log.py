import logging
import os
import sys
from config import log_config
from logging import config
from datetime import datetime
from termcolor import colored

class Log:
    def __init__(self, path: str) -> None:
        if not os.path.exists(path):
            os.makedirs(path)
        log_config["handlers"]["file"]["filename"] = path + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%P')) + ".log"
        config.dictConfig(log_config)
        self._log = logging.getLogger("log-submit")

    def Write_Debug(self, s: str):
        self._log.debug(colored(s,'yellow'))

    def Write_Info(self, s: str):
        self._log.info(colored(s,'green',attrs=['blink']))

    def Write_Warning(self, s: str):
        self._log.warning(colored(s,'red',attrs=["reverse", "bold"]))

    def Write_Error(self, s: str):
        self._log.error(s, exc_info=True)

    def Write_Critical(self, s: str):
        self._log.critical(colored(s,'red',attrs=["reverse", "bold"]))
