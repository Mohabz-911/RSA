import math
import matplotlib.pyplot as plt
import RSA
import time

KEY_SIZE = 14
pt = 'mohab'
ct = []
keys = []
attack_times = []
en_times = []

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
    if(math.gcd(e, phi) == 1):
        d = pow(e, -1, phi)
        pt2 = RSA.decipher(ct, d, n)
        if pt2 == pt:
            return d
    return -1

#Main routine
k = KEY_SIZE
while k <= 32:
    print("ATTACK at key-size = ", k, ':')
    keys.append(k)
    p, q, n, phi, e, d = RSA.generate_key(k)
    start_time = round(time.time() * 1000)
    ct = RSA.cipher(pt, e, n)
    end_time = round(time.time() * 1000)
    en_times.append((end_time-start_time)/1000)
    start_time = round(time.time() * 1000)
    d2 = attack(e, n)
    end_time = round(time.time() * 1000)
    attack_times.append((end_time-start_time)/1000)
    if d2 == d:
        print("SUCCEEDED")
        print("Private Key = ", d2)
        print('Time = ', (end_time-start_time)/1000)
    else:
        print("FAILED")
    k += 1

figure, axis = plt.subplots(2,1)
axis[0].plot(keys, attack_times, c = 'r')
axis[1].plot(keys, en_times, c = 'b')
plt.show()