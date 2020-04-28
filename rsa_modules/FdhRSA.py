from Crypto.Hash import SHA256
from rsa_modules import PlainRSA
import logging


class FdhRSA(PlainRSA):
    """
    Improved PlainRSA scheme to the version with attachment (RSA-FDH),
    i.e. this algorithm uses a hash function (signed (encrypted) the
    private key is the message shortcut, not the message itself.)
    """

    def __init__(self, size):
        super().__init__(size)
        self.logger = logging.getLogger(__name__)

    def generate_hash(self, message):
        pass

    def encryptMessage(self, message):
        hash_for_message = self.generate_hash(message)
        self.encryptMessage(hash_for_message)
