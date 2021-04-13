from functools import reduce

def LagrangePolynomial(points, prime):
    F = FiniteField(prime)
    P = F['x']
    points = [(F(x), F(y)) for x, y in points]
    coefs = P.lagrange_polynomial(points)
    return coefs.coefficients()[::-1]

def testLagrange(num=10):
    number_of_coefs = 32
    for t in range(num):
        prime = random_prime(2^512)
        coefs0 = [randint(1, prime-1) for _ in range(number_of_coefs)]
        points = []
        for _ in range(number_of_coefs):
            x0 = randint(1, prime-1)
            y0 = (reduce(lambda a, c: a * x0 + c, coefs0)) % prime
            points.append((x0, y0))
        coefs1 = LagrangePolynomial(points, prime)
        assert coefs0 == coefs1
