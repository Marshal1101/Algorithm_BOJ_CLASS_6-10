import sys


def insert(trie:dict, string:str) -> None:
    cur_dict = trie
    for c in string:
        if c not in cur_dict:
            cur_dict[c] = {}
        cur_dict = cur_dict[c]
    cur_dict["*"] = len(string)

def search(trie, setName, word) -> int:
    cur_node = trie
    for c in word:
        if c not in cur_node:
            return False
        cur_node = cur_node[c]
        if "*" in cur_node:
            i = cur_node["*"]
            if word[i:] in setName:
                return True

def main():
    input = sys.stdin.readline
    C, N = map(int, input().split())
    setColor = set()
    setName = set()
    long_col = 0
    for _ in range(C):
        color = input().rstrip()
        if len(color) > long_col:
            long_col = len(color)
        setColor.add(color)
    for _ in range(N):
        name = input().rstrip()
        setName.add(name)
    
    Q = int(input())
    for _ in range(Q):
        team = input().rstrip()
        word = ""
        for i in range(len(team)):
            word += team[i]
            if len(word) > long_col:
                print("No")
                break
            if word in setColor:
                if team[i+1:] in setName:
                    print("Yes")
                    break
        else:
            print("No")


if __name__ == '__main__':
    main()