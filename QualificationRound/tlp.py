import random, sys
T = int(input())
for test in range(T):
	N, K = map(int, input().split())
	visited = set()
	cur_sum = 0
	while True:
		r, p = map(int, input().split())
		visited.add(r)
		cur_sum += p
		if len(visited) == min(K + 1, N):
			break
		n = None
		while n is None or n in visited:
			n = random.randint(1, N)
		print('T', n)
	# print(len(visited), K, N, file=sys.stderr)
	assert len(visited) == K + 1 or len(visited) == N
	print('E', round(cur_sum * N / len(visited) / 2))

