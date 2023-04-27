import sys
input = sys.stdin.readline

c, n = map(int, input().split())
tree_c = dict()
set_n = set()

def insert(tree, word) :
    cur = tree
    for char in word :
        if char not in cur :
            cur[char] = dict()
        cur = cur[char]
    cur["*"] = len(word)
    
def startswith(tree, word) :
    cur = tree
    for char in word :
        if char not in cur :
            return False
        cur = cur[char]
        if "*" in cur :
            idx = cur['*']
            if word[idx:] in set_n :
                return True
    
for _ in range(c) :
    color = input().rstrip()
    cur = tree_c
    insert(tree_c, color)
for _ in range(n) :
    name = input().rstrip()
    set_n.add(name)

q = int(input())
for _ in range(q) :
    team = input().rstrip()
    if startswith(tree_c, team) :
        print("Yes")
    else :
        print("No")
        