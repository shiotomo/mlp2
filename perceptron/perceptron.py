class Perceptron:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def function(self, w1, w2):
        return self.x * w1 + self.y * w2

    def and_gate(self):
        w1 = 0.5
        w2 = 0.5
        theta = 0.7
        tmp = self.function(w1, w2)
        if tmp > theta:
            return 1
        return 0

    def or_gate(self):
        w1 = 0.7
        w2 = 0.7
        theta = 0.3
        tmp = self.function(w1, w2)
        if tmp > theta:
            return 1
        return 0

x = input("x => ")
y = input("y => ")
perceptron = Perceptron(x, y)
print(perceptron.and_gate())
print(perceptron.or_gate())
