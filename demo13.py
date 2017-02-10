#!/usr/bin/env python
# -*- coding: utf-8 -*-


## 切片学习

L = [];
n = 1;

while n <= 99:
	L.append(n);
	n = n + 2;

print L;

print "list前3位";

print L[0:3];

print L[-1:];

print len(L);

print L[48:50];

print L[-1:];

print L[:10:2];
