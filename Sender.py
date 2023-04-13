import RSA
import socket
KEY_SIZE = 512

p, q, n, phi, e, d = RSA.generate_key(KEY_SIZE)

# next create a socket object
s = socket.socket()		
port = 5			
s.bind(('', port))		
print ("socket binded to %s" %(port))
s.listen(5)	
print ("socket is listening")	
c, addr = s.accept()	
print ('Got connection from', addr )

print('Receiving their public key')
e2 = int(c.recv(1024).decode())
c.send(str(e).encode())
n2 = int(c.recv(1024).decode())
c.send(str(n).encode())


print ('Type \'end\' to end connection at any time')	
while True:
    pt = input()
    ct = RSA.cipher(pt, e2, n2)
    c.send(str(len(ct)).encode())
    c.recv(1024)
    for x in ct:
        c.send(str(x).encode())
        c.recv(1024)
    if(pt == 'end'):
        c.close()
        break