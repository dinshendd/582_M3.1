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
    c1 = 0
    c2 = 0
    return [c1,c2]

def decrypt(sk,c):
    m = 0
    return m

