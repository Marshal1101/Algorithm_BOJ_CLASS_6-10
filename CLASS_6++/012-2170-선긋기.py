# 스위핑

import sys


def main():
    input = sys.stdin.readline
    INF = sys.maxsize
    N = int(input())
    line = sorted([tuple(map(int, input().split())) for _ in range(N)])
    ans = 0
    lp = rp = -INF
    for i in range(N):

        if rp < line[i][0]:
            ans += rp - lp
            lp = line[i][0]
            rp = line[i][1]
        else:
            rp = max(rp, line[i][1])

    ans += rp - lp
    print(ans)


if __name__ == '__main__':
    main()