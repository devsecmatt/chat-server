import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    '''
    Request Handler for the server. 

    Instantiated once per connection, and overrides the handle() method
    to communicate to the client
    '''

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("Received from {}:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but in upper case
        self.request.sendall(self.data.upper())

class MyTCPStreamHandler(socketserver.StreamRequestHandler):
    # this version of the handler makes use of streams, where readline()
    # calls recv() until a newline is encountered
    def handle(self):
        # self.rfile is a file-like object created by the handler,
        # enabling us to use readline() instead of raw recv()
        self.data = self.rfile.readline().strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # Likewise, self.wfile is a file-like object used to write back to the client
        self.wfile.write(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    
    # create server and bind to HOST:PORT
    with socketserver.TCPServer((HOST, PORT), MyTCPStreamHandler) as server:
        # activate the server
        # runs forever until interupted with CTRL+C
        server.serve_forever()