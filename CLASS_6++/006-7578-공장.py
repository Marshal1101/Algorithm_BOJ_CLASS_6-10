import sys, math


class SegmentTree:
    def __init__(self, N, arrA, arrB) -> None:
        self.arrA = [0] + arrA
        self.arrB = [0] + arrB
        self.N = N
        self.width = 2 ** (math.ceil(math.log2(self.N)) + 1)
        self.tree = [0] * self.width
        self.dicB = {}
        for i in range(1, self.N+1):
            self.dicB[self.arrB[i]] = i


    def update(self, start, end, node, idx) -> None:
        if idx > end or idx < start: return

        self.tree[node] += 1
        if start == end: return
        
        mid = (start + end) // 2
        self.update(start, mid, node*2, idx)
        self.update(mid+1, end, node*2+1, idx)


    def treeSum(self, start, end, node, left, right) -> int:
        if left <= start and end <= right:
            return self.tree[node]
        
        if left > end or right < start:
            return 0
        
        mid = (start + end) // 2
        return (
            self.treeSum(start, mid, node*2, left, right) +
            self.treeSum(mid+1, end, node*2+1, left, right)
        )

    
    def count(self, length = None):
        if length == None:
            length = self.N+1
        
        ans = 0
        for i in range(1, length):
            idx = self.dicB[self.arrA[i]]
            ans += self.treeSum(1, self.N, 1, idx, self.N)
            self.update(1, self.N, 1, idx)
        
        print(ans)


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    solution = SegmentTree(N, arrA, arrB)
    solution.count()