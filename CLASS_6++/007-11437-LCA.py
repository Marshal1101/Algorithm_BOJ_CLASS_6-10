import sys


def main():
    input = sys.stdin.readline
    N = int(input())
    graph = [[] for _ in range(N+1)]
    for _ in range(N-1):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    level = [0] * (N+1)
    parent = [0] * (N+1)
    set_tree(1, 0, graph, parent, level)

    M = int(input())
    for _ in range(M):
        a, b = map(int, input().split())
        print(LCA(a, b, parent, level))


def LCA(a, b, parent, level):
    # a를 레벨이 더 높은 정점으로 맞춘다.
    if level[a] < level[b]:
        temp = a
        a = b
        b = temp

    # a의 레벨이 b와 같아질 때까지 a가 올라간다.
    while level[a] != level[b]:
        a = parent[a]

    # a, b의 정점이 같아질 때까지 올라간다.
    while a != b:
        a = parent[a]
        b = parent[b]

    return a


def set_tree(node, p_node, graph, parent, level):
    parent[node] = p_node
    level[node] = level[p_node] + 1
    stack = [node]
    while stack:
        node = stack.pop()
        for adj in graph[node]:
            if adj != parent[node]:
                parent[adj] = node
                level[adj] = level[node] + 1
                stack.append(adj)


if __name__ == '__main__':
    main()