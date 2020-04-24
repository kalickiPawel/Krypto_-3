from rsa_modules import PlainRSA
from Crypto.Util.number import getPrime
import binascii
import logging

logger = logging.getLogger(__name__)


class Experiment(PlainRSA):
    def __init__(self, size):
        PlainRSA.__init__(self, size)

    def validation(self, s, m):
        logger.info("Validating")
        decrypt = pow(s, self.e, self.n)
        if m != decrypt:
            return False
        return True
