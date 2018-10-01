def triangleType(s1,s2,s3):
	if (s1==s2 and s1==s3):
		return 3
	elif((s1==s2 and s1!=s3) or (s1==s3 and s1!=s2) or (s2==s3 and s2!=s1)):
		return 2
	else:
		return 1