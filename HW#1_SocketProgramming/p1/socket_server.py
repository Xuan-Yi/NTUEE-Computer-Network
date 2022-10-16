import socket
from datetime import datetime
import time

with open('./b09901080_p1_server_log.txt', 'w') as logFile:
    # Specify the IP address and port number
    # (use "127.0.0.1" for localhost on local machine)
    # Create a socket and bind the socket to the address
    # Todo start

    HOST, PORT = '127.0.0.1', 2103
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    # Todo end

    while True:
        # Listen to any request()
        # Todo start
        s.listen(0)
        # Todo end

        now = datetime.now()
        print("The Server is running..")
        logFile.write(now.strftime("%H:%M:%S ") + "The Server is running..\n")
        logFile.flush()

        reconnect_counter = 0

        while True:
            try:
                # Accept a new request
                # Todo start
                Client, Addr = s.accept()
                # Todo end

                while True:
                    Client.send(b"Please input a question for calculation")
                    # Recieve the data from the client, and send the answer back to the client
                    # Ask if the client want to terminate the process
                    # Terminate the process or continue
                    # Todo start
                    Question = Client.recv(1024).decode('utf-8')
                    logFile.write(f'Question: {Question}\n')
                    print(f'Question: {Question}')
                    # Parser
                    ope_list = []  # list of operators and operands
                    number = ""  # temporary number memory
                    valid = True    # valif flag
                    for i in range(len(Question)):
                        if Question[i] in ['+', '-', '*', '/']:
                            ope_list.append(int(number))
                            ope_list.append(Question[i])
                            number = ''
                        elif Question[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                            number = number+Question[i]
                        elif Question[i] == " ":
                            pass
                        else:
                            valid = False

                    if number != '':
                        ope_list.append(int(number))

                    while "" in ope_list:
                        ope_list.remove("")

                    # Calculate
                    if not valid:
                        Client.send(
                            b'Please give a valid formula\nDo you wish to continue? (Y/N)')
                        logFile.write('Not valid input')
                    else:
                        answer = ope_list[0]
                        # basic operations
                        if ope_list[1] == '+':
                            answer += ope_list[2]
                        elif ope_list[1] == '-':
                            answer -= ope_list[2]
                        elif ope_list[1] == '*':
                            answer *= ope_list[2]
                        elif ope_list[1] == '/':
                            answer /= float(ope_list[2])
                        Client.send(
                            bytes((str(answer)+'\nDo you wish to continue? (Y/N)').encode('utf-8')))
                        logFile.write(f'Answer: {str(answer)}\n')
                        print(f'Answer: {str(answer)}')

                    # Ask whether to continue
                    response = Client.recv(100).decode('utf-8')
                    if response == 'N':
                        break
                    # Todo end
                break
            except ValueError as e:
                continue
        break
    logFile.close()
    print('disconnect...')
    # Close the socket
    # Todo start
    s.close()
    # Todo end
logFile.close()
