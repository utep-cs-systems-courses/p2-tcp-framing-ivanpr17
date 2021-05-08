import sys,os,socket,threading
from time import time
from threading import Thread, enumerate
from socketFramed import framedSocket

threadNum = 0
inTransfer = set()
transferLock = threading.Lock()

class Worker(Thread):
    def __init__(self,conn,addr):
        global threadNum
        Thread.__init__(self,name="Thread-%d" % threadNum)
        threadNum+=1
        self.conn = conn
        self.addr = addr

    def checkTransfer(self, filename):
        global InTransfer, transferLock
        transferLock.acquire()
        if filename in inTransfer:
            canTransfer = False
        else:
            canTransfer = True
            inTransfer.add(filename)
        transferLock.release()

        return canTransfer

    def endTransfer(self, filename):
        global inTransfer
        inTransfer.remove(filename)

    def run(self):
        fs = framedSocket(self.conn)
        contents = (fs.receiveMessage())
        filename = contents
        canTransfer = self.checkTransfer(filename)

        if(canTransfer):
            if(os.path.isFile(filename)):
                fs.sendMessage(b"NO")
                conn.shutdown(socket.SHUT_WR)
            else:
                fs.sendMessage(b"OK")
        else:
            os.write(2,("File in Transfer").encode())
            conn.shutdown(socket.SHUT_WR)

        fd = os.open(filename, os.O_CREAT | os.O_WRONLY)
        os.write(fd,fs.receiveMessage().encode())
        os.close(fd)
        self.endTransfer(filename)

        self.conn.shutdown(socket.SHUT_WR)
