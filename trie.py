class Trie:

    def __init__(self):
        self.child={}
        
    def insert(self, word: str) -> None:
        cur=self.child
        for i in word:
            if i not in cur:
                cur[i]={}
            cur=cur[i]
        cur['#']=1
        
    def search(self, word: str) -> bool:
        cur=self.child
        for i in word:
            if i not in cur:
                return False
            cur=cur[i]
        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        cur=self.child
        for i in prefix:
            if i not in cur:
                return False
            cur=cur[i]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)