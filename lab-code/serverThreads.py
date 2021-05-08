import socket, sys, re, time, os
sys.path.append("../lib")
import params
from socketFramed import framedSocket
import threader

switchesVarDefaults = (
    (('-l','--listenPort'),'listenPort',50001),
    (('-?','--usage'),"usage",False),)

progname = "echoserver"
paramMap = paramMap = params.parseParams(switchesVarDefaults)
listenPort = paramMap['listenPort']
listenAddr = ''

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((listenAddr,listenPort))
s.listen(1)

while True:
    conn,addr = s.accept()
    threader.Worker(conn,addr).start()
