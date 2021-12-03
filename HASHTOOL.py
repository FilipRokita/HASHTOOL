#HASHTOOL
#Filip Rokita
#www.filiprokita.com

import hashlib

userInput = input("TEXT/FILE PATH: ")

try:
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    with open(userInput, "rb") as f:
        while True:
            fd = f.read(65536)
            if not fd:
                break
            md5.update()
            sha1.update()
            sha256.update()
    print("MD5(FILE):", md5.hexdigest())
    print("SHA1(FILE):", sha1.hexdigest())
    print("SHA256(FILE):", sha256.hexdigest())

except:
    encoded = userInput.encode()
    md5 = hashlib.md5(encoded)
    sha1 = hashlib.sha1(encoded)
    sha256 = hashlib.sha256(encoded)
    print("MD5(TEXT):", md5.hexdigest())
    print("SHA1(TEXT):", sha1.hexdigest())
    print("SHA256(TEXT):", sha256.hexdigest())

input()