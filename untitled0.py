#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 11:03:24 2018

@author: zhouzhuofei
"""


n=int(input())


def myfunc(n):
    assert n>=0
    if n<2:
        return 1;
    else:
        return n*myfunc(n-1);





print(myfunc(n))
