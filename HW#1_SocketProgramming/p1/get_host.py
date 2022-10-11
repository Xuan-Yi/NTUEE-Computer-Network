
import socket

# Get the local host name
HostName = socket.gethostname()
print("Name of the localhost is {}".format(HostName))


# Get the IP address of the local host

IP = socket.gethostbyname(HostName)
print("IP address of the localhost is {}".format(IP))