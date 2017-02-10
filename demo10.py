#!/usr/bin/env python
# -*- coding: utf-8 -*-


#计算平方
def power(x):
	return x * x;

print power(3);


#计算n次方
def powers(x , n = 1):
	s = 1;
	while n > 0:
	 	n = n - 1;
	 	s = s * x;
	return s;
print powers(2 , 10);


def classmate(name , grade , age = 20 , city = 'gz'):
	print "name :" , name;
	print "grade:" , grade;
	print "age  :" , age;
	print "city :" , city;

classmate('王五' , '99' , city = 'beijing');

## *********************************************************函数学习笔记 start*******************************************************
##
## python函数的传参和php函数的传参基本一样，但是还有不一样的地方，python的有多个默认参数时，如果写上参数的名称再赋值，则值传给了此参数名称
## 例：test(x , y , m = 1, k = 'test')      test(1 , 2 , k = 'name')    k的则被赋值为name，而m的值还是1，没有变

## *********************************************************学习笔记 end*******************************************************


def add_end(L = []):
	L.append('END');
	return L;

print add_end();
print add_end();


def add_ends( L = None):
	if L is None:
		L = [];
	L.append('END');
	return L;
print add_ends();
print add_ends();




