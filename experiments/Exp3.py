from experiments import Experiment
import binascii
import logging


logger = logging.getLogger(__name__)


class Exp3(Experiment):
    """ 
    Eksperyment 3 - Atak na szyfrowanie z wykorzystaniem RSA.
    """

    def __init__(self, size):
        super().__init__(size)
        logger.info('>---Start the Experiment 3--<\n')

        self.c = 2829246759667430901779973875
        self.e = 3
        self.N = 74863748466636279180898113945573168800167314349007339734664557033677222985045895878321130196223760783214379338040678233908010747773264003237620590141174028330154012139597068236121542945442426074367017838349905866915120469978361986002240362282392181726265023378796284600697013635003150020012763665368297013349

    @staticmethod
    def nth_root(x, n):
        # Start with some reasonable bounds around the nth root.
        upper_bound = 1
        while upper_bound ** n <= x:
            upper_bound *= 2
        lower_bound = upper_bound // 2
        # Keep searching for a better result as long as the bounds make sense.
        while lower_bound < upper_bound:
            mid = (lower_bound + upper_bound) // 2
            mid_nth = mid ** n
            if lower_bound < mid and mid_nth < x:
                lower_bound = mid
            elif upper_bound > mid and mid_nth > x:
                upper_bound = mid
            else:
                # Found perfect nth root.
                return mid
        return mid + 1

    def make_experiment(self):
        message_int = int(self.nth_root(self.c, self.e))
        logger.warn("Obliczona wiadomość int: {}".format(message_int))
        return self.generate_txt(message_int)
