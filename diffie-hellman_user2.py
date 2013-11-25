#!/usr/bin/env python
"""
Diffie-hellman user2
"""


import socket
import random
from common import *
import ConfigParser
"""
main function
"""
def main():                                                                             # main 
    #prime number after the checking
    config = ConfigParser.ConfigParser()
    config.read('config.cfg')
    host = config.get('networking', 'ip')
    port = int(config.get('networking', 'port'))
 
    prime_num=generate_random()
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    data_c1=str(prime_num)

    generator=find_generator(prime_num)
    priv_key_of_current=random.randint(100000000000,9999999999999999999999999)
    key_by_current=modfun(generator,priv_key_of_current,prime_num)

    data_c2=str(key_by_current)
    s.send(data_c1)
    print "Prime number Send                    :",prime_num                            
    data_s1 = s.recv(size)
    key_from_other=int(data_s1)
    print "key from other Received              :", key_from_other
    
    final_key_current=modfun(key_from_other,priv_key_of_current,prime_num)
    
    if data_s1:
        s.send(data_c2)
        print "Key from current Send                  :",key_by_current
    data_s2 = s.recv(size)
    final_key_other=int(data_s2) 
    print "Final Key from other Received        :",final_key_other
    data_c3=str(final_key_current)
    if data_s2:
        s.send(data_c3)
        print "Final key from current Send            :",final_key_current
    s.close()
    if final_key_other==final_key_current:
        print "Key Exchange done!!!"
    else:
        print "Oops,Key exchange failed.\nTry again!"


if __name__ == "__main__":
    main()
