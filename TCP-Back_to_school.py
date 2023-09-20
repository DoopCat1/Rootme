import socket
import re
from math import sqrt


#Connecting to server
server_address = ('challenge01.root-me.org', 52002)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)

def math_calc(msg):     #Using regex search the number in specific, and calculate the numbers. After send result to the sender function.
	f_value = re.search('(?<=root of )(\w+)',msg)
	f_value = f_value.group()
	s_value = re.search('(?<=multiply by )(\w+)',msg)  
	s_value = s_value.group()

	square = int(f_value)
	multi = sqrt(square) * int(s_value)
	multi = round(multi,2)
	multi = str(multi).encode()
	send_msg(multi)


def send_msg(msg):     #Only send the specific message and print data from server. 
	s.sendall(msg)
	s.shutdown(socket.SHUT_WR)
	while 1:
	    data = s.recv(1024)
	    if len(data) == 0:
	        break
	    str_data = str(data, 'UTF-8')
	    print("Flag:", str_data)
	print("Connection finished :)")
	s.close()

#This send to math_calc the first data that returns from server, where is it locate the specific numbers

data = s.recv(10240)     
str_data = str(data, 'UTF-8')
math_calc(str_data)

