#-------------------------------------------------------------------------------
# Name:        get host by name
# Purpose:
#
# Author:      urey
#
# Created:     14/10/2012
# Copyright:   (c) urey 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import socket
def main():
    hostname = "chiphell.com"
    addr = socket.gethostbyname(hostname)
    print "the address of", hostname, "is", addr

    pass

if __name__ == '__main__':
    main()
