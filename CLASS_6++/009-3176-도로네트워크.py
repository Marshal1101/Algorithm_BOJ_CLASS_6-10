import sys, math
from collections import defaultdict


def LCA(a, b, parent, level, max_level):
    max_d = 0
    min_d = 1000001
    # a를 레벨이 더 높은 정점으로 맞춘다.
    if level[a] < level[b]:
        temp = a
        a = b
        b = temp

    # a의 레벨이 b와 같아질 때까지 a가 올라가면서 최대 최소.
    if level[a] != level[b]:
        for i in range(max_level-1, -1, -1):
            if level[parent[a][i][0]] >= level[b]:
                if parent[a][i][1] < min_d:
                    min_d = parent[a][i][1]
                if parent[a][i][2] > max_d:
                    max_d = parent[a][i][2]
                a = parent[a][i][0]

    # a, b의 레벨이 같으므로 조상 찾을 때까지 루트에서 내려가면서 최대 최소.
    if a != b:
        for i in range(max_level-1, -1, -1):
            if parent[a][i][0] != parent[b][i][0]:
                if parent[a][i][1] < min_d:
                    min_d = parent[a][i][1]
                if parent[a][i][2] > max_d:
                    max_d = parent[a][i][2]
                if parent[b][i][1] < min_d:
                    min_d = parent[b][i][1]
                if parent[b][i][2] > max_d:
                    max_d = parent[b][i][2]               
                a = parent[a][i][0]
                b = parent[b][i][0]

        if parent[a][i][1] < min_d:
            min_d = parent[a][i][1]
        if parent[a][i][2] > max_d:
            max_d = parent[a][i][2]
        if parent[b][i][1] < min_d:
            min_d = parent[b][i][1]
        if parent[b][i][2] > max_d:
            max_d = parent[b][i][2]

    return min_d, max_d


def set_tree(node, p_node, graph, parent, level, edge, max_level):
    parent[node][0][0] = p_node
    level[node] = level[p_node] + 1
    stack = [node]
    while stack:
        node = stack.pop()
        for adj in graph[node]:
            if adj != parent[node][0][0]:
                parent[adj][0][0] = node
                level[adj] = level[node] + 1
                parent[adj][0][1] = edge[node][adj] if edge[node][adj] > 0 else 1000001
                parent[adj][0][2] = edge[node][adj] if edge[node][adj] > 0 else 0
                for i in range(1, max_level):
                    parent[adj][i][0] = parent[parent[adj][i-1][0]][i-1][0]
                    parent[adj][i][1] = min(parent[adj][i][1], parent[adj][i-1][1], parent[parent[adj][i-1][0]][i-1][1])
                    parent[adj][i][2] = max(parent[adj][i][2], parent[adj][i-1][2], parent[parent[adj][i-1][0]][i-1][2])
                stack.append(adj)


def main():
    input = sys.stdin.readline
    N = int(input())
    graph = [[] for _ in range(N+1)]
    edge = [defaultdict(int) for _ in range(N+1)]
    for _ in range(N-1):
        a, b, c = map(int, input().split())
        edge[a][b] = edge[b][a] = c
        graph[a].append(b)
        graph[b].append(a)

    max_level = math.ceil(math.log2(N))
    level = [0] * (N+1)
    parent = [[[0, 1000001, 0] for _ in range(max_level)] for _ in range(N+1)]

    set_tree(1, 0, graph, parent, level, edge, max_level)
    
    M = int(input())
    for _ in range(M):
        c1, c2 = map(int, input().split())
        print(*LCA(c1, c2, parent, level, max_level))



if __name__ == '__main__':
    main()