
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
	ans = -1
	visited = set()
	fringe = [(0, 1, (0,) * W, ())]
	goal = (E, 0, (0,) * W, ())
	found = False
	while True:
		ans += 1
		new_fringe = []
		# print(fringe)
		for i in fringe:
			# print(' ', i)
			if i in visited:
				continue
			if i == goal:
				found = True
				break
			i0, i1, i2, i3 = i
			i2 = list(i2)
			while i0 < E and i2 == X[i0]:
				i0 += 1
				i1 = 0
			if i0 == E:
				assert i1 == 0
				i2[i3[-1]] -= 1
				new_fringe.append((i0, i1, tuple(i2), i3[:-1]))
			else:
				# print('  ', i0, i1, i2, i3)
				if i1 == 0 and i3:
					i2[i3[-1]] -= 1
					new_fringe.append((i0, i1, tuple(i2), i3[:-1]))
					i2[i3[-1]] += 1
				candid = []
				abort = False
				for index, (j, k) in enumerate(zip(i2, X[i0])):
					if j < k:
						i2[index] += 1
						candid.append((i0, i1, tuple(i2), i3 + (index,)))
						i2[index] -= 1
					elif j > k:
						abort = True
				if not abort:
					new_fringe += candid
		if found:
			break
		visited.update(fringe)
		fringe = new_fringe
	print('Case #%d:' % (test + 1), ans)

