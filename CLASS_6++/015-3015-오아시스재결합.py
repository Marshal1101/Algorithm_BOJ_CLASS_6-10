import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    stk = []
    ans = 0
    for _ in range(N):
        c = int(input())

        while stk and stk[-1][0] < c:
            ans += stk.pop()[1]

        if not stk:
            stk.append((c, 1))
        else:
            if stk[-1][0] == c:
                eq_cnt = stk.pop()[1]
                ans += eq_cnt
                if stk:
                    ans += 1
                stk.append((c, eq_cnt+1))
            else:
                ans += 1
                stk.append((c, 1))

    print(ans)


if __name__ == '__main__':
    main()