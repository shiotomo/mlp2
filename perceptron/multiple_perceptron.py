from perceptron import Perceptron

class MultiplePerceptron(Perceptron):

    def xor_gate(self):
        and = self.function(theta, w1, w2)
