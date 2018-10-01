def second_max(a,b,c,d):
    x=max(a,b,c,d)
	if x==a:
		y=max(b,c,d)
		return y
	elif x==b:
		y=max(a,c,d)
		return y
	elif x==c:
		y=max(a,b,d)
		return y
	else:
		y=max(a,b,c)
		return y