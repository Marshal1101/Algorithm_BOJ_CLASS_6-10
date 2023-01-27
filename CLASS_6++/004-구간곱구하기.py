import sys, math

DIV = 10 ** 9 + 7

def init_tree(arr, tree, start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = (start + end) // 2
    left_val = init_tree(arr, tree, start, mid, node * 2)
    right_val = init_tree(arr, tree, mid+1, end, node * 2 + 1)
    tree[node] = left_val * right_val % DIV
    return tree[node]


def cumulate(tree, left, right, start, end, node):
    if left > end or right < start: return 1
    if left <= start and end <= right: return tree[node]

    mid = (start + end) // 2
    left_val = cumulate(tree, left, right, start, mid, node * 2)
    right_val = cumulate(tree, left, right, mid+1, end, node * 2 + 1)
    return left_val * right_val % DIV


def update(arr, tree, index, val, start, end, node):
    if index < start or index > end: return

    if start == end:
        tree[node] = val
        return

    mid = (start + end) // 2
    update(arr, tree, index, val, start, mid, node * 2)
    update(arr, tree, index, val, mid+1, end, node * 2 + 1)
    tree[node] = tree[node * 2] * tree[node * 2 + 1] % DIV


def main():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    arr = [-1] + [int(input()) for _ in range(N)]
    width = 2 ** math.ceil(math.log2(N))
    tree = [1] * (width * 2)

    init_tree(arr, tree, 1, N, 1)
    
    for _ in range(M+K):
        A, B, C = map(int, input().split())
        if A == 1: update(arr, tree, B, C, 1, N, 1)
        else: print(cumulate(tree, B, C, 1, N, 1))


if __name__ == '__main__':
    main()