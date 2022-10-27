import sys

"""start: 시작 인덱스, end: 끝 인덱스, node: 해당 노드, arr: 배열, tree: 누적값 트리"""
def init(arr, start, end, node, tree):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start + end) // 2
    tree[node] += init(arr, start, mid, node * 2, tree)
    tree[node] += init(arr, mid + 1, end, node * 2 + 1, tree)
    return tree[node]

"""left, right: 구간 합을 구하고자 하는 범위"""
def cumulation(start, end, node, left, right, tree):
    if left > end or right < start: return 0
    if left <= start and end <= right: return tree[node]

    mid = (start + end) // 2
    ret = 0
    ret += cumulation(start, mid, node * 2, left, right, tree)
    ret += cumulation(mid + 1, end, node * 2 + 1, left, right, tree)
    return ret

"""index: 구간합을 수정하고자 하는 노드, dif: 기존 값과 수정할 값과의 차이"""
def update(start, end, node, index, dif, tree):
    if index < start or index > end: return;

    tree[node] += dif
    if start == end: return
    mid = (start + end) // 2
    update(start, mid, node * 2, index, dif, tree)
    update(mid + 1, end, node * 2 + 1, index, dif, tree)


def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    arr = [0] + list(map(int, [input() for _ in range(N)]))
    tree = [0] * (4 * N)

    init(arr, 1, N, 1, tree)

    for _ in range(M+K):
        A, B, C = map(int, input().split())
        if A == 1:
            dif = C - arr[B]
            update(1, N, 1, B, dif, tree)
            arr[B] = C
        else: print(cumulation(1, N, 1, B, C, tree))


if __name__ == '__main__':
    main()