from collections import defaultdict
def zeroMatrix(P):
	m = len(P)
	n = len(P[0])
	rows = defaultdict(int)
	cols = defaultdict(int)
	for i in range(m):
		for j in range(n):
			if P[i][j] == 0:
				rows[i] = 1
				cols[j] = 1
	for k in rows:
		for i in range(n):
			P[k][i] = 0

	for k in cols:
		for i in range(m):
			P[i][k] = 0
	print P

def main():
	M = [[1, 2, 0, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
	zeroMatrix(M)

	M = [[1, 2, 3, 4, 0], [6, 0, 8, 9, 10], [11, 12, 13, 14, 15], [16, 0, 18, 19, 20], [21, 22, 23, 24, 25]]
	zeroMatrix(M)

if __name__ == "__main__":
    main()