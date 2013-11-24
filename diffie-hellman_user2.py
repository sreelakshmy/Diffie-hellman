#!/usr/bin/env python
"""
Diffie-hellman user2
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
Finding if the genreated random number is prime or not
Miller rabbins test :n=prime_number-1
"""
def miller_rabins(prime_num):                                                           #primality testing
    n = prime_num - 1
    k = 0
    quotient = n
    reminder = 0
    while reminder == 0:
        quotient, reminder = divmod(quotient, 2)
        k += 1
    k -= 1
    m = quotient * 2 + reminder
    if (prime_num==1) or (prime_num==2) or (prime_num==3):
        print "Prime"
        exit()

    for i in range(10):
        check = random.randint(2, n - 1)
        t = modfun(check, m, prime_num)
        if t == 1 or t == n:
           continue
        for i in range(k - 1):
           t = modfun(t, 2, prime_num)
           if t == 1:
               string_check="Composite"
               return string_check
           if t == n:
               break
        if t != n:
            string_check="Composite"
            return string_check  
    string_check="Prime"
    return string_check

"""
Function to generate a number and calling primality test function
"""
def _random():										# creating prime number
    prime_num= random.randint(100000000000,9999999999999999999999999)
    string_check=miller_rabins(prime_num)                                               # testing modulus value
    while True:
        if(string_check!='Prime'):
            prime_num= random.randint(100000000000,9999999999999999999999999)
        string_check=miller_rabins(prime_num)
        if(string_check=='Prime'):
            break
    return prime_num
"""
main function
"""
def main():                                                                             # main 
    #prime number after the checking
    prime_num=_random()
    
    #Networking
    
    host = 'localhost'
    port = 5032
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
