# -*-coding:utf-8 -*-

"""
@Author:    chaoli
@DateTime:  2021/12/26 3:39 下午
@Contact:   qizuma@126.com
@Version:   1.0
@File:      datasets.py
@Desc:
"""

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda, Compose
import matplotlib.pyplot as plt


class TabularDataset(TensorDataset):
    """根据输入是Dict获取Dataset，通常用于小数据集，可以加载到内存。不包含数据preprocess和load to memory的过程

    Args:
        data_dict(dict): 输入数据字典。字典的keys必须是features和label。
    """
    def __init__(self, data_dict):
        self.data_dict = data_dict.copy()
        super().__init__(*data_dict.values())

    def __getitem__(self, index):
        pass

    def __len__(self):
        pass
