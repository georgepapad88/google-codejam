import math

def foo(x,y):
	x.append(y if len(x)==0 else x[len(x)-1]+y)
	return x

def baz(x,lst):
	if(lst.len==0):
		return []
	else:
		res=math.ceil(x*)
		x=


with open('input.txt') as file:
	file.readline()
	line1 = file.readline()
	line2 = file.readline()
	while line1:
		turn=int(line1.strip().split()[1])
		lst = map(lambda x: float(x),line2.strip().split())
		lst2= map(lambda x: 1/x,lst)
		lst2.reverse()
		list3 = reduce(foo,lst2,[])
		lst4 =  [b/a for a, b in zip(lst3, lst2)]
		lst5 = reduce(lambda x,y: ,lst4,turn) 
		line1 = file.readline()
		line2 = file.readline()

