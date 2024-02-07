# Servidor UDP multi-cliente

## **Manual de uso**

### **Ejecución:**

Utilice el siguiente comando: `python server_MUDP.py`  
para ejecutar el servidor UDP multi-cliente
Ejemplo:

~~~bash
$ python server_MUDP.py 
[MM/DD/AA - HH:MM:SS] Creating socket...
[MM/DD/AA - HH:MM:SS] Socket created
[MM/DD/AA - HH:MM:SS] Binding server to Host: 127.0.0.1 | Port: XXXX...
[MM/DD/AA - HH:MM:SS] Server binded  to Host: 127.0.0.1 | Port: XXXX...  

~~~

En otra terminal ejecute el siguiente comando: `python client_UDP.py`  
para ejecutar el cliente UDP (ejecute tantos comandos como clientes desee).

Ejemplo:

~~~bash
$ python client_UDP.py 
[MM/DD/AA - HH:MM:SS] Creating UDP/IPv4 socket...
[MM/DD/AA - HH:MM:SS] Socket created
Enter message to send: 
~~~

### **Interacción:**

A continuación digite el mensaje que quiere enviar al servidor.

Ejemplo:

~~~bash
Enter message to send: este es mi mensaje
[MM/DD/AA - HH:MM:SS] [msg SENT] to XXXX
[MM/DD/AA - HH:MM:SS] [ confirm RECEIVED ] from XXXX

 server notify: RECEIVED 

Enter message to send: 

~~~

Respuesta del servidor:

~~~bash
[MM/DD/AA - HH:MM:SS] [ REQUEST from ('127.0.0.1', PORT_CLIENT) ]
Successfully received:
este es mi mensaje

[MM/DD/AA - HH:MM:SS] [ confirmation SENT to ('127.0.0.1', PORT_CLIENT) ]
~~~

### **Finalización:**

Para finalizar un cliente digite `CTRL+D` o `CTRL+C`. O finalice mendiante el comando `kill`.

Ejemplo:

~~~bash
Enter message to send: ^C
Program finished by signal SIGINT
[MM/DD/AA - HH:MM:SS] Done interaction...
[MM/DD/AA - HH:MM:SS] Closing socket...
[MM/DD/AA - HH:MM:SS] Socket closed
$
~~~

Para finalizar el servidor digite `CTRL+C`. O finalice mendiante el comando `kill`.

Ejemplo:

~~~bash
[MM/DD/AA - HH:MM:SS][ confirmation SENT to ('127.0.0.1', 55638) ]
^C[MM/DD/AA - HH:MM:SS] Shutting down server...
[MM/DD/AA - HH:MM:SS] Server OFF
$
~~~

---

## **Créditos**

**Autor:** Fabián orozco chaves
**Contacto:** fabian.orozcochaves@ucr.ac.cr

Archivo de código apoyado en:  

- [Fuente_1](https://tinyurl.com/realPythonSockets)
- [Fuente_2](https://tinyurl.com/cppSecretsUDPServer)

---

## Otras rutas

[Ejemplo de uso con screenshots](./doc/Tarea3_B95690_ServerUDP.pdf)

---
