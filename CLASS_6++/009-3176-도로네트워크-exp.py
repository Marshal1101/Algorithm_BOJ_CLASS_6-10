# https://www.acmicpc.net/source/45409466

from sys import stdin
from collections import deque as dq


def solution(graph: dict[int, list[tuple[int]]],
             queries: list[list[int]], n: int, k: int) -> str:
    def fill():
        q = dq([(1, 0, 0)])
        while q:
            src, parent, depth = q.popleft()
            p[0][src], d[src] = parent, depth
            for dest, dist in graph[src]:
                if dest == parent:
                    continue
                q.append((dest, src, depth + 1))
                min_[0][dest] = max_[0][dest] = dist
        for r in range(1, len(p)):
            for c in range(1, n):
                p[r][c] = p[r - 1][p[r - 1][c]]
                min_[r][c] = min(min_[r - 1][c], min_[r - 1][p[r - 1][c]])
                max_[r][c] = max(max_[r - 1][c], max_[r - 1][p[r - 1][c]])

    def get_dist(fr, to) -> str:
        if d[to] < d[fr]:
            to, fr = fr, to
        min_d, max_d = min_[0][to], max_[0][to]
        diff, i = d[to] - d[fr], 0
        while diff:
            if diff & 1:
                min_d, max_d = min(min_d, min_[i][to]), max(max_d, max_[i][to])
                to = p[i][to]
            diff //= 2
            i += 1
        if fr == to:
            return f'{min_d} {max_d}'
        for i in range(len(p) - 1, -1, -1):
            if p[i][fr] != p[i][to]:
                min_d = min(min_d, min_[i][fr], min_[i][to])
                max_d = max(max_d, max_[i][fr], max_[i][to])
                fr, to = p[i][fr], p[i][to]
        min_d = min(min_d, min_[0][fr], min_[0][to])
        max_d = max(max_d, max_[0][fr], max_[0][to])
        return f'{min_d} {max_d}'

    p, d = [[0] * n for _ in range(len(bin(n - 1)[2:]))], [0] * n
    min_ = [[0] * n for _ in range(len(bin(n - 1)[2:]))]
    max_ = [[0] * n for _ in range(len(bin(n - 1)[2:]))]
    fill()
    return '\n'.join([get_dist(fr, to) for fr, to in queries])


def reader():
    read = stdin.readline
    n = int(read().rstrip())
    g = {}
    for _ in range(n - 1):
        a, b, dist = map(int, read().split())
        g.setdefault(a, []).append((b, dist))
        g.setdefault(b, []).append((a, dist))
    k = int(read().rstrip())
    q = [list(map(int, read().split())) for _ in range(k)]
    print(solution(g, q, n + 1, k))


if __name__ == '__main__':
    reader()