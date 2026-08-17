class Tree:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = Tree()

    def addWord(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Tree()
            cur = cur.children[c]

        cur.endOfWord = True

    def search(self, word):
        def dfs(i, cur):

            if i == len(word):
                return cur.endOfWord

            c = word[i]

            if c != '.':
                if c not in cur.children:
                    return False
                return dfs(i + 1, cur.children[c])

            else:
                for child in cur.children.values():
                    if dfs(i + 1, child):
                        return True
                return False

        return dfs(0, self.root)

        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)