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
	R, C = map(int, input().split())
	ans = R, C
	print('Case #%d:' % (test + 1))
	print('..+' + '-+' * (C - 1))
	print('..|' + '.|' * (C - 1))
	print('+' + '-+' * C)
	for i in range(R - 1):
		print('|' + '.|' * C)
		print('+' + '-+' * C)

