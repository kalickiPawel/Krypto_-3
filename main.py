from PlainRSA import PlainRSA
from Experiments import Exp1, Exp2, Exp3, Exp4
import logger

securityLength = 128
objRSA = PlainRSA(securityLength)

message = 'Hello Bob!'
encrypted_text = objRSA.encryptMessage(message)
decrypted_text = objRSA.decryptMessage(encrypted_text)

print("Klucz publiczny: {}".format(objRSA.e))
print("Klucz prywatny: {}".format(objRSA.d))
print('poczatkowa wiadomosc: {}'.format(message))
print('zaszyfrowany int tekstu: {}'.format(encrypted_text))
print('odszyfrowana wiadomosc: {}'.format(decrypted_text))

objExp1 = Exp1(securityLength)
(s, m) = objExp1.no_message_attack()
print("To jest s: {}".format(s))
print("To jest m: {}".format(m))

# objExp2 = Exp2(securityLength)
# objExp3 = Exp3(securityLength)
# objExp4 = Exp4(securityLength)
