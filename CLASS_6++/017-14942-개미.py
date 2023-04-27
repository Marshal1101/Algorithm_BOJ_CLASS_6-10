import sys
import math
from collections import defaultdict


def LCA(a, energy, max_level, lca, dist):

    # a 위치, 에너지
    ea = energy[a]
    # dist 에서 에너지만큼 소화 가능한 노드로 점프

    for i in range(max_level-1, -1, -1):
        if ea >= dist[a][lca[a][i]]:
            ea -= dist[a][lca[a][i]]
            a = lca[a][i]

    return a if a > 0 else 1



def dfs(node, p_node, graph, parent, level, max_level, lca, dist):
    parent[node] = p_node
    level[node] = level[p_node] + 1
    lca[node][0] = p_node
    stack = [node]
    while stack:
        node = stack.pop()
        for v in graph[node]:
            if v != parent[node]:
                parent[v] = node
                level[v] = level[node] + 1
                lca[v][0] = node
                for i in range(1, max_level):
                    lca[v][i] = lca[lca[v][i-1]][i-1]
                    dist[lca[v][i]][v] += dist[lca[v][i-1]][v] + dist[lca[v][i-1]][lca[v][i]]
                    dist[v][lca[v][i]] += dist[lca[v][i-1]][v] + dist[lca[v][i-1]][lca[v][i]]
                    if lca[v][i] == 0:
                        break
                stack.append(v)


def printl(arr, name=""):
    print(name, arr)

def printb(arr, name=""):
    print(name)
    for b in arr:
        print(b)

def main():
    input = sys.stdin.readline
    N = int(input())
    energy = [0] + [int(input()) for _ in range(N)]
    graph = [[] for _ in range(N+1)]
    dist = [defaultdict(int) for _ in range(N+1)]
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        dist[u][v] = w
        dist[v][u] = w
        graph[u].append(v)
        graph[v].append(u)

    parent = [0] * (N+1)
    level = [0] * (N+1)
    max_level = math.ceil(math.log2(N))
    lca = [[0] * max_level for _ in range(N+1)]

    dfs(1, 0, graph, parent, level, max_level, lca, dist)

    # printb(dist, "dist")
    # printl(parent, "parent")
    # printl(level, "level")
    # printb(lca, "lca")

    for i in range(1, N+1):
        print(LCA(i,energy, max_level, lca, dist))


if __name__ == '__main__':
    main()