from rsa_modules import PlainRSA
import logging

logger = logging.getLogger(__name__)


class Experiment(PlainRSA):
    def __init__(self, size):
        super().__init__(size)

    def validation(self, c, m) -> bool:
        logger.warning("Start validation")
        decrypt = self.decrypt_message(c)
        return m == decrypt
