import sys
sys.setrecursionlimit(10**9)

def dfs(node, dp, adj, visited):
    if len(adj[node]) == 0:
        dp[node][0] = 0
        dp[node][1] = 1
    else:
        for child in adj[node]:
            if not visited[child]:
                visited[child] = True
                dfs(child, dp, adj, visited)
                dp[node][0] += dp[child][1]
                dp[node][1] += min(dp[child][0], dp[child][1])
        dp[node][1] += 1

def main():
    input = sys.stdin.readline
    N = int(input())
    adj = [[] for _ in range(N+1)]
    for _ in range(N-1):
        v1, v2 = map(int, input().split())
        adj[v1].append(v2)
        adj[v2].append(v1)

    dp = [[0]*2 for _ in range(N+1)]
    visited = [False] * (N+1)

    visited[1] = True
    dfs(1, dp, adj, visited)
    print(min(dp[1][0], dp[1][1]))


if __name__ == '__main__':
    main()