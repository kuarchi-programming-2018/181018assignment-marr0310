#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 18:32:09 2018

@author: kinoshitamao
"""

# coding: utf-8
# 学生メソッドを作る

class Gakusei:
    def __init__(self, kokugo, sansu):
        self.kokugo = kokugo
        self.sansu  = sansu

    # この下に、合計得点を戻り値として返すsumメソッドを記述する
    def sum(self):
        return self.kokugo + self.sansu

yamada = Gakusei(70, 43)
print("合計は" + str(yamada.sum()) + "点です")