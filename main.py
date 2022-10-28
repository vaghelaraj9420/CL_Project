from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "127.0.0.1"
PORT = 8000

class PythonHTTP(BaseHTTPRequestHandler):

    def do_GET(self):                               # for controlling get requests 
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # opening the text file
        with open('index.html','r') as file:
        
            while True:
            
                # Get next line from file
                line = file.readline()
            
                # if line is empty
                # end of file is reached
                if not line:
                    break
                # print(line)
                self.wfile.write(bytes(line,"utf-8"))


            # for line in file:
        
            #     # reading each word        
            #     for word in line.split():
        
            #         # displaying the words           
            #         # print(word) 
            #         self.wfile.write(bytes(word,"utf-8"))

        # self.wfile.write(bytes("<html><body><h1>Hello World!</h1></body></html>", "utf-8"))
        # self.wfile.write(bytes("index.html", "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        # self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))

        data = self.rfile.read(int(self.headers.getheader('Content-Length')))
        empty = [data]
        with open('processing.txt', 'wb') as file:
            for item in empty:
                file.write("%s\n" % item)

        file.close()
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")


server = HTTPServer((HOST, PORT), PythonHTTP)
print("Server now running....")

server.serve_forever()
server.server_close()
print("Server Stopped!") 
