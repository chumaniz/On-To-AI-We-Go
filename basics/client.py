import socket

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

try:
    s.connect(("127.0.0.1", 9999))

    message = s.recv(1024)

    s.close()

    print(message.decode('ascii'))
except ConnectionRefusedError:
    print("Heyyi, jou voken naar, sien jy nou nie dat ek slaap nie?! Vok man!!")

