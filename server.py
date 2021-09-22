import socket


def main():
    local_ip = "192.168.1.4"
    local_port = 20001
    buffer_size = 1024
    msg_from_server = "Hello UDP Client"
    bytes_to_send = str.encode(msg_from_server)

    UDP_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    UDP_server_socket.bind((local_ip, local_port))

    print("UDP server up and listening")
    bytes_address_pair = UDP_server_socket.recvfrom(buffer_size)

    message = bytes_address_pair[0]
    address = bytes_address_pair[1]
    client_msg = f"Message from Client:{message}"
    client_ip = f"Client IP Address:{address}"

    print(client_msg)
    print(client_ip)

    UDP_server_socket.sendto(bytes_to_send, address)


if __name__ == '__main__':
    main()


