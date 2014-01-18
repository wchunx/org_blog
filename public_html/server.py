import SimpleHTTPServer
import SocketServer
import cgi

host = ''
port = 8090

class simpleHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_POST(self):
        try:
            form = cgi.FieldStorage(
                                    fp = self.rfile,
                                    headers = self.headers,
                                    environ = {
                                               'REQUEST_METHOD':'POST',
                                               'CONTENT_TYPE':self.headers.getheader('current-type')
                                               }    
                                    )

            print form

        except IOError:
            self.send_error(404, ' POST error');
 
conn = SocketServer.TCPServer((host, port), simpleHandler)

print 'start server at port:', port

conn.serve_forever()
