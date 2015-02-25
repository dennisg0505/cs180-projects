#!/usr/bin/env python

import sys

input = sys.stdin.read()
inputArray = eval(input)

area = 0

for i in range(len(inputArray)):
	area += (inputArray[i + 2] - inputArray[i]) * inputArray[i + 1]
	print area
	i += 1
