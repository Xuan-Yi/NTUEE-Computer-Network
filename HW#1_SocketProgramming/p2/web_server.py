from socket import *

# Note: After finishing the program, try to type http://HOST:PORT/index.html in your browser for test

ServerSocket = socket(AF_INET, SOCK_STREAM)
# Create a socket and bind the socket to the address
# Todo start
HOST, PORT = '192.168.1.104', 2103
ServerSocket.bind((HOST, PORT))
ServerSocket.listen(0)
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
        RecvMessage = ConnectionSocket.recv(4096).decode()  # HTTP request
        # Todo end

        if RecvMessage == "":
            RecvMessage = "/ /"

        FileName = RecvMessage.split()[1]
        f = open(FileName[1:], encoding='utf-8')

        # Read data from the file that the client requested
        # Split the data into lines for further transmission
        # Todo start
        DataInFile = f.readlines()
        f.close()
        # Todo end

        # Send one HTTP header line into socket
        # Send HTTP Status to the client
        # Todo start
        ConnectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        # Todo end

        # Send the Content Type to the client
        # Todo start
        ConnectionSocket.send('Content-Type: text/html\r\n\n'.encode())
        # Todo end

        # Send the content of the requested file to the client
        for i in range(0, len(DataInFile)):
            ConnectionSocket.send(DataInFile[i].encode())
        ConnectionSocket.send("\r\n".encode())

        print(RecvMessage)
        print(FileName)

        ConnectionSocket.close()
    except IOError as e:
        # Send the response message if the file is not found
        # Todo start
        if str(e) != '[Errno 2] No such file or directory: \'favicon.ico\'':
            print('/NOTFOUND.HTML')
            print('404 NOT FOUND')
        else:
            print(f'error: {e}')
        f = open('NOTFOUND.HTML', encoding='utf-8')
        DataInFile = f.readlines()
        f.close()

        ConnectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        ConnectionSocket.send('Content-Type: text/html\r\n\n'.encode())
        for i in range(0, len(DataInFile)):
            ConnectionSocket.send(DataInFile[i].encode())
        ConnectionSocket.send("\r\n".encode())
        # Todo end

        # Close client socket
        # Todo start
        ConnectionSocket.close()
        # Todo end
