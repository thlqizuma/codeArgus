# -*-coding:utf-8 -*-

"""
@Author:    chaoli
@DateTime:  2021/12/26 4:33 下午
@Contact:   qizuma@126.com
@Version:   1.0
@File:      early_stop.py
@Desc:      
"""


class EarlyStop(object):
    def __init__(self, metrics_key='loss', patience=2, higher_is_better=False):
        self.metrics_key = metrics_key
        self.higher_is_better = higher_is_better
        self.patience = patience
        self.patience_cnt = patience

        self.previous_metrics = None
        self.best_metrics = None

    def should_stop(self, eval_result):
        if self.metrics_key not in eval_result:
            raise ValueError(
                "metrics key is not in eval result {}", eval_result
            )

        previous_metrics = self.previous_metrics
        curr_metrics = eval_result[self.metrics_key]

        import numpy as np
        is_metrics_better = np.greater if self.higher_is_better else np.less

        # 跟之前epoch比而不是跟best比，如果跟best比，避免刚开始训练没多久就停止掉
        improving = previous_metrics is None or is_metrics_better(curr_metrics, previous_metrics)

        self.previous_metrics = curr_metrics
        if self.best_metrics is None or is_metrics_better(curr_metrics, self.best_metrics):
            self.best_metrics = curr_metrics

        if not improving:
            self.patience_cnt -= 1
        else:
            self.patience_cnt = self.patience

        if self.patience_cnt == 0:
            return True

        return False
