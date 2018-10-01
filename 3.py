def validSides(a,b,c):
	if ((a+b>c or a+c>b or b+c>a)):
		return true
	else:
		return false
