n = int(input ("enter a number :"))
def analyzer(n):
	e = 0
	b_li = []
	t_li = []
	nb_li = []
	for a in range (1,n+1):
		if a % 2 == 0:
			e += a
		if a % 2 == 0 and a % 3 == 0:
			b_li.append(a)
		elif a % 2 != 0 and a % 3 != 0:
			nb_li.append(a)
		if a % 3 == 0:
			t_li.append(a)
	return e,b_li,t_li,nb_li
e,b_li,t_li,nb_li = analyzer(n)
print ("Sum of even numbers :",e)
print ("Numbers divisible by 2 and 3:",b_li)
print ("Numbers divisible by 3:",t_li)
print ("Numbers cannot divisible by 2 and 3:",nb_li)
