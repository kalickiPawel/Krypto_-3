from Crypto.Util.number import getPrime
from experiments import Experiment
import logging


logger = logging.getLogger(__name__)


class Exp1(Experiment):
    """ Eksperyment 1 - No - message attack
        wygeneruj losowy podpis s i oblicz m = s ^ e mod N.
        Na wyjściu otrzymasz parę podpis, wiadomość (s,  m)
        wygenerowaną pomimo braku użycia klucza prywatnego.
    """

    def __init__(self, size):
        super().__init__(size)
        logger.info('>---Start the Experiment 1--<\n')

    def no_message_attack(self):
        self.s_exp1 = getPrime(self.size)
        self.m_exp1 = self.encryptMessage(self.s_exp1)
        return(self.s_exp1, self.m_exp1)

    def validation(self):
        return super().validation(self.s_exp1, self.m_exp1)
