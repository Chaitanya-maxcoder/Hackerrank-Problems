import sys

t = int(sys.stdin.readline())

for a0 in range(t):
    m = 0
    n = int(sys.stdin.readline())
    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            m = m + i
    sys.stdout.write(str(m) + "\n")

