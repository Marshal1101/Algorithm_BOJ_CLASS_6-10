import sys, math


def LCA(a, b, parent, level, max_level):
    # a를 레벨이 더 높은 정점으로 맞춘다.
    if level[a] < level[b]:
        temp = a
        a = b
        b = temp

    # a의 레벨이 b와 같아질 때까지 a가 올라간다.
    if level[a] != level[b]:
        for i in range(max_level-1, -1, -1):
            if level[parent[a][i]] >= level[b]:
                a = parent[a][i]

    # a, b의 레벨이 같으므로 조상 찾을 때까지 올라간다.
    ret = a
    if a != b:
        for i in range(max_level-1, -1, -1):
            if parent[a][i] != parent[b][i]:
                a = parent[a][i]
                b = parent[b][i]
            ret = parent[a][i]

    return ret



def set_tree(node, p_node, graph, parent, level, max_level):
    parent[node][0] = p_node
    level[node] = level[p_node] + 1
    stack = [node]
    while stack:
        node = stack.pop()
        for adj in graph[node]:
            if adj != parent[node][0]:
                parent[adj][0] = node
                level[adj] = level[node] + 1
                for i in range(1, max_level):
                    parent[adj][i] = parent[parent[adj][i-1]][i-1]
                stack.append(adj)

def main():
    input = sys.stdin.readline
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    max_level = math.ceil(math.log2(N))
    level = [0] * (N+1)
    parent = [[0] * max_level for _ in range(N+1)]
    set_tree(1, 0, graph, parent, level, max_level)

    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        print(LCA(a, b, parent, level, max_level))


if __name__ == '__main__':
    main()