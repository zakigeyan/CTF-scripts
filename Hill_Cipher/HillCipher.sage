import string
import sys

def decryptHillCipher(ct, key):
    poss = string.lowercase
    size = int(sqrt(len(key)))
    assert len(ct) % size == 0
    ct_list = [poss.index(i) for i in ct]
    ct_list = [ct_list[i:i+size] for i in range(0, len(ct_list), size)]
    key_list = [poss.index(i) for i in key]
    key_list = [key_list[i:i+size] for i in range(0, len(key_list), size)]
    A = matrix(Zmod(26), key_list)
    pt = ''
    for i in ct_list:
        B = vector(Zmod(26), i)
        X = A.solve_right(B)
        pt += ''.join(poss[j] for j in X)
    return pt

def encryptHillCipher(pt, key, pad='z'):
    poss = string.lowercase
    size = int(sqrt(len(key)))
    if len(pt) % size:
        pt += pad * (size - (len(pt) % size))
    assert len(pt) % size == 0
    pt_list = [poss.index(i) for i in pt]
    pt_list = [pt_list[i:i+size] for i in range(0, len(pt_list), size)]
    key_list = [poss.index(i) for i in key]
    key_list = [key_list[i:i+size] for i in range(0, len(key_list), size)]
    A = matrix(Zmod(26), key_list)
    ct = ''
    for i in pt_list:
        B = vector(Zmod(26), i)
        X = A * B
        ct += ''.join(poss[j] for j in X)
    return ct

def testHillCipher():
    key = 'abljhfzbo' # 3x3
    pt = 'hillcipherimplementation'
    ct = encryptHillCipher(pt, key)
    assert pt == decryptHillCipher(ct, key)
