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
    """
    参考：https://zhuanlan.zhihu.com/p/288251816
    """
    def __init__(self, num_buckets=200):
        self._num_buckets = num_buckets
        self._table = np.zeros(shape=[2, self._num_buckets])

    def reset(self):
        self._table = np.zeros(shape=[2, self._num_buckets])

    def update(self, labels: np.ndarray, predicts: np.ndarray):
        """
        @param labels: 1-D ndarray
        @param predicts:  1-D ndarray
        @return: None
        """
        labels = labels.astype(int)
        predicts = self._num_buckets * predicts

        buckets = np.round(predicts).astype(int)
        buckets = np.where(
            buckets >= self._num_buckets,
            self._num_buckets-1, buckets
        )

        for i in range(len(labels)):
            self._table[labels[i], buckets[i]] += 1

    def compute(self):
        tp = 0
        fp = 0
        area = 0
        for i in range(self._num_buckets):
            new_tp = tp + self._table[1, i]
            new_fp = fp + self._table[0, i]

            area += (new_tp - tp) * (fp + new_fp) / 2.0
            # area += (new_fp - fp) * (tp + new_tp) / 2.0
            tp = new_tp
            fp = new_fp
        if tp < 1e-3 or fp < 1e-3:
            return -0.5
        return area / (tp * fp)


if __name__ == '__main__':
    from sklearn import metrics
    label = np.random.randint(low=0, high=2, size=[1000])
    predict = np.random.uniform(0, 1, size=[1000])
    auc = AucMeter(num_buckets=102400)
    auc.update(label, predict)
    print(auc.compute())
    print(metrics.roc_auc_score(label, predict))
