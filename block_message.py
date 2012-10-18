#-------------------------------------------------------------------------------
# Name:        block
# Purpose:
#
# Author:      urey
#
# Created:     18/10/2012
# Copyright:   (c) urey 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# sending data one block at a time

import socket, struct, sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = sys.argv.pop() if len(sys.argv) == 3 else '127.0.0.1'
PORT = 1060
format = struct.Struct("!I")

def recvall(sock, length):
    data = ''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError("socket closed %d bytes into a %d-byte message" % (len(data), length))
        data += more
    return data

def get(sock):
    lendata = recvall(sock, format.size)
    (length,) = format.unpack(lendata)
    return recvall(sock, length)

def put(sock, message):
    sock.send(format.pack(len(message))+ message)

if sys.argv[1:] == ['server']:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    print 'Listen at', s.getsockname()
    sc, sockname = s.accept()
    print 'Accept connection from', sockname
    sc.shutdown(socket.SHUT_WR)
    while True:
        message = get(sc)
        if not message:     # if  message is 0 length then break, the server program is over
            break
        print 'message says:', repr(message)
    sc.close()
    s.close()

elif sys.argv[1:] == ['client']:
    s.connect((HOST, PORT))
    s.shutdown(socket.SHUT_RD)
    put(s, 'Please could you stop the noise ')
    put(s, 'I\'m trying to get some rest')
    put(s, ' From all the unborn chicken voices in my head')
    put(s, '')
    s.close()

else:
    print >>sys.stderr, 'usage: block_message.py server|client [host]'