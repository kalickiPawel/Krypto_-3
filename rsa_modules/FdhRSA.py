from Crypto.Util.number import getPrime
import binascii
from logger import logger
import logging

logger = logging.getLogger(__name__)


class FdhRSA(PlainRSA):
    """
    Improved PlainRSA scheme to the version with attachment (RSA-FDH),
    i.e. this algorithm uses a hash function (signed (encrypted) the
    private key is the message shortcut, not the message itself.)
    """

    def __init__(self, size):
        super().__init__(size)

    def generate_hash(self, message):
        pass

    def encryptMessage(self, message):
        hash_for_message = self.generate_hash(message)
        self.encryptMessage(hash_for_message)
