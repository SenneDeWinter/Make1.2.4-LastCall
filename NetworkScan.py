#!/usr/bin/env python
"""
Info about our project code
"""


from socket import *
import time
startTime = time.time()


__author__ = "Senne De Winter"
__email__ = "senne.dewinter@student.kdg.be"
__status__ = "Development"

def main():
    target = input('Enter the host to be scanned: ') #to ask for the domain
    t_IP = gethostbyname(target)                     #to set the domain
    print('Starting scan on host: ', t_IP)           #to print that the script started

    for i in range(50, 500):                         #to repeat
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))               #to ping the ports
        if (conn == 0):
            print('Port %d: OPEN' % (i,))            #to print open if a port is open
        s.close()


print('Time taken:', time.time() - startTime)        #to print how long everything took


if __name__ == '__main__':
    main()
