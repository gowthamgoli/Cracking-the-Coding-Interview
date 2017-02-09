def makeURL(s, length):
	list_s = list(s)
	totlen = len(s)
	j = totlen-1
	for i in reversed(range(length)):
		if list_s[i] != " ":
			list_s[j] = list_s[i]
			j -= 1
		else:
			list_s[j-2:j+1] = '%20'
			j -= 3
	return "".join(list_s)

def main():
	print makeURL("Mr John Smith    ", 13)
	print makeURL("much ado about nothing      ", 22)

if __name__ == '__main__':
	main()
