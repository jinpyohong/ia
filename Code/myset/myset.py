class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):     # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other.data:        # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other.data:           # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)

    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:

    def __ior__(self, other):
        self.concat(other.data) # in-place operation |
        return self             # for = 

    def __iand__(self, other):
        res = [x for x in self.data if x in other.data]
        self.data = res
        return self

    
    def add(self, elem):
        if elem not in self.data:
            self.data.append(elem)
            
if __name__ == '__main__':    
    x = Set([1,3,5,7, 1, 3])
    y = Set([2,1,4,5,6])
    print(x, y, len(x))
    print(x.intersection(y), y.union(x))
    print(x & y, x | y)
    print(x[2], y[:2])
    for element in x:
        print(element, end=' ')
    print()
    print(3 not in y)  # membership test
    print(list(x))   # convert to list because x is iterable

    x |= y
    print(x)
    x &= y
    print(x)