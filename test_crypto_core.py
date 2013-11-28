from crypto_core import RSASign, RSAVerify
from sage.all import *



def test_sign_and_verify():
    # Setting up the RSA cryptosystem for the test
    p = random_prime(2**512)
    q = random_prime(2**512)
    n = Integer(p * q)
    phi = (p - 1)*(q - 1)
    e = Integer(65537)
    bezout = xgcd(e, phi);
    d = Integer(mod(bezout[1], phi))
    assert mod(d * e, phi) == 1

    # First create an instance of RSASign
    signer = RSASign(None, d, n)

    # Then sign a message
    signed_message = signer.sign("blah")

    # Craft the final message
    final_message = str(signed_message) + "@" + "blah"

    # Verify the final message
    verifier = RSAVerify(None, e, n)
    if not verifier.verify(final_message):
        print "Message has been tampered with, unable to validate"
    else:
        print "Message validated"

if __name__ == '__main__':
    test_sign_and_verify()
