from rsa_modules import PlainRSA
from experiments import Exp1, Exp2, Exp3, Exp4

securityLength = 128
objRSA = PlainRSA(securityLength)

message = 'Hello Bob!'
int_text = objRSA.generate_int(message)
encrypted_text = objRSA.encryptMessage(int_text)
decrypted_text = objRSA.decryptMessage(encrypted_text)

print('Klucz publiczny: {}'.format(objRSA.e))
print('Klucz prywatny: {}\n'.format(objRSA.d))
print('poczatkowa wiadomosc: {}'.format(message))
print('zaszyfrowany int tekstu: {}'.format(encrypted_text))
print('odszyfrowana wiadomosc: {}\n'.format(decrypted_text))

objExp1 = Exp1(securityLength)
(s, m) = objExp1.no_message_attack()
print('Wygenerowany podpis: {}'.format(s))
print('Treść szyfrogramu wiadomości: {}'.format(m))
print('Czy poprawne szyfrowanie?: {}\n'.format(
    'Tak' if objExp1.validation() else 'Nie'))

message1 = "Za oknem pada deszcz"
message2 = "Moj tajny tekst."
objExp2 = Exp2(securityLength, message1, message2)
s = objExp2.make_experiment()
print('\nWygenerowany podpis: {}'.format(s))
print('Czy poprawne szyfrowanie?: {}\n'.format(
    'Tak' if objExp2.validation() else 'Nie'))

# objExp3 = Exp3(securityLength)
# objExp4 = Exp4(securityLength)
