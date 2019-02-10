class Perceptron:
    def function(self, theta, w1, w2, x, y):
        tmp = x * w1 + y * w2
        if tmp > theta:
            return 1
        return 0

    def and_gate(self, x, y):
        w1 = 0.5
        w2 = 0.5
        theta = 0.7
        return self.function(theta, w1, w2, x, y)

    def or_gate(self, x, y):
        w1 = 0.7
        w2 = 0.7
        theta = 0.3
        return self.function(theta, w1, w2, x, y)

    def nand_gate(self, x, y):
        w1 = -0.3
        w2 = -0.3
        theta = -0.5
        return self.function(theta, w1, w2, x, y)

    def nor_gate(self, x, y):
        w1 = -0.5
        w2 = -0.5
        theta = -0.3
        return self.function(theta, w1, w2, x, y)


if __name__ == '__main__':
    x = float(input("x => "))
    y = float(input("y => "))
    perceptron = Perceptron()
    print("AND: " + str(perceptron.and_gate(x, y)))
    print("OR: " + str(perceptron.or_gate(x, y)))
    print("NAND: " + str(perceptron.nand_gate(x, y)))
    print("NOR: " + str(perceptron.nor_gate(x, y)))
