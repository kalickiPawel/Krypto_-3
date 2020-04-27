from Crypto.Util.number import getPrime
import binascii
from logger import logger
import logging

logger = logging.getLogger(__name__)


class PlainRSA():
    def __init__(self, size):
        self.size = size
        p, q = getPrime(size), getPrime(size)
        phi = (p-1)*(q-1)
        self.n, self.e = p*q, 65537
        self.d = self.modinv(self.e, phi)

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def generate_int(self, m):
        hex_data = binascii.hexlify(m.encode())
        text_int = int(hex_data, 16)
        logger.info('Wiadomosc: {}'.format(m))
        logger.info('dane w hex: {}'.format(hex_data))
        logger.info('dane w int: {}\n'.format(text_int))
        if text_int > self.n:
            raise Exception('tekst za duzy dla klucza')
        return text_int

    def generate_txt(self, c):
        return binascii.unhexlify(hex(c)[2:]).decode()

    def encryptMessage(self, m):
        return pow(m, self.d, self.n)

    def decryptMessage(self, c):
        return pow(c, self.e, self.n)
