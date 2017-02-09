def compressString(s):
	counter = 0
	output = ''
	i = 0
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			counter += 1
		else:
			output = output + s[i] + str(counter+1)
			counter = 0
	output = output + s[i+1] + str(counter + 1)
	if len(output) > len(s):
		return s
	return output


def main():
	print compressString('aabcccccaaa')
	print compressString('abcdef')
	print compressString('aabcccccaab')

if __name__ == "__main__":
    main()