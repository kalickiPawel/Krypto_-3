from Crypto.Util.number import getPrime
from logger import logger_setup
import binascii
import logging

logger = logging.getLogger(__name__)


class Plain:
    """
    Implementation of the basic RSA signature algorithm (Plain RSA),
    i.e. without using the hash function.
    """

    def __init__(self, size):
        self.size = size

        p, q = getPrime(size), getPrime(size)

        self.n, self.e = p * q, 65537
        phi = (p - 1) * (q - 1)
        self.d = self.mod_inv(self.e, phi)

        logger.warning('Value of p: {}'.format(p))
        logger.warning('Value of q: {}'.format(p))
        logger.warning('Value of n: {}'.format(self.n))

    def euclidean_algorithm(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.euclidean_algorithm(b % a, a)
            return g, x - (b // a) * y, y

    def mod_inv(self, a, m):
        g, x, y = self.euclidean_algorithm(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def generate_int(self, m):
        hex_data = binascii.hexlify(m.encode())
        text_int = int(hex_data, 16)
        logger.info('Message: {}'.format(m))
        logger.info('Data in hex: {}'.format(hex_data))
        logger.info('Data in int: {}\n'.format(text_int))
        if text_int > self.n:
            raise Exception('Text is too big for key')
        return text_int

    @staticmethod
    def generate_txt(c):
        return binascii.unhexlify(hex(c)[2:]).decode()

    def encrypt_message(self, m):
        return pow(m, self.d, self.n)

    def decrypt_message(self, c):
        return pow(c, self.e, self.n)
