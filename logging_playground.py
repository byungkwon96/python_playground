# by default only importance of warning of above gets printed
import logging

logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
# warning, error, critical got pritnined

# only works if you put after the import
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
)
print("---------------NEW CONFIG -----------")
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# helper logging
logger = logging.getLogger(__name__)
logger.propogate = False
logger.info("hello from helper")

# log handlers
logger = logging.getLogger(__name__)
stream_h = logging.StreamHandler()
file_h = logging.FileHandler("file.log")

# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

# set the format and connect to handlers
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

# add log handlers into the loger
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is a warning")
logger.error("This is an error")

# File config and dict config method
# in other files such as logging.config
"""
[handlers]
keys=consoleHandler

[formatters]
keys=simpleFormatter

[logger_root]
level=DEBUG
handlers=consoleHandler

[logger_simpleExample]
level=DEBUG
handlers=consoleHandler
qualname=simpleExample
propagate=0

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=simpleFormatter
args(sys.stdout,)

[formatter_simpleFormmater]
format = %(name)s - %(levelname)s - %(message)s
"""
# TO USE LOGGING.CONFIG import and use them as other logger
# import logging.config
# logging.config.fileConfig('logging.conf)
# logger = logging.getLogger('simpleExample')
# logger.debug('this is a debug message')

# Capturing Logger (Stack trace) helpful for trouble shooting
import traceback

try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error(e, exc_info=True)
except Exception as e:
    logging.error("Ther error is %s", traceback.format_exc())

# logs 5 files with specific size
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc
handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
logger.addHandler(handler)

handlerT = TimedRotatingFileHandler(
    "timed_test.log", when="s", interval=5, backupCount=5
)
# logger.addHandler(handlerT)
