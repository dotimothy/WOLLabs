# HTTPS Web Server for TheDoLab #
# Author: Timothy Do 
# 04/23/2022 

#import socket module
from socket import *
import os

# create an IPv4 TCP socket
#Fill in start 
serverSocket = socket(AF_INET,SOCK_STREAM)     
#Fill in end

# Server Socket Variables %
serverIP  = "0.0.0.0" 
serverPort = 6789 

# Prepare a sever socket
#Fill in start  
serverSocket.bind((serverIP,serverPort))
#Fill in end

# Listen for connections from client 
#Fill in start     
serverSocket.listen(1)
#Fill in end
print ("Hosting Server on Port " + str(serverPort) + " and Listening...")
while True:
    # Establish the connection
    
    connectionSocket, addr = serverSocket.accept()
    print("Accpeted Connection from " + str(addr[0]) + ":" + str(addr[1]))
    try:
        message = connectionSocket.recv(1024).decode()
        message_split = message.split()
        if len(message_split) <= 1:
            # Small connection from browser - ignore
            connectionSocket.close()
            continue
            
        filename = message_split[1]
        if(filename == "/"):
            filename = "/index.html"
            
        if(filename == "/wolserver.py"):
            outputdata = b'Permission Denied.'
        elif(filename == "/servertd2020"):
            outputdata = b'<script> alert(\'Turning on SERVER-TD2020 via WOL Server\'); close(); </script>'
            os.system("sudo etherwake -i eth0 18:03:73:BD:F7:BC")
        elif(filename == "/hp2020"):
            outputdata = b'<script> alert(\'Turning on DESKTOP-HP2020 via WOL Server\'); close(); </script>'
            os.system("sudo etherwake -i eth0 2C:27:D7:1D:00:C5")
        elif(filename == "/td2015"):
            outputdata = b'<script> alert(\'Turning on DESKTOP-TD2015 via WOL Server\'); close(); </script>'
            os.system("sudo etherwake -i eth0 D8:CB:8A:3C:3A:FF")
        elif(filename == "/tdmsi"):
            outputdata = b'<script> alert(\'Turning on LAPTOP-TDMSI via WOL Server\'); close(); </script>'
            os.system("sudo etherwake -i eth0 00:D8:61:85:A0:6B")
        elif(filename == "/workstation"):
            outputdata = b'<script> alert(\'Turning on WORKSTATION-TD2020 via WOL Server\'); close(); </script>'
            os.system("sudo etherwake -i eth0 F0:2F:74:F3:5E:95")
        elif(filename == "/allcomputers"):
            outputdata = b'<script> alert(\'Turning on All Computers via WOL Server\'); close(); </script>'
            os.system("sudo etherwake -i eth0 00:D8:61:85:A0:6B")
            os.system("sudo etherwake -i eth0 D8:CB:8A:3C:3A:FF")
            os.system("sudo etherwake -i eth0 2C:27:D7:1D:00:C5")
            os.system("sudo etherwake -i eth0 18:03:73:BD:F7:BC")
            os.system("sudo etherwake -i eth0 2C:F0:5D:71:EF:47")
        else:
            f = open(filename[1:], "rb")
            outputdata = f.read()
        
        # Send one HTTP header line into socket
        #Fill in start
        connectionSocket.send(b'HTTP/1.1 200 OK\r\n\r\n')
        #Fill in end
        
        # Send the content of the requested file to the client
        #Fill in start     
        connectionSocket.send(outputdata)
        #Fill in end
        
        # Close client socket
        #Fill in start
        connectionSocket.close()     
        #Fill in end        
    except IOError:
        # Send response message for file not found
        connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n\r\n')
        connectionSocket.send(b'<html><head></head><body><h1>404 Not Found</h1></body></html>')
        
        # Close client socket
        #Fill in start  
        connectionSocket.close()   
        #Fill in end
    except KeyboardInterrupt:
        # User pressed Ctrl+C, exit gracefully
        break
        
# Close server connection
serverSocket.close()
