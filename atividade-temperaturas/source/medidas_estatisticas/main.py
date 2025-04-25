class medidas_estatisticas:

    def __init__(self, data):
        self.data = data
    
    def media(self):
        sum = 0
        for temp in self.data:
            sum += int(temp)

        return sum / len(self.data)

    def moda(self):
        frequencia = {}
        for temp in self.data:
            if temp not in frequencia:
                frequencia[temp] = 1
            else:
                frequencia[temp] += 1
            
        moda = max(frequencia, key=frequencia.get)
        
        return moda

    def mediana(self):
        data = sorted(self.data)
        n = len(data)
        if n % 2 == 0:
            mediana = (data[n//2] + data[n//2 - 1]) / 2
        else:
            mediana = data[n//2]

        return mediana
        


