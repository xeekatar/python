numbers = [] 

for i in range(10):
	x = int(input(str(i+1)+': '))
	numbers.append(x)

biggestodd = -1

for i in numbers:
	if i % 2 == 0:
		pass
	elif i > biggestodd:
		biggestodd = i

print (biggestodd,'is the largest number')