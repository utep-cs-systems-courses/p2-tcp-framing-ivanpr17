class framedSocket:
    def __init__(self,connectedSocket):
        self.cs = connectedSocket
        self.buffer = ""

    def sendMessage(self,message):
        lengthStr = str(len(message)) + ':'
        lengthBA = bytearray(lengthStr, 'utf-8')
        message = lengthBA + message
        while len(message):
            sent = self.cs.send(message)
            message = message[sent:]

    def receiveMessage(self):
        message = ""
        self.buffer += self.cs.recv(100).decode()

        left,right = partition(self.buffer)
        message += self.buffer[left:right]
        self.buffer = self.buffer[right:]

        while(self.buffer):
            left,right = partition(self.buffer)
            if len(self.buffer) < right:
                self.buffer += self.cs.recv(100).decode()
            else:
                message += self.buffer[left:right]
                self.buffer = self.buffer[right:]
        return message

    def partition(string):
        num=""
        while(string[0].isdigit()):
            num += string[0]
            string = string[1:]

        if num.isnumeric():
            left = len(num)+1
            right = int(num) + (len(num)+1)
            return left,right
        else:
            return None
