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
	N = int(input())
	D = list(map(int, input().split()))
	l = [False] * N
	# r = [False] * N
	assert(len(D) == N)
	best = 0
	for index, i in enumerate(D):
		if i >= best:
			l[index] = True
			best = i
	best = 0
	for index, i in reversed(list(enumerate(D))):
		if i >= best:
			l[index] = True
			best = i
	ans = sum(l)
	print('Case #%d:' % (test + 1), ans)

