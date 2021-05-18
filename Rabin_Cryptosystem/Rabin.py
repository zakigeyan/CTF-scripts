from Crypto.Util.number import bytes_to_long, getPrime

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

class Rabin():
    def __init__(self, size):
        p = self.get_prime(size//2)
        q = self.get_prime(size//2)
        self.private, self.public = (p, q), p * q

    def get_prime(self, size):
        while True:
            p = getPrime(size)
            if p % 4 == 3:
                return p

    def decrypt(self, c):
        p, q = self.private
        mp = pow(c, (p+1)//4, p)
        mq = pow(c, (q+1)//4, q)
        _, yp, yq = egcd(p, q)
        r = (yp * p * mq + yq * q * mp) % self.public
        s = (yp * p * mq - yq * q * mp) % self.public
        return list(map(int, [r, s, self.public - r, self.public - s]))

    def encrypt(self, m):
        return pow(m, 2, self.public)

def test():
    rabin = Rabin(1024)
    m = bytes_to_long('deomkicer')
    enc = rabin.encrypt(m)
    dec = rabin.decrypt(enc)
    assert m in dec
