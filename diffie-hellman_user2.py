#!/usr/bin/env python



import socket
import random
import itertools
new_range = lambda start, stop: iter(itertools.count(start).next, stop)


def square(num_to_square):                                                          #  finding square
    squared = num_to_square*num_to_square
    return squared

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

def find_generator(prime_num):                                                      # finding the generator in the group 
    gen_p = (prime_num-1)/2;
    for generator in new_range(1,prime_num-1):
        y=modfun(generator,gen_p,prime_num);
        if(y==prime_num-1):
            return generator

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

def main():                                                                             # main 
    
    prime_num= random.randint(100000000000,9999999999999999999999999)
    string_check=miller_rabins(prime_num)                                               # testing modulus value
    while True:
        if(string_check!='Prime'):
            prime_num= random.randint(100000000000,9999999999999999999999999)
        string_check=miller_rabins(prime_num)
        if(string_check=='Prime'):
            break
    host = 'localhost'
    port = 5011#int(raw_input("Port number:"))
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    data_c1=str(prime_num)
    generator=find_generator(prime_num)
    priv_key_of_user2=random.randint(100000000000,9999999999999999999999999)
    key_by_user2=modfun(generator,priv_key_of_user2,prime_num)
    data_c2=str(key_by_user2)
    s.send(data_c1)
    print "Prime number Send                    :",prime_num     # final modulus value
    data_s1 = s.recv(size)
    key_from_user1=int(data_s1)
    print "key from user1 Received              :", key_from_user1
    final_key_user2=modfun(key_from_user1,priv_key_of_user2,prime_num)
    if data_s1:
        s.send(data_c2)
        print "Key from user2 Send                  :",key_by_user2
    data_s2 = s.recv(size)
    final_key_user1=int(data_s2) 
    print "Final Key from user1 Received        :",final_key_user1
    data_c3=str(final_key_user2)
    if data_s2:
        s.send(data_c3)
        print "Final key from user2 Send            :",final_key_user2
    s.close()
    if final_key_user1==final_key_user2:
        print "Key Exchange done!!!"
    else:
        print "Oops,Key exchange failed.\nTry again!"


if __name__ == "__main__":
    main()
