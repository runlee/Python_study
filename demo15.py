#!/usr/bin/env python
# -*- coding: utf-8 -*-

## 列表学习
import os;


print [x * x for x in range(1,10)];



print [m + n for m in 'ABC'  for n in 'XYZ'];


print [d for d in os.listdir('..')];



d = {'a':1 , 'b': 2 , 'c' : 3};

for x,val in d.iteritems():
	print x , '=' , val;



L = ['HELLO' , 'NAME' , 'AGE'];

print [s.lower() for s in L];

print L;

