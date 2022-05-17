# Ch 12 Networked programs
#Support code for Sockets in Python

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80))
#so far this code has "rung the 'phone"
#Now think about what type of data to send and what type of data will be received?
#The application protocol might be:www, Mail, Login, RSS etc.
#protocol http://, host www.dr-chuck.com, document page1.htm.
#see http://www.youtube.com/watch?v=x2GyIlq59rl  1-17 to 2-19
#6:37:32 continue


