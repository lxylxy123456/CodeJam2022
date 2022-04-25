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
	N, P = map(int, input().split())
	X = []
	for i in range(N):
		x = list(map(int, input().split()))
		X.append([min(x), max(x)])
	# [end at min, end at max]
	dp = [0, 0]
	# [min, max]
	pos = [0, 0]
	for x in X:
		new_dp = [10**30, 10**30]
		new_pos = x.copy()
		for i in range(2):
			for j in range(2):
				new_dp[1 - j] = min(new_dp[1 - j],
									dp[i] + abs(pos[i] - x[j]) + x[1] - x[0])
		dp = new_dp
		pos = new_pos
		# print(dp, pos, x)
	ans = min(new_dp)
	print('Case #%d:' % (test + 1), ans)

