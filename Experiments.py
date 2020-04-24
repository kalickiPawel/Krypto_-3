from PlainRSA import PlainRSA
from Crypto.Util.number import getPrime
import binascii
from logger import logger


class Experiment(PlainRSA):
    def __init__(self, size):
        PlainRSA.__init__(self, size)

    def validation(self, s, m):
        logger.info("Validating")
        decrypt = pow(s, self.e, self.n)
        if m != decrypt:
            return False
        return True


class Exp1(Experiment):
    """ Eksperyment 1 - No - message attack
        wygeneruj losowy podpis s i oblicz m = s ^ e mod N.
        Na wyjściu otrzymasz parę podpis, wiadomość (s,  m)
        wygenerowaną pomimo braku użycia klucza prywatnego.
    """

    def __init__(self, size):
        Experiment.__init__(self, size)
        logger.info('\n>---Start the Experiment 1--<\n')

    def no_message_attack(self):
        self.s_exp1 = getPrime(self.size)
        self.m_exp1 = pow(self.s_exp1, self.e, self.n)
        return(self.s_exp1, self.m_exp1)

    def validation(self):
        super().validation(self.s_exp1, self.m_exp1)


class Exp2(Experiment):
    """ Eksperyment 2 - Adwersarz wybiera dwie wiadomość m1, m2
        - takie, że m = m1 * m2 mod N. Następnie uzyskuje podpisy 
        dla wiadomości m1, m2 odpowiednio s1 i s2. 
        Adwersarz oblicza podpis dla m jako s = s1 * s2 mod N.
    """

    def __init__(self, size, m1, m2):
        Experiment.__init__(self, size)
        logger.info('\n>---Start the Experiment 2--<\n')

        self.m1 = self.generate_text(m1)
        self.m2 = self.generate_text(m2)

        self.s1 = pow(self.m1, self.e, self.n)
        self.s2 = pow(self.m2, self.e, self.n)

        self.m_exp2 = self.realise_multiply_mod(self.m1, self.m2)
        self.s_exp2 = self.realise_multiply_mod(self.s1, self.s2)

    def generate_text(self, m):
        hex_data = binascii.hexlify(m.encode())
        plain_text = int(hex_data, 16)
        logger.info('Wiadomosc: {}'.format(m))
        logger.info('dane w hex: {}'.format(hex_data))
        logger.info('int tekst: {}'.format(plain_text))
        return plain_text

    def make_experiment(self):
        return self.s_exp2

    def realise_multiply_mod(self, a, b):
        return a * b % self.n

    def validation(self):
        super().validation(self.s_exp2, self.m_exp2)


class Exp3(Experiment):
    pass


class Exp4(Experiment):
    pass
