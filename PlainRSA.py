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
        self.n = p*q
        self.e = 65537
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

    def encryptMessage(self, m):
        hex_data = binascii.hexlify(m.encode())
        plain_text = int(hex_data, 16)
        logger.info('dane w hex: {}'.format(hex_data))
        logger.info('int tekst: {}'.format(plain_text))
        if plain_text > self.n:
            raise Exception('tekst za duzy dla klucza')
        return pow(plain_text, self.e, self.n)

    def decryptMessage(self, c):
        logger.info('rozszyfrowany int tekst: {}'.format(
            pow(c, self.d, self.n)))
        return binascii.unhexlify(hex(pow(c, self.d, self.n))[2:]).decode()
