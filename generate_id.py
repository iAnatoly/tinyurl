from hashlib import sha256
from base64 import b64encode

class ID:
    @staticmethod
    def generate(text, length=1):
        digest = sha256(bytes(text,"utf-8"))
        digest_b64 = b64encode(digest.digest())
        digest_b58 = str(digest_b64.translate(None, b"lIO0+/="),"utf-8")
        if len(digest_b58)<length:
            raise Exception("ID length exhausted")

        print(digest_b58)
        return digest_b58[:length]