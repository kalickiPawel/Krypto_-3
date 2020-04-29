from Crypto.Hash import SHA256
from rsa_modules import PlainRSA
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
        self.logger = logging.getLogger(__name__)

    def encrypt_message(self, message):
        hash_for_message = SHA256.new()
        hash_for_message.update(bytes(message, 'ascii'))
        return super().encrypt_message(int(hash_for_message.hexdigest(), 16))

    def decrypt_message(self, c):
        return super().decrypt_message(c)
