import SimpleHTTPServer
import BaseHTTPServer
import SocketServer
import urllib

PORT = 8000

class KeyServer(BaseHTTPServer.BaseHTTPRequestHandler):
    def do_GET(self):
        pass

httpd = SocketServer.ForkingTCPServer(('', PORT), KeyServer)
print "serving at port", PORT
httpd.serve_forever()
