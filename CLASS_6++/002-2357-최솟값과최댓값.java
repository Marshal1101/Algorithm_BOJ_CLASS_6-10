import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;


public class Main {
    int MAX = 1000000001;
    int MIN = 0;

    public int[] initTree(int[] arr, int[][] tree, int start, int end, int node) throws Exception {
        if (start == end) {
            tree[node][0] = arr[start];
            tree[node][1] = arr[start];
            return tree[node];
        }

        int mid = (start + end) / 2;
        int[] leftVal = initTree(arr, tree, start, mid, node * 2);
        int[] rightVal = initTree(arr, tree, mid+1, end, node * 2 + 1);
        int minVal = leftVal[0] < rightVal[0] ? leftVal[0] : rightVal[0]; 
        int maxVal = leftVal[1] > rightVal[1] ? leftVal[1] : rightVal[1];
        tree[node][0] = minVal;
        tree[node][1] = maxVal;
        return tree[node];
    }

    public int[] getMinMaxVal(int[][] tree, int left, int right, int start, int end, int node) throws Exception {
        int[] ret = new int[2];

        if (left > end || right < start) {
            ret[0] = MAX;
            ret[1] = MIN;
            return ret;
        }
        if (left <= start && right >= end) return tree[node];

        int mid = (start + end) / 2;
        int[] leftVal = getMinMaxVal(tree, left, right, start, mid, node * 2);
        int[] rightVal = getMinMaxVal(tree, left, right, mid+1, end, node * 2 + 1);
        ret[0] = leftVal[0] < rightVal[0] ? leftVal[0] : rightVal[0]; 
        ret[1] = leftVal[1] > rightVal[1] ? leftVal[1] : rightVal[1];
        return ret;
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        
        int[] arr = new int[N+1];
        for (int i = 1; i < N+1; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        int maxSize = 1 << ((int) Math.ceil(Math.log(N) / Math.log(2)) + 1);
        int[][] tree = new int[maxSize][2];
        initTree(arr, tree, 1, N, 1);

        int a, b;
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            int[] ret = getMinMaxVal(tree, a, b, 1, N, 1);
            sb.append(ret[0] + " " + ret[1]).append('\n');
        }

        bw.write(sb.toString());
        bw.flush();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}