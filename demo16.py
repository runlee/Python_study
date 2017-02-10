#!/usr/bin/env python
# -*- coding: utf-8 -*-




L = (x * x for x in range(10));


# for i in L:
# 	print i;



# print L.next();



def fib(max):
	n,a,b = 0,0,1;
	while n < max:
		print b;
		a , b = b , a+b;
		n = n + 1;

print fib(6);



f = abs;

def add(a , b, f):
	return f(a) + f(b);


print add(-10 , -10 , f);
