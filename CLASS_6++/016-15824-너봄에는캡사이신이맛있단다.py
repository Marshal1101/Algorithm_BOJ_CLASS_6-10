def divide(si, ei, arr):
    print(si, ei)
    if si == ei:
        return arr[si], arr[ei], 0
    
    mid = (si + ei) // 2
    fmin, fmax, fval = divide(si, mid, arr)
    bmin, bmax, bval = divide(mid+1, ei, arr)
    
    rmin = min(fmin, bmin)
    rmax = max(fmax, bmax)
    return rmin, rmax, (fval + bval + rmax - rmin) % (10 ** 9 + 7)

def pow(m, k, mod):
    if k == 0:
        return 1
    if k == 1:
        return m
    half = pow(m, k//2, mod)
    if k % 2:
        ret = half * half * m % mod
    else:
        ret = half * half % mod
    return ret

N = int(input())
arr = sorted(map(int, input().split()))
ans = 0
mod = 10**9+7
for i in range(N):
    ans += arr[i] * (pow(2, i, mod) - pow(2, N-1-i, mod))
print(ans % mod)