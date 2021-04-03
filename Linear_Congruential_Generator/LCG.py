#!/usr/bin/python
from Crypto.Util.number import *
from Crypto.Random.random import randrange

class LCG:
    def __init__(self, modulus, a, c, seed):
        self.modulus = modulus
        self.a = a
        self.c = c
        self.seed = seed
    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.modulus
        return self.seed

class CrackLCG:
    def __init__(self, states):
        self.states = states
        diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
        zeros = [t2 * t0 - t1 * t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
        self.modulus = zeros[0]
        for i in zeros[1:]:
            self.modulus = GCD(self.modulus, i)
        self.a = (self.states[2] - self.states[1]) * int(inverse(self.states[1] - self.states[0], self.modulus)) % self.modulus
        self.c = (self.states[1] - self.states[0] * self.a) % self.modulus
    def genPrevState(self):
        self.states.insert(0, (self.states[0] - self.c) * inverse(self.a, self.modulus) % self.modulus)
    def genNextState(self):
        self.states.append((self.a * self.states[-1] + self.c) % self.modulus)
    def getStates(self):
        return self.states

def testLCG(num=10):
    mod = getPrime(64)
    a = randrange(1, mod-1)
    c = randrange(1, mod-1)
    seed = randrange(1, mod-1)
    L = LCG(mod, a, c, seed)
    states = [L.next() for _ in range(num)]
    CL = CrackLCG(states)
    for _ in range(num):
        CL.genNextState()
        states.append(L.next())
    assert CL.getStates() == states
