#!/usr/bin/env python

import socket
import random
import common
import ConfigParser

from crypto_core import RSASign, RSAVerify

def main():
    general_config = ConfigParser.ConfigParser()
    config = ConfigParser.ConfigParser()

    general_config.read('config.cfg')
    config.read('config_user2.cfg')
    host = general_config.get('networking', 'ip')
    port = int(general_config.get('networking', 'port'))
    lower_range_DH = int(general_config.get('crypto', 'lower_range_DH'))
    upper_range_DH = int(general_config.get('crypto', 'upper_range_DH'))

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))

    other_N, other_e = config.get('crypto_user1', 'N'), config.get('crypto_user1', 'e')
    other_N, other_e = int(other_N), int(other_e)

    N = config.get('crypto_user2', 'N')
    e = config.get('crypto_user2', 'e')
    d = config.get('crypto_user2', 'd')
    p = config.get('crypto_user2', 'p')
    q = config.get('crypto_user2', 'q')

    signer = RSASign(s, d, N)
    verifier = RSAVerify(s, other_e, other_N)

    DH_prime = common.generate_random()
    generator = common.find_generator(DH_prime)
    signer.sign_and_send(DH_prime)

    x2 = random.randint(lower_range_DH, upper_range_DH)
    y2 = common.modfun(generator, x2, DH_prime)
    signer.sign_and_send(y2)

    y1 = verifier.recv_and_verify()
    y12 = common.modfun(y1, x2, DH_prime)

    print "[+] Negotiated session key", y12


if __name__ == "__main__":
    main()
