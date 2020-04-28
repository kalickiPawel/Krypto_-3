from rsa_modules import PlainRSA
from experiments import Exp1, Exp2, Exp3, Exp4

securityLength = 128
obj_rsa = PlainRSA(securityLength)

message = 'Hello Bob!'
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

obj_exp_1 = Exp1(securityLength)
(s, m) = obj_exp_1.no_message_attack()
print('Wygenerowany podpis: {}'.format(s))
print('Zaszyfrowany int tekstu: {}'.format(m))
print('Czy poprawne szyfrowanie?: {}\n'.format(
    'Tak' if obj_exp_1.validation() else 'Nie'))

message1 = "Za oknem pada deszcz"
message2 = "Moj tajny tekst."
obj_exp_2 = Exp2(securityLength, message1, message2)
s = obj_exp_2.make_experiment()
print('Wygenerowany podpis: {}'.format(s))
print('Czy poprawne szyfrowanie?: {}\n'.format(
    'Tak' if obj_exp_2.validation() else 'Nie'))

obj_exp_3 = Exp3(securityLength)
print('Odczytana wiadomość to: {}\n'.format(obj_exp_3.make_experiment))

message = "Przykladowy tekst Håstad"
obj_exp_4 = Exp4(securityLength, message)
print('Odczytana wiadomosc: {}'.format(obj_exp_4.make_experiment()))

message = "To jest test dla FDH-RSA"
obj_fdh_rsa = FdhRSA(securityLength)
print(obj_fdh_rsa.encrypt_message(message))
