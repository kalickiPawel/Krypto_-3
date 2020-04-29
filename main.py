from rsa_modules import Plain, Fdh
from experiments import Exp1, Exp2, Exp3, Exp4
import logging

securityLength = 128
classes = [Plain, Exp1, Exp2, Exp3, Exp4, Fdh]
logger = logging.getLogger(__name__)


class Main:
    def __init__(self, select_obj):
        self.select = int(select_obj)
        logger.info("Initialized base program")
        self.get_selection()

    def get_selection(self):
        logger.warning("Choice: {}".format(self.select))
        generate = ['generate_{}'.format(name.__name__.lower()) for name in classes]
        getattr(Main, generate[self.select])()

    @staticmethod
    def generate_plain():
        message = 'Hello Bob!'
        obj_rsa = Plain(securityLength)
        int_text = obj_rsa.generate_int(message)
        encrypted_int = obj_rsa.encrypt_message(int_text)
        decrypted_int = obj_rsa.decrypt_message(encrypted_int)
        decrypted_text = obj_rsa.generate_txt(decrypted_int)

        print('Klucz publiczny: {}'.format(obj_rsa.e))
        print('Klucz prywatny: {}\n'.format(obj_rsa.d))

        print('poczatkowa wiadomosc: {}'.format(message))
        print('zaszyfrowany int tekstu: {}'.format(encrypted_int))
        print('odszyfrowany int tekstu: {}'.format(decrypted_int))
        print('koncowa wiadomosc: {}\n'.format(decrypted_text))

    @staticmethod
    def generate_exp1():
        obj_exp_1 = Exp1(securityLength)
        (s, m) = obj_exp_1.no_message_attack()
        print('Wygenerowany podpis: {}'.format(s))
        print('Zaszyfrowany int tekstu: {}'.format(m))
        print('Czy poprawne szyfrowanie?: {}\n'.format(
            'Tak' if obj_exp_1.validation() else 'Nie'))

    @staticmethod
    def generate_exp2():
        message1 = "Za oknem pada deszcz"
        message2 = "Moj tajny tekst."
        obj_exp_2 = Exp2(securityLength, message1, message2)
        s = obj_exp_2.make_experiment()
        print('Wygenerowany podpis: {}'.format(s))
        print('Czy poprawne szyfrowanie?: {}\n'.format(
            'Tak' if obj_exp_2.validation() else 'Nie'))

    @staticmethod
    def generate_exp3():
        obj_exp_3 = Exp3(securityLength)
        print('Odczytana wiadomość to: {}\n'.format(obj_exp_3.make_experiment))

    @staticmethod
    def generate_exp4():
        message = "Przykladowy tekst Håstad"
        obj_exp_4 = Exp4(securityLength, message)
        print('Odczytana wiadomosc: {}'.format(obj_exp_4.make_experiment()))

    @staticmethod
    def generate_fdh():
        obj_fdh_rsa = Fdh(securityLength)
        message = "To jest test dla FDH RSA"
        print('\nImplementacja FDH RSA\npoczatkowa wiadomosc: {}'.format(message))
        encrypted_int = obj_fdh_rsa.encrypt_message(message)
        decrypted_int = obj_fdh_rsa.decrypt_message(encrypted_int)
        print('Czy poprawne szyfrowanie?: {}'.format(
            'Tak' if obj_fdh_rsa.validation(encrypted_int, decrypted_int) else 'Nie'))


def generate_selection():
    print("Możliwe metody do wyboru: ")
    descriptions, names = zip(*[(item.__doc__.strip(), item.__name__.strip()) for item in classes])
    print(*("\t{0} -> {2}\n\t{1}\n".format(i, text, name) for i, (text, name) in enumerate(zip(descriptions, names))))
    while True:
        try:
            choice = input("Dokonaj wyboru: ").strip()
            if int(choice) < len(classes):
                break
            else:
                print("Popraw wybor")
        except ValueError:
            print("Popraw wybor")
    return choice


if __name__ == "__main__":
    selector = generate_selection()
    main = Main(selector)
