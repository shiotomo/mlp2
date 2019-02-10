class Perceptron:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def function(self, theta, w1, w2):
        tmp = self.x * w1 + self.y * w2
        if tmp > theta:
            return 1
        return 0

    def and_gate(self):
        w1 = 0.5
        w2 = 0.5
        theta = 0.7
        return self.function(theta, w1, w2)

    def or_gate(self):
        w1 = 0.7
        w2 = 0.7
        theta = 0.3
        return self.function(theta, w1, w2)

    def nand_gate(self):
        w1 = -0.3
        w2 = -0.3
        theta = -0.5
        return self.function(theta, w1, w2)

    def nor_gate(self):
        w1 = -0.5
        w2 = -0.5
        theta = -0.3
        return self.function(theta, w1, w2)


x = float(input("x => "))
y = float(input("y => "))
perceptron = Perceptron(x, y)
print("AND: " + str(perceptron.and_gate()))
print("OR: " + str(perceptron.or_gate()))
print("NAND: " + str(perceptron.nand_gate()))
print("NOR: " + str(perceptron.nor_gate()))
