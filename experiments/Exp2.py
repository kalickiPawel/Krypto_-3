from experiments import Experiment
import logging

logger = logging.getLogger(__name__)


class Exp2(Experiment):
    """ 
    Experiment 2 - Obtaining the key for m = m1*m2 mod N.
    """

    def __init__(self, size, m1, m2):
        super().__init__(size)
        logger.info('>---Start the Experiment 2--<\n')

        self.m1 = self.generate_int(m1)
        self.m2 = self.generate_int(m2)

        self.s1 = self.encrypt_message(self.m1)
        self.s2 = self.encrypt_message(self.m2)

        self.m_exp2 = self.realise_multiply_mod(self.m1, self.m2)
        self.s_exp2 = self.realise_multiply_mod(self.s1, self.s2)

    def make_experiment(self):
        return self.s_exp2

    def realise_multiply_mod(self, a, b):
        return (a * b) % self.n

    def validation(self):
        return super().validation(self.s_exp2, self.m_exp2)
