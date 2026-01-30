import time

L = list(range(10_000_00))   # 1 million
T = tuple(range(10_000_00))

start = time.time()
for i in L:
    i * 5
print('list time:', time.time() - start)

start = time.time()
for i in T:
    i * 5
print('tuple time:', time.time() - start)
