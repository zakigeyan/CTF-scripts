from Crypto.Util.number import getPrime, isPrime
from Crypto.Random.random import randrange
from gmpy2 import isqrt, is_square, next_prime

def FermatFactor(N):
    '''
    https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
    '''
    a = isqrt(N + 1)
    b = a*a - N
    while not is_square(b):
        b += 2*a + 1
        a += 1
    p = a - isqrt(b)
    q = a + isqrt(b)
    return [p, q]

def testFermat(num=10):
    for i in range(num):
        p0 = getPrime(512)
        q0 = next_prime(p0)
        for j in range(randrange(2, 30)):
            q0 = next_prime(q0)
        N = p0 * q0
        p1, q1 = FermatFactor(N)
        assert isPrime(p1) and N % p1 == 0
        assert isPrime(q1) and N % q1 == 0
