import math, sys
# sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))

A = []
A0 = []
A1 = []
A2 = []
for i in range(30):
	A.append(2**i)
	A0.append(2**i)
for i in range(6):
	A.append(5 * 10**8 + i)
	A1.append(5 * 10**8 + i)
while len(A) < 100:
	A2.append(4 * 10**7 + len(A))
	A.append(4 * 10**7 + len(A))
# print(A, file=sys.stderr)

T = int(input())
for test in range(T):
	N = int(input())
	assert(N == 100)
	print(*A)
	B = list(map(int, input().split()))

	target = sum(B + A)
	assert target % 2 == 0
	target //= 2
	
	g1 = []
	g2 = []
	g1s = 0
	g2s = 0
	for i in sorted(B + A2, reverse=True):
		if g1s < g2s:
			g1.append(i)
			g1s += i
		else:
			g2.append(i)
			g2s += i
	# print(len(B), len(g1), len(g2), file=sys.stderr)
	if g1s > g2s:
		g1, g2 = g2, g1
		g1s, g2s = g2s, g1s
	assert target > g1s
	a1 = A1.copy()
	while target > g1s + 5 * 10**8 + 20:
		i = a1.pop()
		g1.append(i)
		g1s += i
	d = target - g1s
	for i in range(30):
		if d & (1 << i):
			g1.append(2**i)
			g1s += 2**i
	assert target == g1s
	assert sum(g1) == g1s
	# print(*B, file=sys.stderr)
	# print(*g1, file=sys.stderr)
	print(*g1)

