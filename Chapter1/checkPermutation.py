from collections import defaultdict
def checkPermutation(s1, s2):

	if len(s1) != len(s2):
		return False

	charCount_s1 = defaultdict(int)

	for c in s1:
		charCount_s1[c] += 1

	for c in s2:
		charCount_s1[c] -= 1

	for k in charCount_s1:
		if charCount_s1[k] != 0:
			return False

	return True

def main():
	s1 = "abcde"
	s2 = "bcdea"
	print checkPermutation(s1, s2)

	s1 = "abcde"
	s2 = "bacdb"
	print checkPermutation(s1, s2)

if __name__ == '__main__':
	main()