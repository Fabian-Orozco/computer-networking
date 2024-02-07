# fabian.orozcochaves@ucr.ac.cr
# Fabian Orozco Chaves - B95690

# Cliente UDP (multi-envios)
# Finalice el cliente con EOF / SIGINT / kill.
# Apoyado en: <https://tinyurl.com/cppSecretsUDPServer>

import socket
from datetime import datetime

#######################################################################

txt_GREEN = '\033[32m'
txt_RESET = '\033[0m'
txt_BLUE = '\033[34m'
txt_RED = '\033[31m'
txt_BOLD_UNDERLINE = '\033[1m\033[4m'

#######################################################################

''' Clase de un cliente UDP que envía activamente (while true) '''
class ClientUDP:
    def __init__(self, host, port):  # Constructor
        self.host = host  # Direccion IP
        self.port = port  # Puerto de escucha
        self.sock = None  # Socket del servidor
        self.sockTimeout = 10  # Tiempo de espera del socket para recibir una respuesta de lo que envió.
    
    def print_msg_time(self, msg):
        ''' Imprime el día y la hora actuales + el mensaje enviado por parámetro '''
        current_time = datetime.now().strftime('%x - %X')
        print (f'[{current_time}] {msg}')
    
    def configure_client(self):
        ''' Crea el socket  '''
        self.print_msg_time('Creating UDP/IPv4 socket...')
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(self.sockTimeout)  # Lo establece como el valor del atributo
        self.print_msg_time('Socket created')

    def send_to_server(self, data_to_send):
        ''' Envía la información al servidor '''
        self.sock.sendto(data_to_send.encode('utf-8'), (self.host, self.port))
        self.print_msg_time(f'[msg SENT] to {self.port}')

    def receive_from_server(self):
        try:
            resp, server_address = self.sock.recvfrom(1024)
            self.print_msg_time(f'[ confirm RECEIVED ] from {self.port}')
            print('\n', resp.decode('utf-8'), '\n')
        
        except socket.timeout as e:
            self.print_msg_time(f'timeout {self.sockTimeout}s: nothing received')
    
    def finalize_interact(self):
        self.print_msg_time(f'Done interaction...')
        self.print_msg_time('Closing socket...')
        self.sock.close()
        self.print_msg_time(f'Socket closed')

    def interact_wit_server(self):
        ''' Envia datos continuamente al servidor establecido por medio del socket '''
        try:
            while True:  # Escucha continuamente
                try:
                    data_to_send = input('Enter message to send: ')
                
                except KeyboardInterrupt as err:  # SIGINT (ctrl+c)
                    print(f' \nProgram finished by signal SIGINT')
                    break

                except EOFError as err:  # EOF (ctrl+d)
                    print(f' \nProgram finished by signal EOF')
                    break
                
                self.send_to_server(data_to_send)
                self.receive_from_server()

        finally:
            self.finalize_interact()

# end class ClientUDP

#######################################################################

def main():
    client = ClientUDP('127.0.0.1', 8080)
    client.configure_client()
    client.interact_wit_server()

if __name__ == '__main__':
    main()

#######################################################################
