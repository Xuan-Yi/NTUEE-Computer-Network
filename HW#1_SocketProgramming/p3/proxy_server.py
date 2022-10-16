from socket import *

host_port = []

# Create a server socket, bind it to a port and start listening
TCPServerSocket = socket(AF_INET, SOCK_STREAM)
# Todo start
HOST, PORT = '127.0.0.1', 2104  # default HOST:PORT

TCPServerSocket.bind((HOST, PORT))
TCPServerSocket.listen(10)
# Todo end

while True:
    # Strat receiving data from the client
    print('Ready to serve...')
    # Todo start
    TCPClientSocket, Addr = TCPServerSocket.accept()
    # Todo end
    print('Received a connection from:', Addr)

    # Receive request from the client
    # Todo start
    RecvMessage = TCPClientSocket.recv(4096).decode('utf-8')
    # Todo end
    print(RecvMessage)

    # Extract the filename from the given message
    if RecvMessage == "":
        RecvMessage = "/ /"
    print(RecvMessage.split()[1])
    Filename = RecvMessage.split()[1].partition("/")[2]
    print(Filename)
    FileExist = "false"
    FileToUse = "/" + Filename
    print(FileToUse)

    # handle favicon.ico
    if Filename == 'favicon.ico':
        TCPClientSocket.send(("HTTP/1.1 404 NotFound\r\n").encode('utf-8'))
        continue

    # handle other normal requests
    try:
        # Check whether the file exist in the cache
        f = open(FileToUse[1:], "r", encoding='utf-8')
        DataInFile = f.readlines()
        f.close()
        FileExist = "true"

        # Proxy Server finds the file (cache hit) and generates a response message
        # Send the file back to the client
        TCPClientSocket.send(("HTTP/1.1 200 OK\r\n").encode('utf-8'))
        TCPClientSocket.send(
            ("Content-Type:text/html\r\n\r\n").encode('utf-8'))
        # Todo start
        for i in range(len(DataInFile)):
            TCPClientSocket.send(DataInFile[i].encode('utf-8'))
        TCPClientSocket.send("\r\n".encode('utf-8'))
        TCPClientSocket.close()
        # Todo end

        print('Read from cache')

    # Error handling if the file is not found in cache
    except IOError:
        if FileExist == "false":
            # Create a socket on the proxy server
            # Todo start
            SocketOnProxyServer = socket(AF_INET, SOCK_STREAM)
            # Todo end
            HostName = Filename.replace("www.", "", 1)
            # print("host name is " + HostName)
            try:
                print("try to connect to the web_server")
                # Connect the socket to the web server port
                # Todo start
                SocketOnProxyServer.connect(
                    ('127.0.0.1', 2103))    # IP of web_server
                # Todo end
                print("connected successfully")

                # Create a temporary file based on this socket
                FileObject = SocketOnProxyServer.makefile(
                    'rw', None, encoding='utf-8')
                print("GET " + "http://" + FileToUse + " HTTP/1.1\r\n")
                FileObject.write("GET " + FileToUse + " HTTP/1.1\r\n")
                FileObject.flush()
                print("get the file successfully")

                # Read the response into buffer
                # Todo start
                Buffer = FileObject.readlines()
                pivot = [i for i, val in enumerate(
                    Buffer) if val == '\n']  # index of blank
                status = Buffer[0].split()[1]
                if status == '404':
                    print('404 Not Found')
                    continue
                Data = Buffer[pivot[0]+1:]
                # Todo end

                # Create a new copy in the cache for the requested file
                # Also send the response back to client socket and the corresponding file from cache
                TmpFile = open(Filename, "w", encoding='utf-8')
                print("open the file successfully")
                # Todo start
                for i in range(len(Buffer)):
                    TCPClientSocket.send(Buffer[i].encode())
                for j in range(len(Data)):
                    TmpFile.write(str(Data[j]))
                TmpFile.close()
                SocketOnProxyServer.close()
                # Todo end

            except:
                print("Illegal request")
        else:
            # HTTP response message for file is not found
            # Todo start
            print('404 Not Found')
            # Todo end

        # Close the client sockets
        TCPClientSocket.close()
    # break

# Close the server socket
# Todo start
TCPServerSocket.close()
# Todo end
