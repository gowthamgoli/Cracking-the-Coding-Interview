from collections import defaultdict
def isPalinPerm(s):
	s = s.lower()
	chars = defaultdict(int)
	for c in s:
		if c != ' ':
			chars[c] += 1
	oddCounter = 0
	for k in chars:
		if chars[k]%2 != 0:
			oddCounter += 1
			if oddCounter > 1:
				return False
	return True


def main():
	print isPalinPerm("Tact Coa")
	print isPalinPerm("Taca Coa")
	print isPalinPerm('no x in nixon')
	print isPalinPerm("So patient a nurse to nurse a patient so")
	print isPalinPerm('Able was I ere I saw Elba')

if __name__ == '__main__':
	main()
