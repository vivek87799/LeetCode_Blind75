"""
211. Design Add and Search Words Data Structure
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

"""
class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current_node = self.root
    
        for w in word:
            if w not in current_node.children:
                current_node.children[w]=TrieNode()
            current_node = current_node.children[w]
        current_node.word=True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            current_node = root
            for j in range(i, len(word)):
                if word[j] == ".":
                    for child in current_node.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if word[j] not in current_node.children:
                        return False
                    current_node = current_node.children[word[j]]
            return current_node.word        
        return dfs(0, self.root)
        
            