class SegmentTree {
    /** arr 원본 배열, start: 시작인덱스, end:배열끝인덱스, node:트리루트 */
    constructor(arr, start = 0, end = arr.length-1, node = 1) {
        const width = 2 ** Math.ceil(Math.log2(arr.length));
        this.tree = new BigInt64Array(2 * width);
        this.arr = arr;
        this.start = start;
        this.end = end;
        this.node = node;
        this.val = null;
    }

    /** 배열로 누적 합 트리 생성 start: 시작인덱스, end: 끝인덱스, node:노드시작인덱스 */
    initTree(start = this.start, end = this.end, node = this.node) {
        if (start == end) {
            this.tree[node] = this.arr[start];
            return this.tree[node];
        }

        let mid = parseInt((start + end) / 2);
        this.tree[node] += this.initTree(start, mid, 2*node);
        this.tree[node] += this.initTree(mid+1, end, 2*node+1);
        return this.tree[node];
    }

    /** 인덱스 left에서 right까지 합을 반환한다. */
    getSum(left, right, start = this.start, end = this.end, node = this.node) {
        if (start > right || end < left) return 0n;
        if (start >= left && end <= right) return this.tree[node];

        let mid = parseInt((start + end) / 2);
        return (
            this.getSum(left, right, start, mid, 2*node) + 
            this.getSum(left, right, mid+1, end, 2*node+1)
        );
    }

    /** arr[index]의 값을 val으로 수정한다. */
    update(index, val, start = this.start, end = this.end, node = this.node) {
        if (index < start || index > end) return;

        let diff = val - this.arr[index];
        this.tree[node] += diff;
        if (start == end) return;
        
        let mid = parseInt((start + end) / 2);
        this.update(index, val, start, mid, 2*node);
        this.update(index, val, mid+1, end, 2*node+1);
        if (node == 1) this.arr[index] = val;
    }
}

let input = require('fs').readFileSync(
    'z.in'
    ).toString().trim().split('\n');
const [N, M, K] = input[0].split(" ").map(Number);
const arr = new Array(N+1).fill(0n);
for (let i = 1; i < N+1; i++) {
    arr[i] = BigInt(input[i]);
}

const tree = new SegmentTree(arr, 1, N, 1);
tree.initTree();

let answer = "";
for (let i = N+1; i < N+1+M+K; i++) {
    let [a, b, c] = input[i].split(" "); 
    if (Number(a) == 1) tree.update(Number(b), BigInt(c));
    else answer += `${tree.getSum(Number(b), Number(c))}\n`;
}

console.log(answer);