class percentil:
    def __init__(self, data):
        self.data = list(map(int, data))
    
    def percentil(self, percentil):
        self.data.sort()
        n = len(self.data)
        p = n * percentil / 100
        if p.is_integer():
            return (self.data[int(p - 1)] + self.data[int(p)]) / 2
        else:
            return self.data[int(p)]