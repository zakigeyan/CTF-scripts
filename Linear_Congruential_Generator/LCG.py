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
    def __init__(self, modulus, states):
        self.modulus = modulus
        assert len(states) >= 3, 'insufficient states'
        self.states = states
        self.a = (self.states[2] - self.states[1]) * int(inverse(self.states[1] - self.states[0], self.modulus)) % self.modulus
        self.c = (self.states[1] - self.states[0] * self.a) % self.modulus
    def genPrevState(self):
        self.states.insert(0, (self.states[0] - self.c) * inverse(self.a, self.modulus) % self.modulus)
    def genNextState(self):
        self.states.append((self.a * self.states[-1] + self.c) % self.modulus)
    def getStates():
        return self.states
