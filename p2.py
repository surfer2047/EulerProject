#!/usr/bin/env python
#Author: nix@1947
#Description: P2
count = 0
sum = 0
a = 0
b = 1
check = True
while check:
	c = a + b
	if c >= 4000000:
		check = False
	if c % 2 == 0:
		sum = sum + c
	a = b
	b = c
print sum
