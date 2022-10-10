from email.message import Message
import socket
from datetime import datetime
import string

with open('./server_log.txt', 'w') as logFile:
    # Specify the IP address and port number
    # (use "127.0.0.1" for localhost on local machine)
    # Create a socket and bind the socket to the address
    # TODO start
    HOST, PORT = '127.0.0.1', 12000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(0)
    # TODO end

    while True:
        # Listen to any request()
        # TODO start
        # TODO end

        now = datetime.now()
        print("The Server is running..")
        logFile.write(now.strftime("%H:%M:%S ") + "The Server is running..\n")
        logFile.flush()

        while True:
            try:
                # Accept a new request
                # TODO start
                Client, Addr = s.accept()
                # TODO end

                while True:
                    Client.send(b"Please input a question for calculation")
                    # Recieve the data from the client, and send the answer back to the client
                    # Ask if the client want to terminate the process
                    # Terminate the process or continue
                    # TODO start
                    Question = Client.recv(1000).decode('utf-8')
                    # Parser
                    Qusetion = str(Question).replace(" ","")    # remove all spacef
                    ope_list=[] # list of operators and operands
                    number = "" # temporary number memory
                    valid = True    # valif flag
                    for i in range(len(Question)):
                        if Question[i] in ['+','-','*','/','(',')']:
                            ope_list.append(int(number))
                            ope_list.append(Question[i])
                            number=''
                        elif Question[i] in ['0','1','2','3','4','5','6','7','8','9']:
                            number = number+Question[i]
                        else: 
                            valid = False

                    while "" in ope_list:
                        ope_list.remove("")
                    
                    for i in range(len(ope_list)):
                        if ope_list[i] in ['+','-','*','/']:
                            if (i>0) and (ope_list[i-1] not in ['0','1','2','3','4','5','6','7','8','9',')']):
                                valid = False
                            elif (i<(len(ope_list)-1)) and (ope_list[i+1] not in ['0','1','2','3','4','5','6','7','8','9','(']):
                                valid = False
                            elif (i==0) or (i==(len(ope_list)-1)):
                                valid = False
                        elif ope_list[i] =='(':
                            if (i>0) and (ope_list[i-1] in ['0','1','2','3','4','5','6','7','8','9',')']):
                                valid=False
                            elif (i<(len(ope_list)-1)) and (ope_list[i+1] in ['+','-','*','/',')']):
                                valid=False
                            elif i==len(ope_list)-1:
                                valid=False
                        elif ope_list[i]==')':
                            if (i>0) and (ope_list[i-1] in ['+','-','*','/','(']):
                                valid=False
                            elif (i<(len(ope_list)-1)) and (ope_list[i+1] in ['0','1','2','3','4','5','6','7','8','9','(']):
                                valid=False
                            elif i==0:
                                valid=False
                    
                    temp_stack = []   # -1 as head
                    temp_ope_stack = ope_list   # -1 as head
                    
                    while len(temp_ope_stack)!=0:
                        if temp_ope_stack[-1]=='(':
                            if temp_stack[-1]==')':
                                temp_stack.remove(-1)
                            else:
                                temp_stack.append('(')
                        elif temp_ope_stack[-1]==')':
                            if(temp_stack[-1]=='('):
                                temp_stack.remove(-1)
                            else:
                                temp_stack.append(')')
                        temp_ope_stack.remove(-1)
                    if len(temp_stack)!=0:
                        valid=False
                    
                    # Calculate
                    if not valid:
                        Client.send(b'Please give a valid formula')
                    else:
                        answer = ope_list[0]
                        # basic operations
                        if ope_list[1]=='+':
                            answer = answer+ope_list[2]
                        elif ope_list[1]=='-':
                            answer=answer- ope_list[2]
                        elif ope_list[1]=='*':
                            answer = answer+ope_list[2]
                        elif ope_list[1]=='/':
                            answer = float(answer)/float(ope_list[2])
                        Client.send(answer)
                    # Ask whether to continue
                    Client.send(b'Do you wish to continue? (Y/N)')
                    response = Client.recv(100).decode('utf-8')
                    if response == 'N':
                        break    
                    # TODO end
                    
                Client.close()
            except ValueError:
                continue
        break
    logFile.close()
    # Close the socket
    # TODO start
    # TODO end
