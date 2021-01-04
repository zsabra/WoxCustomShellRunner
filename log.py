import datetime
import traceback
import sys
import json
import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(handlers=[
    RotatingFileHandler(
        filename='.log',
        mode='a',
        maxBytes=5*1024*1024,
        backupCount=2,
        encoding='utf-8',
        delay=0
    )
])


def tabJoin(messages):
    return "\t".join(list(map(lambda message: str(message), messages)))


def info(messages):
    logging.info(tabJoin(messages))


def error(messages):
    logging.error(tabJoin(messages))


def debug(messages):
    logging.debug(tabJoin(messages))


def exceptionHandler(exc_type, exc_value, exc_traceback):
    message = "".join(traceback.format_exception(
        exc_type, exc_value, exc_traceback))
    print(message)
    error([message])
    # sys.exit(1)

# print(json.loads(json.dumps(["wt.exe", 'cmd.exe', '/K', 'wsl.exe'])))
