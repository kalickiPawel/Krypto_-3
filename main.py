from rsa_modules import PlainRSA, FdhRSA
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


def generate_selection():
    print("Możliwe metody do wyboru: ")
    classes = [PlainRSA, FdhRSA, Exp1, Exp2, Exp3, Exp4]
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
