import socket
import time
#import pickle

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'

SERVER ="192.168.225.174"
ADDR = (SERVER, PORT)

DISCONNECT_MESSAGE = "!CLIENT DISCONNECTED"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b'' * (HEADER - len(send_length))
    client.send(send_length)
    time.sleep(3)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send('hi')
send('my name is forku brandon')
send('what is your name?')
send('what si my name?')
send(DISCONNECT_MESSAGE)