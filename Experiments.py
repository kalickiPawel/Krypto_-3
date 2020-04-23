from PlainRSA import PlainRSA
from Crypto.Util.number import getPrime


class Experiment(PlainRSA):
    def __init__(self, size):
        PlainRSA.__init__(self, size)


class Exp1(Experiment):
    # Eksperyment 1 - No - message attack
    # wygeneruj losowy podpis s i oblicz m = s^emod  N.
    # Nawyjściuotrzymasz parę podpis, wiadomość (s,  m)
    # wygenerowaną pomimo braku użycia klucza prywatnego.
    def __init__(self, size):
        Experiment.__init__(self, size)

    def no_message_attack(self):
        experiment_S = getPrime(self.size)
        experiment_M = pow(experiment_S, self.e, self.n)
        return(experiment_S, experiment_M)


class Exp2(Experiment):
    pass


class Exp3(Experiment):
    pass


class Exp4(Experiment):
    pass
