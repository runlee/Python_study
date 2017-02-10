#!/usr/bin/env python
# -*- coding: utf-8 -*-


# filter学习


def is_old(num):
	return num % 2 == 1;

number_list = [1 , 2 , 3 , 4 , 5];
print filter(is_old , number_list);



# 请尝试用filter()删除1~100的素数。


