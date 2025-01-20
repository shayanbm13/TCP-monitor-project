import socket
from PyQt5.QtCore import QObject, pyqtSignal

def get_local_IP():
    
    
    hostname = socket.gethostname()

    # دریافت تمام آدرس‌های IP مرتبط با این کامپیوتر
    ip_addresses = socket.gethostbyname_ex(hostname)
    # print(ip_addresses)

    # یافتن آدرس IP درون شبکه لوکال
    local_ip_address = str()
    try:
        for item in ip_addresses :
            if item.__len__() > 0:
                local_ip_address=[ip for ip in item if ip.startswith('192.168.')]
                
            else:
                local_ip_address="no ip found"
    except :
        local_ip_address="no ip found"
    
    return local_ip_address[0]
    
# print(get_local_IP())

    
# print(f"server is active server_IP is {server_ip} and port is {server_port} ")

class Server(QObject):
    clients = []
    running = True  # Flag to determine if the server is running

    received_message=list()
    
    

    def __init__(self):
        super().__init__()
        self.host = get_local_IP()
        self.port = 5354

    def start_server(self):
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server is active. Server IP is {self.host} and port is {self.port}")

            while self.running:
                conn, addr = s.accept()
                self.clients.append((conn, addr))
                print(f'Connected by {addr}. Total connected clients: {len(self.clients)}')

                # Handle the connection in a separate thread or process if needed.
                # You can create a new class/method for handling each connection.

                # Start a new thread or use non-blocking sockets to handle messages from clients.
                # Check for received messages in a loop.

                # Example of handling incoming messages:
                while True:
                    try:
                        data = conn.recv(1024)
                        if not data:
                            print(f'Disconnected by {addr}')
                            self.clients.clear()
                            print(f'Total connected clients: {len(self.clients)}')
                            break  # Break the loop when the client disconnects

                        # Process received data here...
                        received_messageee = data.decode('utf-8')  # تبدیل داده باینری به متن
                        print(f"Received message from client: {received_messageee}")
                        self.received_message.clear()
                        self.received_message.append(received_messageee)
                        
                        
                    except ConnectionResetError:
                        print(f'Client {addr} forcibly closed the connection.')
                        self.clients.remove((conn, addr))
                        print(f'Total connected clients: {len(self.clients)}')
                        break  # Break the loop when the client forcibly closes the connection
            print("Server Stoped")

    def send_message_to_clients(self, message):
        print(self.clients)
        for client, _ in self.clients:
            try:
                client.sendall(message.encode('utf-8'))
            except Exception as e:
                print(f"Error sending message to a client: {e}")

    def get_connected_clients(self):
        if self.clients.__len__()>0:
            return True
        elif self.clients.__len__()==0:
            return False
    def stop_server(self):
        self.running = False


# Usage example:
# Create an instance of the server
# my_server = Server()
# my_server.start_server()


# Start the server
# server_thread = threading.Thread(target=my_server.start_server)
# server_thread.start()

# When you want to stop the server, call the stop_server method
# my_server.stop_server()