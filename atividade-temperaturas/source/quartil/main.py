class quartil:
    def __init__(self, data):
        self.data = list(map(int, data))

    def primeiro_quartil(self):
        n = len(self.data)
        self.data.sort()
        if n % 2 == 0:
            return (self.data[n//4 - 1] + self.data[n//4]) / 2
        else:
            return self.data[n//4]
    
    def segundo_quartil(self):
        n = len(self.data)
        self.data.sort()
        if n % 2 == 0:
            return (self.data[n//2 - 1] + self.data[n//2]) / 2
        else:
            return self.data[n//2]

    def terceiro_quartil(self):
        n = len(self.data)
        self.data.sort()
        if n % 2 == 0:
            return (self.data[3*n//4 - 1] + self.data[3*n//4]) / 2
        else:
            return self.data[3*n//4]