def rotate(M):
	n = len(M)
	numPhases = n/2

	for p in range(numPhases):
		for i in range(p, n-p-1):
			temp = M[p][i]
			M[p][i] = M[n-i-1][p]
			M[n-i-1][p] = M[n-p-1][n-i-1]
			M[n-p-1][n-i-1] = M[i][n-p-1]
			M[i][n-p-1] = temp

	print M

def main():
	M = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
	rotate(M)

if __name__ == "__main__":
    main()