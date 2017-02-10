#!/usr/bin/env python
# -*- coding: utf-8 -*-

#递归学习

def fact(n):
	if n == 1:
		return n;
	return n * fact(n - 1);

print fact(5);



def fact2(n):
	return fact_item(n , 1);

def fact_item(num , product):
	if num == 1:
		return product;
	return fact_item(num - 1 , num * product);


print fact2(100);