from Crypto.PublicKey import RSA
bits=1024
new_key = RSA.generate(bits) 
public_key = new_key.publickey().exportKey("PEM") 
private_key = new_key.exportKey("PEM") 
f=open('file1.txt', "w")
f.write(private_key)
f1=open('file.txt','w')
f1.write(public_key)
