from Karatsuba import Karatsuba
import random
def rdnum16(a):
    ret =""
    for i in a: #Tao string chua cac ki tu so
        if (i.isalnum()):
            ret+=i
        else:
            break
    return int(ret,16)
#Doc tu file 1 so dec
def rdnum10(a):
    ret =""
    for i in a:
        if (i.isnumeric()):
            ret+=i
        else:
            break
    return int(ret)
with open ("PaQ.txt", "r") as f:
    p = rdnum16(f.readline())
    q = rdnum16(f.readline())

with open ("Caccapkey.txt", "r") as f:
    e = rdnum10(f.readline())
    d = rdnum10(f.readline())
'''
phi = Karatsuba(q-1, p-1)
n = Karatsuba(q,p)
x = Karatsuba(e,d)%phi



# cap e va d la dung
def compmod(a,b,n):	#Tinh a^b mod n
    bi = str(bin(b))
    l = len(bi)
    c = 0
    f = 1
    for i in range(l):	#Lay list cac bit cua b
        c = 2*c
        f = Karatsuba(f,f)%n        
        if bi[i] == '1':
            c = c+1    
            f = Karatsuba(f,a)%n
    return f

a = compmod(123, 17, 3233)
b = compmod(a, 2753, 3233)

c = pow(123,e,n)
d = pow(c, d, n)
#print(a, b)
print(hex(c))
print(hex(d))
#Thuat toan nhan sai'''
def miller_rabin(n, a): # odd number only
#find k and q
    q = n-1 
    k = 0
    while(q%2 == 0):
        k += 1
        q //= 2
#testing
    v = pow(a, q, n)
    if v == 1 | v == -1:
        return True
    for _ in range(k-1):
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
    a = random.randrange(2,n-1)
    for _ in range(100):
        if miller_rabin(n,a) == False:
            return False
    return True
print(primetest(q))
print(primetest(p))