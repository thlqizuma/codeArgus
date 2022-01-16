# -*-coding:utf-8 -*-

"""
@Author:    chaoli
@DateTime:  2022/1/16 4:29 下午
@Contact:   qizuma@126.com
@Version:   1.0
@File:      logger.py
@Desc:      customized logger
"""
import os
import logging
from logging.handlers import TimedRotatingFileHandler

level_map = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critircal": logging.CRITICAL
}


def mk_dir(path):
    try:
        if path is None:
            pass
        else:
            os.stat(path)
    except Exception:
        os.makedirs(path)


def init_logger(log_name, log_dir=None):
    mk_dir(log_dir)

    if log_name not in logging.Logger.manager.loggerDict:
        # logging.root = logging.getLogger()
        # 必须先删除默认logger，否则会打印多遍日志
        logging.root.handlers.clear()
        logger = logging.getLogger(log_name)
        logger.setLevel(logging.DEBUG)

        # 定义日志格式
        datefmt = "%Y-%m-%d %H:%M:%S"
        format_str = "[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s:%(funcName)s] %(message)s"
        formatter = logging.Formatter(fmt=format_str, datefmt=datefmt)

        # 定义屏幕handler，级别为DEBUG
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        if log_dir:
            file_info_handler = TimedRotatingFileHandler(
                filename=os.path.join(log_dir, f"{log_name}.log"), when="D", backupCount=7
            )
            file_info_handler.setLevel(logging.INFO)
            file_info_handler.setFormatter(formatter)
            logger.addHandler(file_info_handler)

            file_error_handler = TimedRotatingFileHandler(
                filename=os.path.join(log_dir, "%s_error.log" % log_name), when="D", backupCount=7
            )
            file_error_handler.setLevel(logging.ERROR)
            file_error_handler.setFormatter(formatter)
            logger.addHandler(file_error_handler)

        logger = logging.getLogger(log_name)
        return logger


def set_logger_level(logger, level="info"):
    assert level in level_map.keys(), f"level应为{list(level_map.keys())}中的值"
    logger.setLevel(level_map[level])
    for h in logger.handlers:
        h.setLevel(level_map[level])


if __name__ == '__main__':
    my_logger = init_logger("argus", log_dir=".")
    my_logger.info("info test.")
    my_logger.warning("warning test.")
    my_logger.error("error test.")
