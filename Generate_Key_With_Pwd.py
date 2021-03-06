import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import time

plaintxt_pass = raw_input("Enter the password you want for the key: ")
encoded_pass = plaintxt_pass.encode()

#salt = Add your own salt by using os.urandom(any number)
kdf = PBKDF2HMAC(
	algorithm = hashes.SHA256(),
	length = 32,
	salt = salt,
	iterations = 100000,
	backend = default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(encoded_pass))
time.sleep(1)
print"\n"
print(key)
time.sleep(1)

file = open("key.key", "wb")
file.write(key)
file.close()
os.path.abspath("key.key")

print("Your key has been created and saved to " + os.path.abspath("key.key") + " Do not rename the key. Also remember to keep the key in a safe place...\n")
