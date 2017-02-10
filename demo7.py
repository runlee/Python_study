#!/usr/bin/env python
# -*- coding: utf-8 -*-


num_arr = (1,2,3,4,5,6,7,8,9,10);
sum = 0;

for num in num_arr:
	sum += num;
print sum;



i = 99;
i_sum = 0;

while i >=1:
	i_sum += i;
	i = i-2;
print i_sum;


print "*************我是可爱的分割线！！***************";

birth = raw_input("出生日期：");

birth = int(birth);
if birth > 2000 :
	print "00后";
elif birth < 2000 and birth >= 1990 :
	print "90后";
else :
	print "呵呵";
