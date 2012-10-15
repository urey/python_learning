﻿#-------------------------------------------------------------------------------
# Name:        udp
# Purpose:
#
# Author:      urey
#
# Created:     14/10/2012
# Copyright:   (c) urey 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import socket, sys
def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    MAX = 65535
    PORT = 1060
    if sys.argv[1:] == ['server']:
        s.bind(('127.0.0.1', PORT))
        print 'Listening at', s.getsockname()
        while True:
            data, address = s.recvfrom(MAX)
            print 'The client at', address, 'says', repr(data)
            s.sendto('Your data was %d bytes' % len(data), address)
    elif sys.argv[1:] == ['client']:

        #print 'address before sending:', s.getsockname()
        s.sendto('this is my message', ('127.0.0.1', PORT))
        print 'address after sending', s.getsockname()
        data, address = s.recvfrom(MAX)
        print 'the server', address, 'says', repr(data)
    else:
        print >> sys.stderr, 'usage: udp.py server|client'
    pass

if __name__ == '__main__':
    main()
