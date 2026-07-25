
import pyaudio
import keyboard
import socket
import threading
import time



HEADER = 64      # fixed-size prefix telling the server how big the message is
PORT   = 5050    # port the server listens on
DISCONNECT = 'Disconnect'  # magic string to signal end of session
server = socket.gethostbyname(socket.gethostname())                                # server IP address
ADDR   = (server, PORT)                              # (IP, port) tuple for socket functions
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # IPv4 TCP socket
client.connect(ADDR)                                 # establish connection to server
CHUNK = 1024 #a single unit of chunk contains 1024 sample at a time 
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100 #taking 44k samples in a sec ( audio is wave s=and samples are small points of the wave)


p = pyaudio.PyAudio()

input_stream = p.open(format=FORMAT, channels=CHANNELS,
                      rate=RATE, input=True, frames_per_buffer=CHUNK)

output_stream = p.open(format=FORMAT, channels=CHANNELS,
                       rate=RATE, output=True, frames_per_buffer=CHUNK)


def send_loop():
        print("PRESS ~ to send voie data--")
        while True:
            if  keyboard.is_pressed("~"):
                data = input_stream.read(CHUNK)
                client.send(data)
                time.sleep(0.01)


    #---------------------------------------------------------------------------------------------------------------------------------------------#

def receive_loop():
        #print("receive loop started")
        while True:
            data = client.recv(1024)
            if data:
                #print(f"Received {len(data)} bytes")
                output_stream.write(data)
                time.sleep(0.01)
    #---------------------------------------------------------------------------------------------------------------------------------------------#    
#---------------------------------------------------------------------------------------------------------------------------------------------#




threading.Thread(target=receive_loop, daemon=True).start()
send_loop()
input_stream.close()
output_stream.close()
p.terminate()
