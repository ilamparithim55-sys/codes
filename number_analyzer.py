n = int(input ("enter a number :"))
def analyzer(n):
	b = 0
	c = 0
	for a in range (1,n+1):
		if a % 3 == 0:
			b += a
		if a % 3 != 0:
			c += a
	return b-c
print (analyzer(n))
