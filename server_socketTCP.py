import socket
import RPi.GPIO as GPIO
import threading
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.IN)

server_ip = "192.168.1.114"
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('', 5000))

gpio_lock = threading.Lock()

def button_clicked(client_socket):
    while True:
        time.sleep(1)
        with gpio_lock:
            input_value = GPIO.input(22)
        
        if input_value == GPIO.HIGH:
            print("Button pressed")
            server_response = str("button_clicked").encode("utf-8")
            client_socket.sendall(server_response)

def server_main():
    server_socket.listen(1)
    print("Server bereit, um Verbindungen anzunehmen ...")

    client, address = server_socket.accept()
    print(f"Verbindung mit {address} hergestellt. ")

    button_thread = threading.Thread(target=button_clicked, args=(client,))
    button_thread.daemon = True 
    button_thread.start()

    try:
        while True:
            recv_data = client.recv(1024)
            if not recv_data:
                print("Leeres Byte empfangen. Verbindung wird getrennt ...")
                break

            print("Received data:", recv_data)
            recv_data = recv_data.decode().split()
            print(f"Decoded data: {recv_data}")
            
            pin_list = []
            true_false_list = []
            for item in recv_data:
                if item.isdigit():
                    pin_list.append(int(item))
                elif item.isalpha():
                    true_false_list.append(item)

            print(f"Pins: {pin_list}, States: {true_false_list}")

            if pin_list:
                GPIO.setup(pin_list[0], GPIO.OUT)
                if true_false_list[0] == "True":
                    GPIO.output(pin_list[0], GPIO.HIGH)
                elif true_false_list[0] == "False":
                    GPIO.output(pin_list[0], GPIO.LOW)

    except KeyboardInterrupt:
        print("Server interrupted by user.")
    finally:
        print("Cleaning up...")
        client.close()
        GPIO.cleanup()

if __name__ == "__main__":
    try:
        server_main()
    except Exception as e:
        print(f"Error: {e}")
        GPIO.cleanup()
