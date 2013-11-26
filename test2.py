import os
#from sage.all import*
#import binascii
#from binascii import unhexlify
import math
import socket
from Crypto.PublicKey import RSA
import hashlib
keyname='file1.txt'
keydata = open(keyname, "r").read()
rsa = RSA.importKey(keydata)
secret = "abcd"
hashed = hashlib.sha256(secret).hexdigest()
hash1=int(hashed,16)
print "hashed",hash1
signature=rsa.sign(hash1,"")
sign=str(signature)
sign=sign.replace("(","")
sign=sign.replace("L,)","")
#print "sign",sign
data1=str(sign)+str('@')+str(secret)
#print data1
#pubfile='id_rsa1.pub'
#keydata = open(pubfile, "r").read()
#pubrsa = RSA.importKey(keydata)
#print "public key",pubrsa
h="00bb9ae3a7a690f82250982d6ee40d82b1a34098657dda166e190739e421b2b1ece4602662074ce52e6543c073ee3ec36db053e5fe171446cd13266d52e2891aa94f38f4537cd94e38b2fc697eacadf4fdbcca24aa747ed00bec235d6a3d6211a9966a52e1e3ec04e02f051675e3de253ff3a7ecca517faf087f4dd90404728649"
n=int(h,16)
e=10001
si,msg=data1.split('@')
#print "si",si
#print "msg",msg
sig=int(si,16)
#print sig
hashed_rec=pow(sig,e,n)
print "hashed2:",hashed_rec
