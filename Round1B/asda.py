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

import random
from collections import Counter

n1s = []
for i in range(256):
	n1s.append(bin(i)[2:].count('1'))

s1n = []
for i in range(9):
	s1n.append([])
for index, i in enumerate(n1s):
	s1n[i].append(index)

def rot(x, r):
	a = x << r
	a |= a >> 8
	a &= 0xff
	return a

T = int(input())
cnts = []
for test in range(T):
	poss = list(range(1, 256))
	nb = None
	for cnt in range(1000):
		if nb is None:
			x = 0b01010101
		elif nb == 8:
			x = 0b11111111
		elif nb == 7:
			x = rot(0b11111110, random.randrange(8))
		elif nb == 1:
			x = rot(0b10000000, random.randrange(8))
		else:
#			vote = Counter()
#			for i in poss:
#				for j in range(8):
#					vote[rot(i ^ 0x00, j)] += 1
#					vote[rot(i ^ 0xaa, j)] += 1
#					vote[rot(i ^ 0xff, j)] += 1
#			mc = vote.most_common(3)
#			x = random.randrange(1, 255)
#			try:
#				if mc[0][1] > mc[2][1] * 2 + 10:
#					x = mc[0][0]
#			except Exception:
#				x = mc[0][0]
			x = random.choice(s1n[nb])
		# print(x, len(poss), nb, file=sys.stderr)
		print(bin(x + 256)[3:])
		a = int(input())
		if a == 0:
			# print(cnt, file=sys.stderr)
			break
		elif a == -1:
			exit()
		else:
			nb = a
#			new_poss = set()
#			for j in range(8):
#				xx = rot(x, j)
#				for i in poss:
#					ixx = i ^ xx
#					if n1s[ixx] == nb:
#						new_poss.add(ixx)
#			poss = new_poss
	cnts.append(cnt)
#	if test == 99:
#		print(sorted(cnts), file=sys.stderr)

