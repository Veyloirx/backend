
server RPCClient('localhost', 8080)
server.connect()
print(server.add(5,6))
print(server.add(5,6))
print(server.hi())
server.disconnect()