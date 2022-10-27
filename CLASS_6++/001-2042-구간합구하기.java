import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;


public class Main {
    public long init_tree(long[] arr, int start, int end, int node, long[] tree) {
        if (start == end) {
            tree[node] = arr[start];
            return tree[node];
        }
        int mid = (start + end) / 2;
        tree[node] += init_tree(arr, start, mid, node * 2, tree);
        tree[node] += init_tree(arr, mid+1, end, node * 2 + 1, tree);
        return tree[node];
    }

    public long cumulation(int start, int end, int node, int left, int right, long[] tree) {
        long ret = 0;
        if (left > end || right < start) return ret;
        if (left <= start && end <= right) return tree[node];

        int mid = (start + end) / 2;
        ret += cumulation(start, mid, node * 2, left, right, tree);
        ret += cumulation(mid+1, end, node * 2 + 1, left, right, tree);
        return ret;
    }

    public void update(int start, int end, int node, int index, long diff, long[] tree) {
        if (index < start || index > end) return;

        tree[node] += diff;
        if (start == end) return;
        int mid = (start + end) / 2;
        update(start, mid, node * 2, index, diff, tree);
        update(mid+1, end, node * 2 + 1, index, diff, tree);
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        long[] arr = new long[N+1];
        long[] tree = new long[4*N];

        for (int i = 1; i < N+1; i++) {
            arr[i] = Long.parseLong(br.readLine());
        }

        init_tree(arr, 1, N, 1, tree);
        
        for (int i = 0; i < M+K; i++) {
            int a, b; 
            long diff;
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            if (a == 1) {
                long c = Long.parseLong(st.nextToken());
                diff = c - arr[b];
                update(1, N, 1, b, diff, tree);
                arr[b] = c;
            }
            else {
                int c = Integer.parseInt(st.nextToken());
                sb.append(cumulation(1, N, 1, b, c, tree)).append('\n');
            }
        }

        bw.write(sb.toString());
        bw.flush();
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}