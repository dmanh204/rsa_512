from Karatsuba import Karatsuba
def compmod(a,b,n):	#Tinh a^b mod n
    bi = str(bin(b))
    l = len(bi)-1
    c = 0
    f = 1
    while (l>0):	#Lay list cac bit cua b
        c = 2*c
        f = Karatsuba(f,f)%n        
        if bi[l] == '1':
            c = c+1    
            f = Karatsuba(f,a)%n
        l = l-1
    #Tinh toan
    return f
#Ma hoa
def rsa(mes, key, n):
    ret = compmod(mes, key, n)
    return ret
#Giai ma
def de_rsa(mes, key, n):
    ret = compmod(mes, key, n)
    return ret
#Doc tu string 1 so hex
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

phi = Karatsuba(q-1, p-1)
n = Karatsuba(q,p)
with open ("Mes.txt", "r") as f:
    m = rdnum16(f.readline())

encr = compmod(m,e,n)
decr = compmod(encr,d,n)

with open ("Result.txt", "w") as f:
    f.write(str(hex(encr))+"/n")
    f.write(str(hex(decr))+"/n")