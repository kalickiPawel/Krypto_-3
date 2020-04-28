from Crypto.Util.number import getPrime
import binascii
from logger import logger
import logging

logger = logging.getLogger(__name__)


class FdhRSA(PlainRSA):
    """
    Ulepszony schemat PlainRSA do wersji z załącznikiem (RSA-FDH), 
    tj. algorytm ten używa funkcji skrótu (podpisywany (szyfrowany) 
    kluczem prywatnym jest skrót z wiadomości a nie sama wiadomość).
    """

    def __init__(self, size):
        super().__init__(size)

    def generate_hash(self, message):
        pass

    def encryptMessage(self, message):
        hash_for_message = self.generate_hash(message)
        self.encryptMessage(hash_for_message)
