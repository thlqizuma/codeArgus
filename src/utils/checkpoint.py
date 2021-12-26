# -*-coding:utf-8 -*-

"""
@Author:    chaoli
@DateTime:  2021/12/26 10:20 下午
@Contact:   qizuma@126.com
@Version:   1.0
@File:      checkpoint.py
@Desc:      
"""


class ModelCheckpoint(object):
    def __init__(self, model_dir, metrics_key, save_best_only=True, max_to_keep=2):
        self.model_dir = model_dir
        self.metrics_key = metrics_key
        self.save_best_only = save_best_only
        self.max_to_keep = max_to_keep

    def _save_latest_checkpoint(self):
        """保存最近的max_to_keep个模型，其余将被删除"""
        pass

    def save(self):
        pass