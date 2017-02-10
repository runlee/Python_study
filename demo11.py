#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calc(numbers):
	sum = 0;
	for n in numbers :
		sum = sum + n * n;
	return sum;
print calc([1,3,5,7]);


def calc2(*numbers):
	sum = 0;
	for n in numbers:
		sum = sum + n * n;
	return sum;

print calc2(1 , 3 , 5 , 7);

num_list = [1 , 3 , 5 , 7];

print calc2(*num_list);


def calc3(name , age , **other):
	print name , age , other;

print calc3('lisi' , 20 );



##  学习心得：python的函数参数非常灵活，参数可以根据*来给参数定义类型，并且传参灵活多变；缺点：代码量多了，容易记错，参数没有赋值给想赋值的参数