from email import message
import socket
import time

with open('./b09901080_p1_client_log.txt', 'w') as logFile:
    logFile.write("The Client is running..\n")
    logFile.flush()

    # Configure the server IP with its corrosponding port number
    # Specify the TCP connection type and make connection to the server
    # Todo start
    HOST, PORT = '127.0.0.1', 2103
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((HOST, PORT))
    except:
        print(f'unable to connect')
    # Todo end

    Testcase = open('./p1_testcase', 'r')
    TestcaseContents = Testcase.readlines()
    Testcase.close()

    # Write the information of HOST and PORT to the client_log.txt
    # Todo start
    logFile.write(f"Connect to {HOST}, using port number {PORT}\n")
    print(f"Connect to {HOST}, using port number {PORT}")
    # Todo end

    # Read test cases from p1_testcase
    # You can change the test case or create other test cases on your own
    state = 'formula'
    for PreprossingLine in TestcaseContents:
        Line = PreprossingLine.strip()

        # For connection stability
        time.sleep(3)

        # Client sent the request to the server and receive the response from the server
        # Todo start
        message = s.recv(4096).decode('utf-8')
        if state == 'formula':
            logFile.write(f'Received the message from server: {message}\n')
            print(f'Received the message from server: {message}')
        else:
            logFile.write(f'Answer: {message}\n')
            print(f'Answer: {message}')

        send = Line
        s.send(send.encode('utf-8'))
        if state == 'formula':
            logFile.write(f'Question: {send}\n')
            print(f'Question: {send}')
            state = 'continue'
        else:
            logFile.write(f'{send}\n')
            print(f'{send}')
            state = 'formula'
        # Todo end

    # Close the socket
    # Todo start
    s.close()
    print('disconnect...')
    # Todo end
logFile.close()
