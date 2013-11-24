#!/usr/bin/env python
"""
Diffie-hellman user1
"""

import socket
import random
import itertools
new_range = lambda start, stop: iter(itertools.count(start).next, stop)

"""
Function to find the sqaure of a number
"""
def square(num_to_square):                                                          #  finding square
    squared = num_to_square*num_to_square
    return squared

"""
Function to find the modular exponential 
p = prime number
find=> (num^a)(mod p)
"""
def modfun(num,a,p):                                                                # modular exponentiation
     if a == 1 :
        return num%p
     else:
      if a%2 == 0:
         a=a/2
         return square(modfun(num,a,p))%p
      else:
         a=(a-1)/2
         return num*square(modfun(num,a,p))%p

"""
Function to find the generator of a given prime number
generator=> generator^((p-1)/2)(mod prime_num)
"""
def find_generator(prime_num):                                                      # finding the generator in the group 
    gen_p = (prime_num-1)/2;
    for generator in new_range(1,prime_num-1):
        y=modfun(generator,gen_p,prime_num);
        if(y==prime_num-1):
            return generator

"""
main function
"""
def main():                                                                             # main 
    
    host = ''
    port =5032# int(raw_input("Port number:"))
    backlog = 5
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(backlog)
    i=0
    while i<=0:
        client, address = s.accept()
        data_c1 = client.recv(size)
        prime_num=int(data_c1)
        print "Prime _number Received            :",prime_num                                                      # final modulus value

        generator=find_generator(prime_num)
        priv_key_of_current=random.randint(100000000000,9999999999999999999999999)
        key_by_current=modfun(generator,priv_key_of_current,prime_num)

        data_s1=str(key_by_current)
        if data_c1:
            client.send(data_s1)
            print "Key by current Send                 :",key_by_current
        data_c2=client.recv(size)
        key_from_other=int(data_c2)
        print "Key from other Received           :",key_from_other
        if data_c2:
            final_key_current=modfun(key_from_other,priv_key_of_current,prime_num)
            data_s2=str(final_key_current)
            client.send(data_s2)
            print "Final key from current Send         :",final_key_current
        data_c3=client.recv(size)
        final_key_other=int(data_c3)
        print "final key from other Received     :", final_key_other
        i=i+1
        client.close()
        if final_key_current==final_key_other:
            print "Key Exchange done!!!"
        else:
            print "Oops,Key exchange failed.\nTry again!"

if __name__ == "__main__":
    main()
