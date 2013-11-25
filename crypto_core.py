class RSASign(object):
    def __init__(self, s, d):
        self.d = d
        self.socket = s

    def sign(self, msg):
        pass

    def sign_and_send(msg):
        signed_message = self.sign(msg)
        self.s.send(str(signed_message))

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
