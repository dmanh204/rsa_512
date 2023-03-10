import random
from Karatsuba import *
def miller_rabin(n, a): # odd number only
#find k and q
    q = n-1	
    k = 0
    while(q%2 == 0):
        k += 1
        q //= 2
#testing
    v = pow(a, q, n)
    if v == 1 or v == -1:
        return True
    for i in range(k-1):
        v = pow(v,2, n)
        if v == n-1:
            return True
    return False

def primetest(n):

    low_primes = [
        2,
        3,
        5,
        7,
        11,
        13,
        17,
        19,
        23,
        29,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
        127,
        131,
        137,
        139,
        149,
        151,
        157,
        163,
        167,
        173,
        179,
        181,
        191,
        193,
        197,
        199,
        211,
        223,
        227,
        229,
        233,
        239,
        241,
        251,
        257,
        263,
        269,
        271,
        277,
        281,
        283,
        293,
        307,
        311,
        313,
        317,
        331,
        337,
        347,
        349,
        353,
        359,
        367,
        373,
        379,
        383,
        389,
        397,
        401,
        409,
        419,
        421,
        431,
        433,
        439,
        443,
        449,
        457,
        461,
        463,
        467,
        479,
        487,
        491,
        499,
        503,
        509,
        521,
        523,
        541,
        547,
        557,
        563,
        569,
        571,
        577,
        587,
        593,
        599,
        601,
        607,
        613,
        617,
        619,
        631,
        641,
        643,
        647,
        653,
        659,
        661,
        673,
        677,
        683,
        691,
        701,
        709,
        719,
        727,
        733,
        739,
        743,
        751,
        757,
        761,
        769,
        773,
        787,
        797,
        809,
        811,
        821,
        823,
        827,
        829,
        839,
        853,
        857,
        859,
        863,
        877,
        881,
        883,
        887,
        907,
        911,
        919,
        929,
        937,
        941,
        947,
        953,
        967,
        971,
        977,
        983,
        991,
        997,
    ]
    if n in low_primes:
        return True
    if n %2 == 0:
        return False
    # very large number
    for i in range(40):
        a = random.randrange(2,n-1)
        if miller_rabin(n,a) == False:
            return False
        else:
            continue
    return True
inp = int(input("Nhap so bit cua so prime can tao: "))
# Tim so i
while(1):
    i = random.randrange(pow(2,inp),pow(2,inp+1))
    if primetest(i) == True:
        break
    else:
        continue
print(primetest(i))
# Tim so y
while(1):
    y = random.randrange(pow(2,inp),pow(2,inp+1))
    if (y == i):
        continue
    if (primetest(y)== True):
        break
    else:
        continue
print(primetest(y))
with open("PaQ.txt", "w") as f:
    f.write(str(hex(i))+"\n")
    f.write(str(hex(y))+"\n")
    f.write(str(hex(Karatsuba(i,y)))+"\n")
print("Done!")

