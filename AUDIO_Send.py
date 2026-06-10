import pyaudio
import keyboard
import socket
import threading
import sys


HEADER = 1024
Client_IP_list = []
Client_PORT_list = []
Client_Name = []
ClientIP_EXCEPT_LIST =[]
ClientPORT_EXCEPT_LIST =[]
Active_Client_Sockets = []
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ADDR =(socket.gethostbyname(socket.gethostname()),5050)
SERVER.bind(ADDR)
#---------------------------------------------------------------------------------------------------------------------------------------------#

def Threading(Client,Address,active_clients_index):
   Client_Work(Client,Address,active_clients_index)
#---------------------------------------------------------------------------------------------------------------------------------------------#

def Broadcast(Client,active_clients_index,Plain_data,):
                if  Plain_data:      #if not ---
                        for Client_ in Active_Client_Sockets:
                                if Client_ is not Client:
                                        Client_.send(Plain_data)
                

#---------------------------------------------------------------------------------------------------------------------------------------------#

def Client_Work(Client,Address,active_clients_index):
        i = 0
        Connection = True
        print(f"Client is connected at : {Address}")
        while Connection:
                        Plain_data = Client.recv(HEADER)
                        Broadcast(Client, active_clients_index, Plain_data)

        Client.close()
#---------------------------------------------------------------------------------------------------------------------------------------------#

def Start_Server():
        SERVER.listen()
        i = 0
        while True:
                client_connection, client_address = SERVER.accept()
                thread = threading.Thread(target=Threading, args=(client_connection,client_address,threading.active_count()-1)) 
                thread.start()
                print(f'Client Successfully Connected [NUMBER OF ACTIVE CLIENTS : {threading.active_count()-1}]')
                Client_IP_list.append(client_address[0])
                Client_PORT_list.append(client_address[1])
                Active_Client_Sockets.append(client_connection)
                print(Client_PORT_list)
                print(Client_IP_list)
                i +=1
#---------------------------------------------------------------------------------------------------------------------------------------------#
print("starting")
Start_Server()
