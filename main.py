from PlainRSA import PlainRSA
from Experiments import Exp1, Exp2, Exp3, Exp4
import logger

securityLength = 128
objRSA = PlainRSA(securityLength)

message = 'Hello Bob!'
encrypted_text = objRSA.encryptMessage(message)
decrypted_text = objRSA.decryptMessage(encrypted_text)

print('\nKlucz publiczny: {}'.format(objRSA.e))
print('Klucz prywatny: {}'.format(objRSA.d))
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
