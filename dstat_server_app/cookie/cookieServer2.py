import socket

host = ''
port = 5560
# This port is arbitrary, it can be any that does not interfere with the ssh (22) or web (80)

storedValue = "Hello world"

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")
    try:
        s.bind(host, port)
    except socket.error as msg:
        print(msg)
    print("Socket bind complete.")
    return s

# s is our socket so other functions can access it
# AF_INET type of communication

def setupConnection()
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ";" + str(address[1]))
    return conn

# Use the connection object later

def GET():
    reply = storedValue
    return reply

def REPEAT(dataMessage):
    reply - dataMessage[1]
    return  reply

def dataTransfer(conn):
    # A big loop that sends/receives data until told not to
    while True:
        # Reveive the data
        data = conn.recv(1024) # receive the data 1024 = buffer size
        data = data.decode('utf-8') # we are working in strings
        # Split the data to separate the command from
        # the rest of the data. Use the first
        dataMessage = data.split(' ', 1)
        command = dataMessage[0]
        if command == 'GET':
            reply = GET()
        elif command == 'REPEAT':
            reply = REPEAT(dataMessage)
        elif command == 'EXIT':
            print("Our client left :(")
            break
        elif command == 'KILL'
            print("Our server is shutting down.")
            s.close()
            break
        else:
            reply = "Unknown command"
        # Send the reply back to the client
        conn.sendall(str.encode(reply))
        print("Data has been sent!")
    conn.close()

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break
