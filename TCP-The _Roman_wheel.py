
import socket
import re
import codecs


#Connecting to server
server_address = ('challenge01.root-me.org', 52021)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(server_address)

def rot13_decode(msg):     
	f_value = re.search('(?<=is \')(\S+)',msg)
	f_value = f_value.group()
	f_value = f_value.replace('\'', '')
	f_value = f_value.replace('.', '')
	f_value = codecs.decode(f_value, 'rot_13')
	print(f_value)
	send_msg(f_value.encode())
	


def send_msg(msg):     
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


data = s.recv(10240)     
str_data = str(data, 'UTF-8')
print(str_data)
rot13_decode(str_data)
