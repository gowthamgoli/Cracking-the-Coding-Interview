def rotate(s1,s2):
	concat_s2 = s2+s2
	if s1 not in concat_s2:
		return False
	return True

def main():
	print rotate('waterbottle', 'erbottlewat')
	print rotate('foo', 'bar')

if __name__ == "__main__":
    main()