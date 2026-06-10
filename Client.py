import socket
import threading
HEADER = 64      # fixed-size prefix telling the server how big the message is
PORT   = 5050    # port the server listens on
FORMAT = 'utf-8'  # text encoding for bytes conversion
DISCONNECT = 'Disconnect'  # magic string to signal end of session
server = socket.gethostbyname(socket.gethostname())                                # server IP address
ADDR   = (server, PORT)                              # (IP, port) tuple for socket functions
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 TCP socket
client.connect(ADDR)                                 # establish connection to server

#----------------------------------------------------------------------------------------------------------------------------------
# -----------#



#---------------------------------------------------------------------------------------------------------------------------------------------#

def send_loop():
    while True:
        data = input("--> ")
        msg = data.encode(FORMAT)            # str → bytes
        data_length = len(msg)                   # byte count of message
        send_len  = str(data_length).encode(FORMAT).zfill(64) #encoding with padding
        #send_len += b' ' * (HEADER - len(send_len))  # maual pad to exactly 64 bytes
        client.send(send_len)                    # ① header — server reads this first
        client.send(msg)

#---------------------------------------------------------------------------------------------------------------------------------------------#

def sending(data):
    msg = data.encode(FORMAT)            # str → bytes
    data_length = len(msg)                   # byte count of message
    send_len  = str(data_length).encode(FORMAT).zfill(64) #encoding with padding
    #send_len += b' ' * (HEADER - len(send_len))  # maual pad to exactly 64 bytes
    client.send(send_len)                    # ① header — server reads this first
    client.send(msg)

#---------------------------------------------------------------------------------------------------------------------------------------------#

def receive_loop():
    while True:
        length_data = client.recv(64).decode(FORMAT) # IN CASE OF MANUAL PADDING USE .strip()
        length = int(length_data)
        if length:
            actual_message = client.recv(length).decode(FORMAT)
            print(f"\n{actual_message}\n--> ", end="", flush=True)

#---------------------------------------------------------------------------------------------------------------------------------------------#
Name = input("ENTER YOUR NAME :")
sending(Name)

length_data = client.recv(64).decode(FORMAT) # IN CASE OF MANUAL PADDING USE .strip()
length = int(length_data)
if length:
            actual_message = client.recv(length).decode(FORMAT)
            print(actual_message)
            print("                                                     ")

#---------------------------------------------------------------------------------------------------------------------------------------------#

threading.Thread(target=receive_loop, daemon=True).start()
send_loop()
