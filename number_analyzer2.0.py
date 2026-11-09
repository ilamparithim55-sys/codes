n = int(input ("enter a number :"))
def analyzer(n):
	b = 0
	fv = []
	ft = []
	for a in range (1,n+1):
		if a % 3 == 0:
			b += a
		if a % 5 == 0 and a % 3 != 0:
			fv.append (a)
		if a % 3 == 0 and a % 5 == 0 :
			ft.append(a)
	return b,fv,ft
b,fv,ft = analyzer(n)
print ("Numbers divisible by 3:" ,b)
print ("Numbers divisible by 5:" ,fv)
print ("Numbers divisible by 3 and 5:" ,ft)
