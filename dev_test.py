N = int(input('N: '))
S = lambda i, K, n: 1 + sum(0 if len({x & k for k in K} - K) - 1 else S(x + 1, K | {x | k for k in K}, n) for x in range(i, 2**n))
print('Preorders:', [S(1, {0, 2**n - 1}, n) for n in range(0, N+1)])