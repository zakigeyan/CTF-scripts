p = GF(random_prime(2^64))
g = p.primitive_element()
for _ in range(10):
    a = p.random_element() # randint(2, p-2)
    A = g^a # pow(g, a, p)
    assert A.log(g) == a # k(A).log(k(g))
