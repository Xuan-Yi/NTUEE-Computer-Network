from socket import *
import os

# Note: After finishing the program, try to type http://HOST:PORT/index.html in your browser for test

ServerSocket = socket(AF_INET, SOCK_STREAM)
# Create a socket and bind the socket to the address
# Todo start
# HOST, PORT = str(gethostbyname(gethostname())), 2103    # current IP
HOST, PORT = '127.0.0.1', 2103  # localhost
print(f'(HOST, PORT) = ({HOST}, {PORT})\n')
ServerSocket.bind((HOST, PORT))
ServerSocket.listen(10)
# Todo end

while True:
    print('Ready to serve...')

    # Establish the connection
    # Todo start
    ConnectionSocket, Addr = ServerSocket.accept()
    # Todo end

    try:
        # Receive a HTTP request from the client
        # Todo start
        RecvMessage = ConnectionSocket.recv(
            4096).decode('utf-8')  # HTTP request
        # Todo end

        if RecvMessage == "":
            RecvMessage = "/ /"

        FileName = RecvMessage.split()[1]

        # handle favicon.ico
        if FileName == 'favicon.ico':
            ConnectionSocket.send('HTTP/1.1 404 NotFound\r\n'.encode('utf-8'))
            continue

        f = open(os.path.join(os.getcwd(), FileName[1:]), encoding='utf-8')

        # Read data from the file that the client requested
        # Split the data into lines for further transmission
        # Todo start
        DataInFile = f.readlines()
        f.close()
        # Todo end

        # Send one HTTP header line into socket
        # Send HTTP Status to the client
        # Todo start
        ConnectionSocket.send('HTTP/1.1 200 OK\r\n'.encode('utf-8'))
        # Todo end

        # Send the Content Type to the client
        # Todo start
        ConnectionSocket.send(
            'Content-Type: text/html\r\n\r\n'.encode('utf-8'))
        # Todo end

        # Send the content of the requested file to the client
        for i in range(0, len(DataInFile)):
            ConnectionSocket.send(DataInFile[i].encode('utf-8'))
        ConnectionSocket.send("\r\n".encode('utf-8'))

        print(RecvMessage)
        print(FileName)

        ConnectionSocket.close()
    except IOError as e:
        # Send the response message if the file is not found
        # Todo start
        if 'favicon.ico' not in str(e):
            print('404 Not Found')
            ConnectionSocket.send('HTTP/1.1 404 NotFound\r\n'.encode('utf-8'))
        # Todo end

        # Close client socket
        # Todo start
        if 'favicon.ico' not in str(e):
            ConnectionSocket.close()
        # Todo end
