from experiments import Experiment
from functools import reduce
import logging

logger = logging.getLogger(__name__)


class Exp4(Experiment):
    """ 
    Experiment 4 - Håstad's broadcast attack.
    """

    def __init__(self, size, message):
        super().__init__(size)
        logger.info('>---Start the Experiment 4--<\n')
        message_int = self.generate_int(message)
        e = 3

        n0 = 95118357989037539883272168746004652872958890562445814301889866663072352421703264985997800660075311645555799745426868343365321502734736006248007902409628540578635925559742217480797487130202747020211452620743021097565113059392504472785227154824117231077844444672393221838192941390309312484066647007469668558141
        n1 = 98364165919251246243846667323542318022804234833677924161175733253689581393607346667895298253718184273532268982060905629399628154981918712070241451494491161470827737146176316011843738943427121602324208773653180782732999422869439588198318422451697920640563880777385577064913983202033744281727004289781821019463
        n2 = 68827940939353189613090392226898155021742772897822438483545021944215812146809318686510375724064888705296373853398955093076663323001380047857809774866390083434272781362447147441422207967577323769812896038816586757242130224524828935043187315579523412439309138816335569845470021720847405857361000537204746060031

        self.n = [n0, n1, n2]
        self.a = [pow(message_int, e, n)
                  for n in self.n]   # Generating ciphers with n's list

    def chinese_remainder(self, n, a):
        sum = 0
        prod = reduce(lambda a, b: a*b, n)
        for n_i, a_i in zip(n, a):
            p = prod // n_i
            sum += a_i * self.mul_inv(p, n_i) * p
        return sum % prod

    def make_experiment(self):
        result = self.chinese_remainder(self.n, self.a)
        result_hex = self.nth_root(result, 3)
        logger.warn("Otrzymany hex: {}".format(result_hex))
        return self.generate_txt(result_hex)

    @staticmethod
    def mul_inv(a, b):
        b0 = b
        x0, x1 = 0, 1
        if b == 1:
            return 1
        while a > 1:
            q = a // b
            a, b = b, a % b
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += b0
        return x1

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
