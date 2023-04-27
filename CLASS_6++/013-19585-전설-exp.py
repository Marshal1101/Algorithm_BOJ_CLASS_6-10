from sys import stdin
import gc
gc.disable()

_R = stdin.buffer.readline
C, N = map(int, _R().split())

# 색깔 해시:문자열 by length
CH = [set() for _ in range(1000)]
# 닉네임 해시:문자열 by length
NH = [set() for _ in range(1001)]

HASH_B = 0x811c9dc5
HASH_P = 0x01000193

for _ in range(C):
    color_name = _R()
    h = HASH_B
    for c in color_name:
        if c > 10: h = (h ^ c)*HASH_P & 0xFFFFFFFF
    CH[len(color_name)-2].add(h)

for _ in range(N):
    nick_name = _R()
    h = HASH_B
    for c in reversed(nick_name):
        h = (h ^ c)*HASH_P & 0xFFFFFFFF
    assert(h not in NH[len(nick_name)-1])
    NH[len(nick_name)-1].add(h)

Q = int(_R())
RH = [0] * 1001
for _ in range(Q):
    team_name = _R()
    h = HASH_B
    for i in range(min(len(team_name), 1001)):
        h = (h ^ team_name[-1-i])*HASH_P & 0xFFFFFFFF
        RH[i] = h
    h = HASH_B
    found = False
    for i in range(min(len(team_name), 1000)):
        h = (h ^ team_name[i])*HASH_P & 0xFFFFFFFF
        j = len(team_name)-1-i-1
        if j >= 1001: continue
        if h not in CH[i]: continue
        if RH[j] not in NH[j]: continue
        found = True
        break
    print("Yes" if found else "No")