
import socket
import sys
try:
    sock_obj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error as err_msg:
    print ('Unable to instantiate socket. Error code: ' + str(err_msg[0]) + ', Error message: ' + err_msg[1])
    sys.exit();
def Main():
    host = '127.0.0.1'
    port = 5001

    mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    mySocket.connect((host,port))

    message = input(" ? ")

    while message != 'q':
        mySocket.sendto(message.encode(),)
    data = mySocket.recvfrom(1024).decode()

    print ('Received from server: ' + data)
    message = input(" ? ")

    mySocket.close()

if __name__ == '__main__':
    Main()

print('Socket Initialized')

