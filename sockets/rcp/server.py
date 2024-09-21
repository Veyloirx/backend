from rpc import RPCServer

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def hi():
    return "Saludos humano"

server = registerMethod(add)
server = registerMethod(sub)
server = registerMethod(hi)
server.run()