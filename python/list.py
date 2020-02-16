
# list(iterable) .... 

# union find
class UnionFind()
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents = self.find(self.parents[x])
            return self.parents[x]
    
    def size(self, x):
        return -self.parents[self.find(x)]
    
    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False
        
        if self.parents[a] > self.parents[b]:
            a, b = b, a
        
        self.parents[a] += self.parents[b]
        self.parents[b] = a

        return True
