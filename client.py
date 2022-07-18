import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234))

while True:
	client.send(input().encode("utf-8"))