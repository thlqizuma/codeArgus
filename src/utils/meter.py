# -*-coding:utf-8 -*-

"""
@Author:    chaoli
@DateTime:  2022/1/15 9:47 下午
@Contact:   qizuma@126.com
@Version:   1.0
@File:      meter.py
@Desc:      
"""

import numpy as np


class AverageMeter(object):
    def __init__(self):
        self.count = 0
        self.value = 0
        self.sum = 0
        self.avg = 0

    def reset(self):
        self.count = 0
        self.value = 0
        self.sum = 0
        self.avg = 0

    def update(self, value, n=1):
        self.value = value
        self.count += n
        self.sum += value
        self.avg = self.sum / self.count


class AucMeter(object):
    def __init__(self, num_buckets=200):
        self._num_buckets = num_buckets
        self._table = np.zeros(shape=[2, self._num_buckets])
        
    def reset(self):
        self._table = np.zeros(shape=[2, self._num_buckets])
