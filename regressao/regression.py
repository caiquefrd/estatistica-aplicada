class Regression:
    
    def __init__(self, data_x, data_y, n):
        self.data_x = data_x
        self.data_y = data_y
        self.n = n


    def somatory_x(self):
        return sum(self.data_x)


    def somatory_y(self):
        return sum(self.data_y)


    def somatory_xy(self):
        result = []
        for i in range(len(self.data_x)):
            xy = self.data_x[i] * self.data_y[i]
            result.append(xy)
        
        return sum(result)


    def somatory_square_x(self):
        result = []
        for i in range(len(self.data_x)):
            result.append(self.data_x[i] ** 2)

        return sum(result)


    def somatory_square_y(self):
        result = []
        for i in range(len(self.data_y)):
            result.append(self.data_y[i] ** 2)

        return sum(result)


    def find_a(self):
        som_xy = self.somatory_xy()
        som_x = self.somatory_x()
        som_y = self.somatory_y()
        som_square_x = self.somatory_square_x()
        n = self.n

        numerator = (n * som_xy) - (som_x * som_y)
        denominator = (n * som_square_x) - ( som_x ** 2 )

        return numerator / denominator


    def find_b(self):
        return (self.somatory_y() - self.find_a() * self.somatory_x()) / self.n

    def print(self):
        print('somatorio x = ', self.somatory_x())
        print('somatorio y = ',self.somatory_y())
        print('somatorio x² = ',self.somatory_square_x())
        print('somatorio xy = ',self.somatory_xy())
        print('somatorio y² = ',self.somatory_square_y())
        a = self.find_a()
        b = self.find_b()
        print("a = ", a)
        print("b = ", b)


data_x = [1,2,3,4,5]
data_y = [1,2,4,5,8]
n = 5

regression = Regression(data_x, data_y, n)
regression.print()

def y_to_x(x):
    a = regression.find_a()
    b = regression.find_b()
    result = (a * x) + b
    return result

print('y para x = 3,5 --->', y_to_x(3.5))
print('y para x = 10 --->', y_to_x(10))