# -*-coding:utf-8 -*-

"""
@Author:    chaoli
@DateTime:  2022/1/16 4:29 下午
@Contact:   qizuma@126.com
@Version:   1.0
@File:      base.py
@Desc:      base class with logger
"""
from abc import ABC

from ..utils import logger


class ClsBase(ABC):
    def __init__(self, log_level="info", log_dir=None):
        super(ClsBase, self).__init__()
        self.class_name = self.__class__.__name__

        # log信息
        self.log_dir = log_dir
        self.logger = logger.init_logger(log_name=self.class_name, log_dir=self.log_dir)
        logger.set_logger_level(self.logger, log_level)
