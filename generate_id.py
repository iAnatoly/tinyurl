from hashlib import sha256
from base64 import b64encode

class ID:
    _ctr = 0
    @staticmethod
    def generate(text, length=10):
        digest = sha256(bytes("{0}-{1}".format(ID._ctr,text),"utf-8"))
        ID._ctr += 1
        digest_b64 = b64encode(digest.digest())
        digest_b58 = str(digest_b64.translate(None, b"lIO0+/="),"utf-8")
        if len(digest_b58)<length:
            raise Exception("ID length exhausted")
        return digest_b58[:length]
