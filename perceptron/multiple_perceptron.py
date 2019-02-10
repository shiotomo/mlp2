from perceptron import Perceptron

class MultiplePerceptron(Perceptron):
    def xor_gate(self, x, y):
        return self.and_gate(self.or_gate(x, y), self.nand_gate(x, y))

if __name__ == '__main__':
    x = float(input("x => "))
    y = float(input("y => "))
    multiple_perceptron = MultiplePerceptron()
    print(multiple_perceptron.xor_gate(x, y))
