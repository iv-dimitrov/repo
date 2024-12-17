import socket
def establish_connection(server_ip):
    server_port = 5000        # Portnummer des Servers
    # Erstellen des Client-Socketobjekts
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Ergänzung: Stelle eine Verbindung zum Server her
    client_socket.connect((server_ip, server_port))
 
    
    return client_socket        # Client_socket connected?

def set_pin_state(client_socket, pin, state):
    command = f"{pin} {state}"

    print(command)
    client_socket.send(command.encode('utf-8'))

    #server_response = client_socket.recv(1024).decode("utf-8")

    #print(server_response)
