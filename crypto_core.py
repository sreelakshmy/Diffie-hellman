class RSASign(object):
    def __init__(self, s, d, n):
        self.d = d
        self.socket = s
        self.n = n
    
    def sign(self, msg):
	    hashed_message = self.calculate_hash(msg)
        signed_message=pow(hash_m,d,n)
        return signed_message

    def sign_and_send(msg):
        signed_message = self.sign(hashed_message)
        self.s.send(str(signed_message)+'@'+str(msg))


class RSAVerify(object):
    def __init__(self, s, e, N):
        self.e = e
        self.N = N
        self.s = s

    def verify(self, msg):
        rec_signed_msg,msg=data_c1.split('@')
	    rec_signed_message=int(rec_signed_message)
	    rec_hashed_message=int(pow(rec_signed_message,e,N))
	    decr_hashed_message = self.calculate_hash(msg)
	    if rec_hashed_message == decr_hashed:
	        flag=1
	    else:
	        flag=0
	    return flag

    def recv_and_verify():
        received_message = self.s.recv(1024)
        received_message = int(received_message)
        message = verify(received_message)
        if message==1:
            print "valid"
        else:
            print "invalid"
            exit()
        return message
    
