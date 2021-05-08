from os import read

next = 0
limit = 0

def my_getChar():
    global next
    global limit

    if next == limit:
        next = 0
        limit = read(0,100)

        if limit == 0:
            return None
    if next < len(limit) - 1:
        c = chr(limit[next])
        next +=1
        return c
    else:
        return None

def my_getLine():
    global next
    global limit
    line = ""
    char = my_getChar()
    while(char!= '' and char != None):
        line += char
        char = my_getChar()
    next = 0
    limit = 0
    return line

def parseTCPInput(string):
    tokens = string.split()
    command = tokens[0]
    localfile = tokens[1]
    remotefile = tokens[2]
    return command,localfile,remotefile
