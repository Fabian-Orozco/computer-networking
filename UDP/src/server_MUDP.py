# fabian.orozcochaves@ucr.ac.cr
# Fabian Orozco Chaves - B95690

# Servidor UDP multi-cliente (clase hija).
# Hereda de server_UDP.
# Apoyado en: <https://tinyurl.com/realPythonSockets> & <https://tinyurl.com/cppSecretsUDPServer>

import socket
import threading
import server_UDP
from datetime import datetime

#######################################################################

''' Clase simple que hereda de server_UDP 
    Escucha por el puerto 8080 y retorna un mensaje al socket con "RECEIVED" '''
class ServerUDP_Multi(server_UDP.ServerUDP):

    def __init__(self, host, port):  # Constructor
        super().__init__(host, port)  # Utiliza el constructor de la clase padre
        self.socket_lock = threading.Lock()  # Evita problemas de sincronización por condiciones de carrera. Solo un hilo puede acceder al socket.

    def handle_request(self, data, client_address):
        '''Indica que se recibó una solicitud, la imprime y envía una confirmación de recibido'''
        msg_received = data.decode('utf-8')

        self.print_msg_time(f'[ REQUEST from {client_address} ]')
        print(self.get_received_successfully(msg_received))

        self.print_msg_time(f'[ confirmation SENT to {client_address} ]')

        # Cuando acaba hace un unlock del socket.
        with self.socket_lock:
            self.sock.sendto(("server notify: RECEIVED").encode('utf-8'), client_address)
    
    def wait_for_client(self):
        '''Recibe los datos por medio del socket y crea un hilo para que se encargue de manipular la solicitud'''
        try:
            while True:  # Escucha continuamente
                try:
                    data, client_address = self.sock.recvfrom(1024)

                    # Creacion de hilos
                    c_thread = threading.Thread(target = self.handle_request, args = (data, client_address))

                    # El thread se elimina de forma automática cuando el programa se cierra
                    c_thread.daemon = True

                    # El hilo inicia la ejecución de "handel request"
                    c_thread.start()

                except OSError as err:
                    self.print_msg_time(err)
        
        except KeyboardInterrupt:
            self.shutdown_server()

# end class ServerUDP_Multi

#######################################################################

def main():
    server = ServerUDP_Multi('127.0.0.1', 8080)  # IP, puerto
    server.configure_server()
    server.wait_for_client()

if __name__ == '__main__':
    main()

#######################################################################
