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
	cymk = []
	for i in range(3):
		cymk.append(list(map(int, input().split())))
	m = list(map(min, *cymk))
	ans = []
	cur = 0
	D = 10**6
	for i in m:
		if cur + i < D:
			d = i
		else:
			d = D - cur
		cur += d
		ans.append(d)
	if cur == D:
		print('Case #%d:' % (test + 1), *ans)
	else:
		print('Case #%d:' % (test + 1), 'IMPOSSIBLE')

