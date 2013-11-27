class RSASign(object):
    def __init__(self, s, d, n):
        self.d = d
        self.socket = s
        self.n = n

    def hashed(self,msg):
        hashed = hashlib.sha256(msg).hexdigest()
        hashed_message=int(hashed,16)
        return hashed_message

    def sign(self, hashed):
        signed_message=pow(hash_m,d,n)
        return signed_message

    def sign_and_send(msg):
        hashed_message = self.hashed(msg)
        signed_message = self.sign(hashed_message)
        self.s.send(str(signed_message)+'@'+str(msg))


class RSAVerify(object):
    def __init__(self, s, e, N):
        self.e = e
        self.N = N
        self.s = s

    def verify(self, msg):
        pass

    def recv_and_verify():
        received_message = self.s.recv(1024)
        received_message = int(received_message)
        message = verify(received_message)
        return message
