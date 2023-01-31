import random

from params import p
from params import g

def keygen():

    #calc q based on p
    q = (p - 1) / 2

    sk = random.randint(1, q)

    pk = pow(g, sk, p)
    return pk,sk

def encrypt(pk,m):

    #calc q based on p
    q = (p - 1) / 2

    a = random.randint(1, q)

    c1 = pow(g, a, p)
    c2 = pow(pk, a, p) * m % p

    return [c1,c2]

def decrypt(sk,c):
    m = ((c[1] % p) * pow(c[0], -sk, p)) % p
    return m

