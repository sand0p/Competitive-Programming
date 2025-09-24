from collections import deque

class Trie:
    class Node:
        def __init__(self, data):
            self.data = data
            self.children = [None] * 26
            self.parent = None
            self.is_endpoint = False
            self.dist = float("inf")

    def __init__(self):
        self.root = self.Node(None)

    def add_word(self, word):
        at = self.root
        beginning_to_add = None
        for c in word:
            c_index = ord(c) - ord("a")
            if at.children[c_index]:
                at = at.children[c_index]
            else:
                at.children[c_index] = self.Node(c)
                at.children[c_index].parent = at
                at = at.children[c_index]
                if (beginning_to_add == None and at.is_endpoint == False and at != self.root):
                    beginning_to_add = at
                    
        if beginning_to_add:
            beginning_to_add.children.append(at)
        at.is_endpoint = True

    def bfs(self):
        Q = deque([(self.root, 0)])
        while Q:
            at, dist = Q.popleft()
            if dist >= at.dist:
                continue
            at.dist = dist
            for neigh in at.children:
                if neigh != None:
                    Q.append((neigh, dist + 1))
            if at.parent != None:
                Q.append((at.parent, dist + 1))

    def find_out(self, word):
        at = self.root
        i = 0
        last_in_trie = len(word)
        while i < len(word):
            c_index = ord(word[i]) - ord("a")
            if at.children[c_index] != None:
                at = at.children[c_index]
                last_in_trie = at.dist
                i += 1
            else:
                break
        print(min(len(word), last_in_trie + len(word) - i))

n, m = map(int, input().split())

words = [input() for _ in " " * n]
trie = Trie()
for w in words:
    trie.add_word(w)
trie.bfs()
for _ in " " * m:
    w = input()
    trie.find_out(w)