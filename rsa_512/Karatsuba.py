def Karatsuba(x,y):
	if len(str(x)) == 1 or len(str(y)) ==1:
		return x*y
	else:
		n = max(len(str(x)), len(str(y)))
		n2 = n//2
		a = x//(10**n2)
		b = x%(10**n2)
		c = y//(10**n2)
		d = y%(10**n2)
		ac = Karatsuba(a,c)
		bd = Karatsuba(b,d)
		kara = Karatsuba(a+b,c+d) -ac -bd

		return ac*10**(2*n2) + kara*10**n2 + bd
