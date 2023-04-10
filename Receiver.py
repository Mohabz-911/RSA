import RSA
# Import socket module
import socket			

p, q, n, phi, e, d = RSA.generate_key()

# Create a socket object
s = socket.socket()		
# Define the port on which you want to connect
port = 5
# connect to the server on local computer
s.connect(('127.0.0.1', port))

s.send(str(e).encode())
e2 = int(s.recv(1024).decode())
s.send(str(n).encode())
n2 = int(s.recv(1024).decode())


while True:
    cipher_arr = []
    message_length = int(s.recv(2048).decode())
    s.send('Ack'.encode())
    for x in range(0, message_length):
        ct = int(s.recv(1024).decode())
        cipher_arr.append(ct)
        s.send('Ack'.encode())
    pt = RSA.decipher(cipher_arr, d, n)
    if(pt == 'end  '):
        s.close()
        break	
    print(pt)