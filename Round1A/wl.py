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

def compute(a, b):
	# a = [1, 2, 3]
	# b = [3, 2, 1]
	# ret = [1, 2, 1], [2, 0, 0], 4
	ret0 = []
	ret1 = []
	ret2 = 0
	for i, j in zip(a, b):
		mij = min(i, j)
		ret0.append(mij)
		ret1.append(j - mij)
		ret2 += abs(i - j)
	return ret0, ret1, ret2

T = int(input())
for test in range(T):
	E, W = map(int, input().split())
	X = []
	for i in range(E):
		X.append(list(map(int, input().split())))
	ans = 0
	stack = [[0] * W]
	stack_sum = [0] * W
	for x in X:
		while True:
			new_sum = []
			for i, j in zip(stack[-1], stack_sum):
				new_sum.append(j - i)
			if any(map(lambda x, y: x < y, x, new_sum)):
				stack_sum = new_sum
				ans += sum(stack.pop())
			else:
				break
		assert stack
		print(stack)
		xx = []
		s1 = stack[-1]
		for i, j, k in zip(x, s1, stack_sum):
			xx.append(i - (k - j))
		c0, c1, c2 = compute(s1, xx)
		ans += c2
		p0 = stack.pop()
		stack.append(c0)
		stack.append(c1)
		for index, (i, j, k) in enumerate(zip(p0, c0, c1)):
			stack_sum[index] += j + k - i
		print(x, stack, stack_sum, '|', c0, c1, c2, '|', s1, xx)
	ans += sum(stack_sum)
	print('Case #%d:' % (test + 1), ans)

