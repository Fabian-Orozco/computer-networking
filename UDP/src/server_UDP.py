# fabian.orozcochaves@ucr.ac.cr
# Fabian Orozco Chaves - B95690

# Servidor UDP (super clase).
# Apoyado en: <https://tinyurl.com/realPythonSockets> & <https://tinyurl.com/cppSecretsUDPServer>

import socket
import threading
import server_UDP

from datetime import datetime

#######################################################################

''' Clase de un servidor UDP multi-cliente '''
class ServerUDP:

    def __init__(self, host, port): # Constructor
        self.host = host  # Direccion IP
        self.port = port  # Puerto de escucha
        self.sock = None  # Socket del servidor
  
    def print_msg_time(self, msg):
        ''' Imprime el día y la hora actuales + el mensaje enviado por parámetro '''
        current_time = datetime.now().strftime('%x - %X')
        print (f'[{current_time}] {msg}')
    
    def configure_server(self):
        ''' Crea el socket, hace el bind del servidor'''
        self.print_msg_time('Creating socket...')
        
        # IPv4 como red local y socket UDP.
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

        self.print_msg_time('Socket created')
        self.print_msg_time(f'Binding server to Host: {self.host} | Port: {self.port}...')

        self.sock.bind((self.host, self.port))
        self.print_msg_time(f'Server binded  to Host: {self.host} | Port: {self.port}...')

    def get_received_successfully(self, data):
        ''' Reconoce si el dato está vacío, de no ser así le agrega que se recibió exitosamente. Retorna el resultado'''
        if data:
            return f'Successfully received:\n{data}\n'
        else:
            return f'[Server] received -empty message-\n'
    
    def handle_request(self, data, client_address):
        '''Indica que se recibó una solicitud, la imprime y envía una confirmación de recibido'''
        msg_received = data.decode('utf-8')  # Convierte a string
        
        self.print_msg_time(f'[ REQUEST from {client_address} ]')
        print(self.get_received_successfully(msg_received))

        self.print_msg_time(f'[ CONFIRMATION SENT to {client_address} ]')
        # Envía en bytes la información.
        self.sock.sendto( ("server notify: RECEIVED").encode('utf-8'), client_address ) 
    
    def wait_for_client(self):
        '''Recibe los datos por medio del socket e invoca a la función para que la manipule lo recibido y envíe una respuesta'''
        try:
            data, client_address = self.sock.recvfrom(1024)
            self.handle_request(data, client_address)

        except OSError as err:
            self.print_msg_time(err)
        
        finally:
            self.print_msg_time('Server done waiting for client')
    
    def shutdown_server(self):
        ''' Indica que el servidor se cierra y cierra el socket del servidor'''
        self.print_msg_time(f'Shutting down server...')
        self.sock.close()
        self.print_msg_time(f'Server OFF')

# end class ServerUDP