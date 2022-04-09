try:
	import os, sys
	stdin = sys.stdin
	if len(sys.argv) > 1:
		stdin = open(sys.argv[1])
	else:
		# stdin = open('s.txt')
		stdin = open(os.path.splitext(__file__)[0] + '.txt')
	input = lambda: stdin.readline()[:-1]
except Exception:
	pass

# import math, sys
# sys.setrecursionlimit(100000000)
# from collections import defaultdict
# A = list(map(int, input().split()))

T = int(input())
for test in range(T):
	S = input()
	nxt = [None] * len(S)
	nxt[-1] = 'A'
	for i in range(len(S) - 2, -1, -1):
		if S[i] == S[i + 1]:
			nxt[i] = nxt[i + 1]
		else:
			nxt[i] = S[i + 1]
	ret = []
	for i, j in zip(S, nxt):
		if i < j:
			ret.append(i * 2)
		else:
			ret.append(i)
	ans = ''.join(ret)
	print('Case #%d:' % (test + 1), ans)

