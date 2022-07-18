import socket
import webbrowser
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostbyname_ex(socket.gethostname())[-1][-1], 1234))

server.listen()

while True:
	user, address = server.accept()

	while True:
		data = user.recv(1024).decode("utf-8").lower()
		print(data)

		if data == "youtube":
			webbrowser.open("https://www.youtube.com")
		elif data == "chrome":
			webbrowser.open("https://www.google.com")
		elif data == "vk":
			webbrowser.open("https://www.vk.com")
		elif data == "music":
			webbrowser.open("https://www.music.yandex.ru/home")

		elif data == "steam":
			os.startfile("D:/Program Files/Steam/steam.exe")

