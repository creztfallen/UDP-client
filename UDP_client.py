import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket client successfully creeated.')

host = 'localhost'
port = 5433
message = 'Hello, server! How you doing?'

try:
    print('Client:' + message)
    s.sendto(message.encode(), (host, 5432))
    
    data, server = s.recvfrom(4096)
    data = data.decode()
    print("Client: " + data)
finally:
    print("Client: Closing the connection")
    s.close()     
