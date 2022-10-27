import sys

input = sys.stdin.readline
flush = sys.stdout.flush


def build():
    for i in reversed(range(1, n)):
        segm[i] = min(segm[2*i], segm[2*i + 1])
        segM[i] = max(segM[2*i], segM[2*i + 1])
    return

def query(l, r):
    l += n
    r += n
    m, M = 10**9 + 1, 0
    while l < r:
        if l & 1:
            if segm[l] < m:
                m = segm[l]
            if segM[l] > M:
                M = segM[l]
            l += 1
        if r & 1:
            r -= 1
            if segm[r] < m:
                m = segm[r]
            if segM[r] > M:
                M = segM[r]
        l >>= 1
        r >>= 1
    return m, M

n, m = map(int, input().split())
segm = [0] * n
segM = [0] * n
for _ in range(n):
    x = int(input())
    segm.append(x)
    segM.append(x)

build()
for _ in range(m):
    a, b = map(int, input().split())
    print(*query(a - 1, b))
