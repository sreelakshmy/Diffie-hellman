import os
import math
import socket
from Crypto.PublicKey import RSA
import hashlib
keyname='private_key.pem'
keydata = open(keyname, "r").read()
rsa = RSA.importKey(keydata)
host = 'localhost'
port = 50002
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

client, address = s.accept()
data_c1 = client.recv(size)


h="00aeb5f0d7a9ec2706d919dd3ab66bfc4c59108e12e2aee7f7854a17e03ac1288be0949af11e27341dc18e2724f6a1754143aaf2c3300873ea3278f9fa69a2280b94385282ee3fedf534db52001d8a3b0c1cebaa3fcefb462bef35120aa314cacf84744ae34eddaea1276934527ef8fb5cc5e585d7adef046eb05d508268fa4eaf"
n=int(h,16)
e=65537

si,msg=data_c1.split('@')


sig=int(si)
hashed_rec=int(pow(sig,e,n))

hash_msg=hashlib.sha256(msg).hexdigest()
hashed=int(hash_msg,16)

print "decr:",hashed_rec
print "hash:",hashed

if hashed_rec is hashed:
    print "valid."
else:
    print "invalid."
