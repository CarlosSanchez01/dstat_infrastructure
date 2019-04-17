import Socket
from time import sleep

host = '192.168.1.205' # Whichever ip address of the raspberry pi
port = '5560' # Same port than specified in the server

def setupSocket()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def sendReceive(s, message):
    s.send(str.encode(message))
    reply = s.receive(1024)
    print("We have received a reply")
    print("Send closing message.")
    s.send(str.encode("EXIT"))
    s.close()
    reply.decode('utf-8')
    return reply

def transmit(message)
    s = setupSocket()
    response = sendReceive(s, message)
    return response
