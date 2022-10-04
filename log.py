import logging
from logging import config
from datetime import datetime

class InfoOnly(logging.Filter):
    def filter(self, record):
        if record.levelno >10 and record.levelno < 21:
            return True
        else:
            return False

log_config = {
    "version":1,
    "root":{
        "handlers" : ["console", "file"],
        "level": "DEBUG"
    },
    "loggers":{
        "log-submit":{
            "handlers": ["Dat_logger"],
            "level": "DEBUG",
            "propagate": True
        },
    },
    "handlers":{
        "console":{
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": "DEBUG"
        },
        "file":{
            "formatter": "std_out2",
            # "filters": ["info"],
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "filename": "all_messages.log", #file path (can use os to get true path)
            "mode": "w" #set filemode
        },
        "Dat_logger":{
            "formatter": "std_out2",
            # "filters": ["info"],
            "class": "logging.FileHandler",
            "level": "INFO",
            "filename":(__name__ + str(datetime.now().strftime('%Y_%M_%d_%H_%M_%S')) + ".log"),
            "mode": "w"
        },
        "Phat_logger":{
            "formatter": "std_out2",
            "class": "logging.FileHandler",
            "level": "WARNING",
            "filename":"PHAT_WARNING_LEVEL.log",
            "mode": "w"
        },
        "Phat_child_logger":{
            "formatter": "std_out2",
            "class": "logging.FileHandler",
            "level": "WARNING",
            "filename":"PHAT_CHILD_WARNING_LEVEL.log",
            "mode": "w"
        },
    },
    "formatters":{
        "std_out": {
            "format": "%(asctime)s : %(levelname)s: %(name)s : %(module)s : %(funcName)s : %(lineno)d : (Process Details : (%(process)d, %(processName)s), Thread Details : (%(thread)d, %(threadName)s))\nLog : %(message)s",
            "datefmt":"%d-%m-%Y %I:%M:%S(%p)S" # https://www.w3schools.com/python/python_datetime.asp for date format syntax
        },
        "std_out2": {
            "format": "%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s",
            "datefmt":"%d-%m-%Y %H:%M:%S"
        }
    },
    "filters":{
        "info":{
            "()": InfoOnly
        }
    },
}

config.dictConfig(log_config)

################ Logger #################
dat_log = logging.getLogger("Dat")

class Addition:
    def __init__(self):
        self.phat_log = logging.getLogger("Phat.child") #This is a child logger of Phat 
        
    def add(self, a, b):
        self.phat_log.debug("Inside Addition Function")
        if isinstance(a, str) and a.isdigit():
            self.phat_log.warning("Warning : Parameter A is passed as String. Future versions won't support it.")

        if isinstance(b, str) and b.isdigit():
            self.phat_log.warning("Warning : Parameter B is passed as String. Future versions won't support it.")

        try:
            result = float(a) + float(b)
            self.phat_log.info("Addition Function Completed Successfully")
            return result
        except Exception as e:
            self.phat_log.error("Error Type : {}, Error Message : {}".format(type(e).__name__, e))
            return None


if __name__ == "__main__":
    dat_log.info("Current Log Level : {}\n".format(dat_log.getEffectiveLevel()))

    addition = Addition()
    result = addition.add(10,20)
    dat_log.info("Addition of {} & {} is : {}\n".format(10,20, result))

    result = addition.add("20",20)
    dat_log.info("Addition of {} & {} is : {}\n".format("'20'",20, result))

    result = addition.add("A",20)
    dat_log.info("Addition of {} & {} is : {}".format("A",20, result))