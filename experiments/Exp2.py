from experiments import Experiment
import binascii
import logging


logger = logging.getLogger(__name__)


class Exp2(Experiment):
    """ Eksperyment 2 - Adwersarz wybiera dwie wiadomość m1, m2
        - takie, że m = m1 * m2 mod N. Następnie uzyskuje podpisy 
        dla wiadomości m1, m2 odpowiednio s1 i s2. 
        Adwersarz oblicza podpis dla m jako s = s1 * s2 mod N.
    """

    def __init__(self, size, m1, m2):
        super().__init__(size)
        logger.info('>---Start the Experiment 2--<\n')

        self.m1 = self.generate_int(m1)
        self.m2 = self.generate_int(m2)

        self.s1 = self.encryptMessage(self.m1)
        self.s2 = self.encryptMessage(self.m2)

        self.m_exp2 = self.realise_multiply_mod(self.m1, self.m2)
        self.s_exp2 = self.realise_multiply_mod(self.s1, self.s2)

    def make_experiment(self):
        return self.s_exp2

    def realise_multiply_mod(self, a, b):
        return (a * b) % self.n

    def validation(self):
        return super().validation(self.s_exp2, self.m_exp2)
