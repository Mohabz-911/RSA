import math
import random
from Crypto.Util import number
base = 37


#Divides the input message into packets (5 characters each)
def divide_text(message):
    out = []
    for i in range(0, len(message), 5):
        out.append(message[i:i+5])
    while(len(out[len(out)-1]) < 5):
        out[len(out)-1] += ' '
    return out

#Encode each packet
def encrypt_message(packet):
    multiplicand = int(base**4)
    sum = 0
    for c in packet:
        if(c <= '9' and c >= '0'):
            c = ord(c) - ord('0')
        elif(c >= 'a' and c <= 'z'):
            c = ord(c) - ord('a') + 10
        else:
            c = 36
        sum += multiplicand*int(c)
        multiplicand /= base
    
    return int(sum)

#Decodes each packet
def decrypt_message(code):
    str1 = ''
    out = []
    for i in range(0,5,1):
        d = int(code % base)
        if(d <= 9 and d >= 0):
            d = chr(d + ord('0'))
        elif(d >= 10 and d <= 35):
            d = chr(d - 10 + ord('a'))
        else:
            d = ' '
        code -= code % base
        code /= base
        out.append(d)
    out.reverse()
    return str1.join(out)

#The higher level function that ciphers the input message
def encode(message):
    encoded_message = []
    packets = divide_text(message)
    for p in packets:
        encoded_message.append(encrypt_message(p))
    return encoded_message

#The higher level function that deciphers the ciphertext
def decode(encoded_message):
    message = ''
    for ct in encoded_message:
        message = message + decrypt_message(ct)
    return message

def generate_key():
    p = number.getPrime(512)
    q = number.getPrime(512)
    n = p * q
    phi = (p-1)*(q-1)
    e = number.getPrime(512)
    while math.gcd(e,phi) != 1:
        e = number.getPrime(512)
    d = pow(e, -1, phi)

    return p, q, n, phi, e, d

def cipher(plaintext, e, n):
    m_arr = encode(plaintext)
    c = []
    for x in m_arr:
        c.append(pow(x, e, n))
    return c

def decipher(ciphertext, d, n):
    codes = []
    for x in ciphertext:
        codes.append(pow(x, d, n))
    out = decode(codes)

    return out

# plaintext = "mohabfathisalemku"
# p, q, n, phi, e, d = generate_key()
# c = cipher(plaintext)
# back = decipher(c)

# print(back)