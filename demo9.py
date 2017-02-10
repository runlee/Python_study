#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math;

def index(x):
	if x >= 0:
		return x;
	else:
		return -x;

print index(10);


def mydef(x):
	pass;

print mydef(10);


def test(x):
	if not isinstance(x , (int,float)):
		raise TypeError("类型错误");
	if x < 10:
		return x;
	elif x > 10 and x < 20:
		name = '李四';
		return name;
	else:
		return '王五';

print test(14);


def move(x , y ,step , angle = 0):
	nx = x + step * math.cos(angle);
	ny = y - step * math.sin(angle);
	return nx,ny;

x,y = move(100 , 100 , 60 ,math.pi/6);

print x,y;


r = move(100 , 100 , 60 ,math.pi/6);
print r;
