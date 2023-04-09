import RSA

plaintext = "mohabfathisalemku"
p, q, n, phi, e, d = RSA.generate_key()
c = RSA.cipher(plaintext, e, n)
back = RSA.decipher(c, d, n)

print(back)