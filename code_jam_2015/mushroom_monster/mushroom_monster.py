#!/usr/bin/python


def a(lst):
	diflst=[0 if (i-j < 0) else i-j for i, j in zip(lst[:-1], lst[1:])]
	return reduce(lambda x,y: x+y, diflst, 0)

def b(lst):
        diflst=[0 if (i-j < 0) else i-j for i, j in zip(lst[:-1], lst[1:])]
	maxval = max(diflst)
	mushrooms_eaten = map(lambda x: min(x,maxval) ,lst[:-1])
        return reduce(lambda x,y: x+y, mushrooms_eaten, 0)

with open('input.txt') as input:
	input.readline()	#discard line
	input.readline()	#discard line
	line=input.readline()
	cnt=1
	while line:
		lst =  map(lambda x: int(x),line.strip().split(' '))
		resA = a(lst)
		resB = b(lst)
		print ('Case #%d: %d %d' % (cnt,resA,resB))
		cnt+=1
		input.readline() 	#discard line
		line=input.readline()
		

