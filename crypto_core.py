
from common import *
DELIM="\n"
class RSASign(object):
    def __init__(self, s, d, n):
        self.d = d
        self.socket = s
        self.n = n
    
    def sign(self, msg):
	hashed_message = calculate_hash(msg)
        signed_message=pow(hash_message,d,n)
        return signed_message

    def sign_and_send(msg):
        signed_message = self.sign(msg)
        self.s.send(str(signed_message)+'@'+str(msg)+DELIM)


class RSAVerify(object):
    def __init__(self, s, e, N):
        self.e = e
        self.N = N
        self.s = s

    def verify(self, msg):
            rec_signed_msg,rec_msg=msg.split('@')
	    rec_signed_message=int(rec_signed_msg)
	    rec_hashed_message=int(pow(rec_signed_message,e,N))
	    decr_hashed_message = int(calculate_hash(rec_msg),16)
	    if rec_hashed_message == decr_hashed:
	        return rec_msg
	    else:
	        exit()

    def recv_and_verify():
        received_message = self.s.recv(1024)
        received_message = int(received_message)
        message = verify(received_message)
        return message
    
