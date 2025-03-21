class Amplitude:
    def __init__(self, data):
        self.data = data

    def calculate(self):
        return max(self.data) - min(self.data)