#!/usr/bin/env python
# -*- coding: utf-8 -*-


# sorted学习

num_list = [33,7634,22,332213123,433,11223213,1212];

print sorted(num_list);


def desc(x,y):
	if x > y:
		return -1;
	if x < y:
		return 1;
	return 0;
print sorted(num_list , desc);


letter_list = ['ddd' , 'Zdsdsd' , 'AAA' , 'aad' , "hhMk"];

print sorted(letter_list);

def  letter_desc(s1 , s2):
	u1 = s1.upper();
	u2 = s2.upper();

	if u1 < u2:
		return -1;
	if u1 > u2:
		return 1;
	return 0;

print sorted(letter_list , letter_desc);