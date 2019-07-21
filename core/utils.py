import base64
import re

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


class Crypto:
    def __init__(self, *args, **kwargs):
        self.key = ''
        self.message = ""
        self.serial = ''
        self.generate_key()
        if args:
            self.message = args[0]
        if kwargs:
            self.message = kwargs['message']

    def generate_key(self):
        password_provided = "Dw@6458995*#"  # This is input in the form of a string
        password = password_provided.encode()  # Convert to type bytes
        salt = b'6o4b1hv#(^00zyr$j&vb!*@cxt4ba)5i$(&(bs(jf24^xzag$_'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        self.key = base64.urlsafe_b64encode(kdf.derive(password))

    def encrypt(self, *args, **kwargs):
        f = Fernet(self.key)
        self.message = f.encrypt(self.message.encode('utf-8'))
        return self.message

    def decrypt(self, *args, **kwargs):
        f = Fernet(self.key)
        self.message = f.decrypt(self.message).decode('utf-8')
        return self.message

    def generate_serial(self, *args, **kwargs):
        if self.message:
            self.serial = re.sub('[^a-zA-Z0-9 \\\]', '', self.message.decode('utf-8'))[:20].upper()
        return self.serial[0:4] + '-' + self.serial[4:8] + '-' + self.serial[8:12] + '-' + self.serial[12:16] + '-' + self.serial[16:20]
