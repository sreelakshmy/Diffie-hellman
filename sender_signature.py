import os
import math
import socket
from Crypto.PublicKey import RSA
import hashlib
keyname='private_key.pem'
keydata = open(keyname, "r").read()
rsa = RSA.importKey(keydata)
secret = "abcd"
hashed = hashlib.sha256(secret).hexdigest()
hash1=int(hashed,16)
print "hashed :"
print hash1
signature=rsa.sign(hash1,"")
for x in signature:
    sig=x
    break
sign=str(sig)
data1=str(sign)+str('@')+str(secret)
host = 'localhost'
port = 50002
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
s.send(data1)
