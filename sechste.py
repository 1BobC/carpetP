# Ch 12 Networked programs
#Support code for Sockets in Python

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))