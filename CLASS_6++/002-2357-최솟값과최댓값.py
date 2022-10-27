import sys, math

MAX =  10 ** 9 + 1
MIN = 0

def init_tree(arr, tree, start, end, node = 1):
    if start == end:
        tree[node] = (arr[start], arr[start])
        return tree[node]

    mid = (start + end) // 2
    left_val = init_tree(arr, tree, start, mid, node * 2)
    right_val = init_tree(arr, tree, mid+1, end, node * 2 + 1)
    min_val = left_val[0] if left_val[0] < right_val[0] else right_val[0]
    max_val = left_val[1] if left_val[1] > right_val[1] else right_val[1]
    return (min_val, max_val)
    
def get_val(tree, left, right, start, end, node):
    if right < start or left > end:
        return (MAX, MIN)
    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    left_val = get_val(tree, left, right, start, mid, node * 2, )
    right_val = get_val(tree, left, right, mid+1, end, node * 2 + 1)
    min_val = left_val[0] if left_val[0] < right_val[0] else right_val[0]
    max_val = left_val[1] if left_val[1] > right_val[1] else right_val[1]
    return (min_val, max_val)


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = [0] + [int(input()) for _ in range(N)]
    width = 2 ** math.ceil(math.log2(len(arr)))
    tree = [(MAX, MIN) for _ in range(2 * width)]

    init_tree(arr, tree, 1, N, 1)
    for _ in range(M):
        start, end = map(int, input().split())
        print(*get_val(tree, start, end, 1, N, 1))


if __name__ == '__main__':
    main()