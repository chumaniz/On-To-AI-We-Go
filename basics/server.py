import socket

s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

s.bind(("127.0.0.1", 9999))
s.listen()

print("Shut the fuck I'm listening...")

while True:
    client, address = s.accept()
    print("Connected to {}".format(address))
    message = "Hallo Jou Ma Se Doos!"

    client.send(message.encode('ascii'))
    client.close()