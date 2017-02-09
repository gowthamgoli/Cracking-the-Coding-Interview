def hasUniqueChars_v1(s):
	chars = {}
	for c in s:
		if c not in chars:
			chars[c] = 1
		else:
			return False
	return True 

def hasUniqueChars_v2(s):
	asciiNum = 128*[0]
	for c in s:
		if asciiNum[ord(c)] == 0:
			asciiNum[ord(c)] = 1
		else:
			return False
	return True


def main():
	s1 = "abcde"
	s2 = "aabbc"
	s3 = "  "
	
	print hasUniqueChars_v1(s1)
	print hasUniqueChars_v1(s2)
	print hasUniqueChars_v1(s3)

	print hasUniqueChars_v2(s1)
	print hasUniqueChars_v2(s2)
	print hasUniqueChars_v2(s3)

if __name__ == '__main__':
	main()
