a = [0] * 10
n = int(s:=input())
f = 1
for _ in s:
    for i in range(10):
        v = f * 10
        a[i] += (n // v - (i < 1)) * f + min(max(n % v + 1 - i*f, 0), f)
    f=v
print(*a)