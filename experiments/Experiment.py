from rsa_modules import Plain
import logging

logger = logging.getLogger(__name__)


class Experiment(Plain):
    def __init__(self, size):
        super().__init__(size)

    def validation(self, c, m) -> bool:
        logger.warning("Start validation")
        decrypt = self.decrypt_message(c)
        return m == decrypt
