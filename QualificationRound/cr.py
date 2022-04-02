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
from operator import itemgetter

T = int(input())
for test in range(T):
	N = int(input())
	F = [0] + list(map(int, input().split()))
	P = [0] + list(map(int, input().split()))
	children = [[]]	# (smallest, total)
	for i in range(N):
		children.append([])
	ans = None
	for i in range(N, -1, -1):
		c = children[i]
		f = F[i]
		if c:
			small = min(map(itemgetter(0), c))
			tot = sum(map(itemgetter(1), c))
			if small < f:
				tot += f - small
				small = f
		else:
			small = tot = f
		if i == 0:
			ans = tot
		else:
			children[P[i]].append((small, tot))
	print('Case #%d:' % (test + 1), ans)

