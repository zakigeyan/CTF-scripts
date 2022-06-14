#!/usr/bin/python
from Crypto.Util.number import *
from Crypto.Random.random import randrange

class LCG:
    def __init__(self, m, a, c, seed):
        self.m = m
        self.a = a
        self.c = c
        self.seed = seed
    def next(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

class CrackLCG:
    def __init__(self, states):
        self.states = states
        diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
        zeros = [t2 * t0 - t1 * t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
        self.m = zeros[0]
        for i in zeros[1:]: self.m = GCD(self.m, i)
        self.a = (self.states[2] - self.states[1]) * int(inverse(self.states[1] - self.states[0], self.m)) % self.m
        self.c = (self.states[1] - self.states[0] * self.a) % self.m
    def genPrevState(self):
        self.states.insert(0, (self.states[0] - self.c) * inverse(self.a, self.m) % self.m)
    def genNextState(self):
        self.states.append((self.a * self.states[-1] + self.c) % self.m)
    def getStates(self):
        return self.states

def testLCG(num=10):
    # generate states
    m = getPrime(64)
    a = randrange(1, m-1)
    c = randrange(1, m-1)
    seed = randrange(1, m-1)
    L = LCG(m, a, c, seed)
    states = [L.next() for _ in range(num)]

    # crack LCG and generate some new states
    CL = CrackLCG(states)
    for _ in range(num):
        CL.genNextState()
        states.append(L.next())
    assert CL.a == a
    assert CL.m == m
    assert CL.c == c
    assert CL.states == states
