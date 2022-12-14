import logging
from selenium.webdriver.chrome.options import Options

class AboveInfo(logging.Filter):
    def filter(self, record):
        if record.levelno >10:
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
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False
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
            # "filters": ["above_info"],
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "filename": "stupid_logs.log",
            # "filename": ("all_messages" + str(datetime.now().strftime('%Y_%M_%d_%H_%M_%S')) + ".log"), #file path (can use os to get true path)
            "mode": "w" #set filemode
        }, 
    },
    "formatters":{
        "std_out": {
            "format": "%(asctime)s : %(levelname)s: %(name)s : %(module)s : %(funcName)s : %(lineno)d : Log : %(message)s",
            "datefmt":"%d-%m-%Y %I:%M:%S(%p)" # https://www.w3schools.com/python/python_datetime.asp for date format syntax
        },
        "std_out2": {
            "format": "%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s",
            "datefmt":"%d-%m-%Y %H:%M:%S"
        }
    },
    "filters":{
        "above_info":{
            "()": AboveInfo
        }
    },
}

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
chrome_options.page_load_strategy = 'normal' 