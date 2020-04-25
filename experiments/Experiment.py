from rsa_modules import PlainRSA
from Crypto.Util.number import getPrime
import binascii
import logging

logger = logging.getLogger(__name__)


class Experiment(PlainRSA):
    def __init__(self, size):
        super().__init__(size)

    def validation(self, s, m):
        logger.warn("Start validation")
        decrypt = self.decryptMessage(s)
        if m != decrypt:
            return False
        return True
