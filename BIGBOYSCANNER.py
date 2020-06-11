import socket
import subprocess
import sys
from datetime import datetime

# #Clear the screen
# subprocess.call("clear",shell=True)


#Just to style it
print("-" * 25,"BIGBOY SCANNER","-"*25)



#Ask user for input
remoteServer = input("Enter host to scan:")
remoteServerIP = socket.gethostbyname(remoteServer)

#Output information when scanning a host
print("-" * 60)
print("Please wait, scanning host", remoteServerIP)
print("-" * 60)

# Check time the scan started
time1=datetime.now()

# Scan ports from range 1-1025
try:
    port_range = range(1,1025)
    for port in port_range:
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            result=sock.connect_ex((remoteServerIP,port))
            if result==0:
                print("[+]Port {}: Open".format(port))
                sock.close()

except KeyboardInterrupt :
    print("You pressed Ctrl+C")
    sys.exit()
#
except socket.gaierror:
    print("Hostname could not be resolves. Exiting")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()

# checking the time again
time2= datetime.now()

# Calculate total time taken
Total_time = time2-time1

# Print info on the screen
print("Total time taken:",Total_time)

