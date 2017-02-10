#!/usr/bin/env python
# -*- coding: utf-8 -*-


# map/reduce学习


def test(x):
	return x * x;


num_list = [1,2,3,4,5,6,7,8,9];

print map(test , num_list);



L = [];

rand_num = range(1,10);
# print rand_num;

for x in rand_num:
	L.append(test(x));

print L;


# 将list里面的值转化成字符串

print map(str , rand_num);

# 将list里面的值转化成float类型
print map(float , rand_num);



def add(x , y):
	return x * 10 + y;


print reduce(add , rand_num);




def fn(x, y):
	return x * 10 + y;

def char2num(s):
	print s;
	return {'0': 0 ,'1': 1 , '2': 2 , '3': 3 ,'4': 4 , '5': 5 , '6': 6 , '7': 7 , '8': 8 , '9': 9}[s];

print reduce(fn  , map(char2num , '13579'));




# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']。


name_list = ['adam', 'LISA', 'barT'];

def practice(string):
	lenth  = len(string);
	last   = string[1 : lenth]; 
	string = string[0].upper() + last.lower();
	return string;

print map(practice , name_list);



print '********************************************************';
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积。

def prod(numbers):
	def take_sets(x ,y):
		return x * y;

	return reduce(take_sets , numbers);

numbers = [1 , 2 , 3 , 4 , 5];

print prod(numbers);

print sum(numbers);












