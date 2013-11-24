Diffie-Hellman key exchange
============================

	also called exponential key exchange. It is a method of digital encryption that uses numbers raised to specific powers to produce decryption keys on the basis of components that are never directly transmitted, making the task of a would-be code breaker mathematically overwhelming.

Implement Diffie-Hellman:

	Two end users  :-
		    Alice and Bob communicating over a channel
            Mutually agree on positive whole numbers :-
			p and g, such that p is a prime number and g is a generator of p.
            Private key of Alice - a
			Privatekey of Bob    - b       (unknown to each)
	
	Alice :-	Xa = g^a mod p
	Bob   :-	Xb = g^b mod p
           
    Alice sends Xa to Bob
	Bob sends Xb to Alice
	
	Alice :-	key_Alice = Xb^a mod p
	Bob   :- 	key_Bob = Xa^b mod p

	Verification:
        Now, compare key_Alice and key_Bob
		If both are same then the key exchange is a success
