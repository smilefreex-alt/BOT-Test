#una botnet es una red de dispositivos infectados por malware, controlados por un atacante para realizar actividades maliciosas, como ataques DDoS, robo de datos o envío de spam.
#El uso ético de una botnet implica utilizarla con fines legítimos, como pruebas de seguridad, investigación o educación, siempre con el consentimiento de los propietarios de los dispositivos involucrados.
#Es importante destacar que el uso no autorizado de una botnet es ilegal y puede tener consecuencias graves, incluyendo sanciones legales y daños a terceros. Por lo tanto, es fundamental utilizar las botnets de manera responsable y ética, respetando la privacidad y seguridad de los demás.
#EMPEZEMOS A CREAR UNA BOTNET DE USO ÉTICO
import socket
import threading
import time

# Configuración del servidor
HOST = '0.0.0.0'  # Dirección IP del servidor
PORT = 65432        # Puerto del servidor
# Lista para almacenar los clientes conectados
clients = []
# Función para manejar la conexión de cada cliente
def handle_client(client_socket):
    while True:
        try:
            # Recibir datos del cliente
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Mensaje recibido: {data}")
            # Enviar una respuesta al cliente
            response = f"Mensaje '{data}' recibido correctamente."
            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
            break
    client_socket.close()
# Función para iniciar el servidor
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Servidor iniciado en {HOST}:{PORT}")
    while True:
        client_socket, addr = server.accept()
        print(f"Cliente conectado desde {addr}")
        clients.append(client_socket)
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()
# Iniciar el servidor
if __name__ == "__main__":
    start_server()
    #Como funciona esta botnet de uso ético?
    #1. El servidor se inicia y espera conexiones de clientes.
    #2. Cuando un cliente se conecta, se crea un nuevo hilo para manejar la comunicación con ese cliente.
    #3. El cliente puede enviar mensajes al servidor, y el servidor responde con una confirmación.
    #4. El servidor puede manejar múltiples clientes simultáneamente gracias a los hilos.
    #5. Esta botnet de uso ético se puede utilizar para pruebas de seguridad, investigación o educación, siempre con el consentimiento de los propietarios de los dispositivos involucrados.

    #Pasos para usar esta botnet de uso ético:
    #1. Ejecutar el servidor en una máquina que actuará como el controlador de la botnet.
    #2. Ejecutar el cliente en otras máquinas que actuarán como los bots de la botnet.
    #3. Enviar mensajes desde los clientes al servidor para probar la comunicación y la funcionalidad de la botnet.
    #4. Asegurarse de que todas las actividades se realicen con el consentimiento de los propietarios de los dispositivos involucrados y respetando la privacidad y seguridad de los demás.

    #Ten en cuenta que esta botnet de uso ético es solo un ejemplo básico y no debe ser utilizada para actividades maliciosas. Siempre es importante actuar de manera responsable y ética al utilizar cualquier tipo de tecnología.

    #Ejecucion paso a paso:
    #1. Ejecutar el servidor: Abre una terminal y ejecuta el script del servidor. El servidor se iniciará y estará listo para aceptar conexiones de clientes.
    #2. Ejecutar el cliente: Abre otra terminal y ejecuta el script del cliente. El cliente se conectará al servidor y podrás enviar mensajes desde el cliente al servidor.
    #3. Enviar mensajes: En la terminal del cliente, escribe un mensaje y presiona Enter. El mensaje se enviará al servidor, y el servidor responderá con una confirmación que se mostrará en la terminal del cliente.
    #4. Repetir el proceso: Puedes repetir el proceso de enviar mensajes desde el cliente al servidor varias veces para probar la comunicación y la funcionalidad de la botnet.
    #5. Finalizar la conexión: Para finalizar la conexión, puedes cerrar la terminal del cliente o del servidor. Asegúrate de cerrar ambos para liberar los recursos utilizados por la botnet de uso ético.

    #Este codigo es el servidor de la botnet de uso ético. Para crear el cliente, puedes utilizar el siguiente código:
    #import socket
    #HOST = '127.0.0.1'  # Dirección IP del servidor
    #PORT = 65432        # Puerto del servidor
    #client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #client.connect((HOST, PORT))
    #while True:
    #    message = input("Ingrese un mensaje para enviar al servidor: ")
    #    client.send(message.encode('utf-8'))
    #    response = client.recv(1024).decode('utf-8')
    #    print(f"Respuesta del servidor: {response}")
    

    #Esto lo que hace es crear un cliente que se conecta al servidor de la botnet de uso ético. El cliente puede enviar mensajes al servidor y recibir respuestas. Puedes ejecutar este código en varias máquinas para simular múltiples clientes conectándose al servidor. Recuerda siempre utilizar esta botnet de manera ética y con el consentimiento de los propietarios de los dispositivos involucrados. 
    

