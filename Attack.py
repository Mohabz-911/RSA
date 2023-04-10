import math
import RSA
import time

KEY_SIZE = 14
pt = 'mohab'
ct = []

def prime_factorize(n):
    p = int(math.sqrt(n))
    while(p != 0):
        if(n%p == 0):
            return p, n//p
        p -= 1
    return -1, -1

def attack(e, n):
    p, q = prime_factorize(n)
    phi = (p-1)*(q-1)
    e = 2
    while(e < phi):
        if(math.gcd(e, phi) == 1):
            d = pow(e, -1, phi)
            pt2 = RSA.decipher(ct, d, n)
            if pt2 == pt:
                return d
        e += 1
    return -1

p, q, n, phi, e, d = RSA.generate_key(KEY_SIZE)
print(p, q, n)
ct = RSA.cipher(pt, e, n)
start_time = round(time.time() * 1000)
d2 = attack(e, n)
end_time = round(time.time() * 1000)
if d2 == d:
    print("Private Key = ", d2)
    print('Time = ', (end_time-start_time)/1000)
    print("SUCCESSFUL ATTACK")