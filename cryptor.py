
import base64
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys


def main():
    option, password, pin, file = 0, 0, 0, 0

    cmdlength = len(sys.argv)
    if cmdlength > 1:
        option = sys.argv[1]
        if option == "-h":
            print("python3 cryptor.py [OPTION] [PASSWORD] [PIN] [FILE]")
            print()
            print("OPTIONS")
            print("-e   encrypt")
            print("-d   decrypt")
            print("-ds  decrypt and save to file ")
            print()
            print("FILE")
            print("to decrypt or encrypt a file")
            print("it has to be in the same directory this file")
            print()
            print("EXAMPLE")
            print("python3 cryptor.py -e password 1234 secret.txt")



        elif cmdlength > 4:

            password = sys.argv[2]

            pin = sys.argv[3]

            file = sys.argv[4]

            if option == "-e":
                encrypt(password.encode("ascii"), pin.encode("ascii"), file)


            elif option == "-d":
                decrypt(password.encode("ascii"), pin.encode("ascii"), file,False)

            elif option == "-ds":
                decrypt(password.encode("ascii"), pin.encode("ascii"), file,True)
            else:
                error()

        else:
            error()
    else:
        error()



def error():
    print("")
    print("ERROR")
    print("make sure you're in the same folder as cryptor.py")
    print("then type in 'python3 cryptor.py -h' for help")
    print("")

def encrypt(password, pin, file):



    cipher = get_cipher(password,pin)

    f = open(str(file),"r")

    unencrypted_text = f.read().encode("ascii")

    encrypted_text = cipher.encrypt(unencrypted_text)

    file = str(file).split(".")[0]+".enc"

    enc = open(file,"w")

    enc.write(encrypted_text.decode("utf-8"))

    print()
    print("Successful encryption")
    print("created file called: ",file)
    print()


def decrypt(password, pin, file,save):

    cipher = get_cipher(password,pin)

    enc = open(str(file),"r")

    encrypted_text = enc.read()

    unencrypted_text = str(cipher.decrypt(encrypted_text.encode("ascii")),'utf-8')

    print(unencrypted_text)

    if save == True:

        file = str(file).split(".")[0]+".txt"
        txt = open(file,"w")
        txt.write(unencrypted_text)
        print()
        print("File Write Successful")
        print("created file called: ",file)
        print()





def get_cipher(password,pin):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256,
                     length=32,
                     salt=pin,
                     iterations=1000000,
                     backend=default_backend())

    cipher_key = base64.urlsafe_b64encode(kdf.derive(password))

    cipher = Fernet(cipher_key)

    return cipher


if __name__ == '__main__':
    main()
