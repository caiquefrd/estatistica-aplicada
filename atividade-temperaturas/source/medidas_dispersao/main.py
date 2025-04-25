class medidas_dispersao:
    def __init__(self, data):
        self.data = list(map(int, data))

    def desvio_padrao(self):
        media = sum(self.data) / len(self.data)
        variancia = sum((x - media) ** 2 for x in self.data) / len(self.data)
        desvio_padrao = variancia ** 0.5

        return desvio_padrao
    
    def variancia(self):
        media = sum(self.data) / len(self.data)
        variancia = sum((x - media) ** 2 for x in self.data) / len(self.data)

        return variancia
