from collections import defaultdict

'''def isOneAway_v1(s1, s2):
	chars = defaultdict(int)
	for c in s1:
		chars[c] += 1
	for c in s2:
		chars[c] -= 1
	numOnes = 0
	numMinusOnes = 0
	for k in chars:
		if chars[k] > 0:
			numOnes += chars[k]
		elif chars[k] < 0:
			numMinusOnes += abs(chars[k])
		if numOnes > 1 or numMinusOnes > 1:
			return False
	return True'''

def checkForReplace(x,y):
	counter = 0
	for i in range(len(x)):
		if x[i] != y[i]:
			counter += 1
			if counter > 1:
				return False
	return True

def checkForDelete(x,y):
	if len(y) == 0:
		return True
	i = 0
	counter = 0
	for j in range(len(x)):
		if i == len(y)-1:
			return True
		if x[j] == y[i]:
			i += 1
		else:
			counter += 1
			if counter > 1:
				return False

def checkForInsert(x,y):
	return checkForDelete(y,x)

def isOneAway_v2(s1, s2):

	len1 = len(s1)
	len2 = len(s2)

	if len1 == len2:
		return checkForReplace(s1, s2)
	elif len2 == len1 - 1:
		return checkForDelete(s1, s2)
	elif len2 == len1 + 1:
		return checkForInsert(s1, s2)
	else:
		return False


def main():
	print isOneAway_v2('pales', 'pale')
	print isOneAway_v2('pale', 'pales')
	print isOneAway_v2('pales', 'ples')
	print isOneAway_v2('pale', 'bale')
	print isOneAway_v2('pale', 'bake')
	print isOneAway_v2('a', 'b')
	print isOneAway_v2('', 'a')
	print isOneAway_v2('palks', 'pal')
	print isOneAway_v2('pal', 'palks')
	print isOneAway_v2('pale', 'pse')
	print isOneAway_v2('paleabc', 'pleabc')
if __name__ == "__main__":
    main()
