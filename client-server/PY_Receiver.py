# Python UDP Receiver

import socket
BUFFER_LEN = 100 #in bytes

IP = "127.0.0.1"
PORT = 8888

def initUDP(IP, port):
    #Create a datagram socket
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    #Enable immediate reuse of IP address
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    #Bind the socket to the port
    sock.bind((IP, port))
    #Set a timeout so the socket does not block indefinitely when trying to receive data
    sock.settimeout(10)

    return sock

def readUDP(sock):
    try:
        data, addr = sock.recvfrom(BUFFER_LEN)
    except socket.timeout as e:
        return b'Error'
    except Exception as e:
        return b'Error'
    else:
        return data

def main():
    print ("[Fabian] Inicia Py_Receiver\n")
    
    my_sock = initUDP(IP, PORT)
    msg_received = "init_true"

    while (msg_received):
        
        msg_received = readUDP( my_sock )
        print (msg_received.decode("utf-8"))
        
    print ("\n[Fabian] Termina Py_Receiver\n")
main()
