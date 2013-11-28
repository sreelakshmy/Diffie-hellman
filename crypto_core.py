from common import calculate_hash

DELIM="\n"

from sage.all import *

class RSASign(object):
    """
    Class that manages the sending of signed data over
    the wire
    """
    def __init__(self, s, d, N):
        self.socket = s
        self.d = Integer(d)
        self.N = Integer(N)

    def sign(self, msg):
        # Calculate the hash
        hashed_message = Integer(calculate_hash(msg))
        # Calculate the signature of the hash and return
        signed_message=power_mod(hashed_message,self.d,self.N)
        return signed_message

    def sign_and_send(msg):
        # Calculate the signature of the hash and send over the
        # network
        signed_message = self.sign(msg)
        self.s.send(str(signed_message)+'@'+str(msg)+DELIM)


class RSAVerify(object):
    """
    Class that manages the verification of messages received
    over the wire
    """
    def __init__(self, s, e, N):
        self.s = s
        self.e = Integer(e)
        self.N = Integer(N)

    def verify(self, msg):
        # Split the message to get the signature and the message
        signed_hash, msg = msg.split('@')
        signed_hash      = Integer(signed_hash)
        # Recalculate the hash of the message
        recalculated_hash = Integer(calculate_hash(msg))
        # Recompute the hash from the signed hash
        retrieved_hash = power_mod(signed_hash, self.e, self.N)

        # Compare the recomputed hash with the recalculated hash
        if retrieved_hash != recalculated_hash:
            return False
        return msg

    def recv_and_verify():
        # Receive the message and verify it
        received_message = self.s.recv(1024).strip()
        received_message = int(received_message)
        message = verify(received_message)
        return message
