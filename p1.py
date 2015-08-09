#!/usr/bin/env python
#Author: @nix1947
#Description: Euler p1

#Can done in single line
print sum((x for x in range (0, 1000) if x % 3 == 0 or x % 5 == 0))

#Can be also done in multiple lines
sum = 0
for i in range(1, 1000):
	if i % 5 == 0 or i % 3 == 0:
		sum = sum + i
print sum




