import SimpleHTTPServer
import BaseHTTPServer
import SocketServer
import urllib
import cgi
import sys

PORT = 8000
dict = {}

class KeyServer(BaseHTTPServer.BaseHTTPRequestHandler):


    def do_GET(self):
        print "got request for:", self.path
        value = self.get_value()
        print "found: ", value
        if value == None:
            self.send_response(404)
            self.end_headers()
        else:
            self.send_response(200)
            self.send_header("Status", "OK")
            self.end_headers()
            self.wfile.write(value)

    def do_POST(self):
        global dict
        print "doing POST"

        # Parse the form data posted
        form = cgi.FieldStorage(
            fp=self.rfile, 
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })

        # begin response
        self.send_response(200)
        self.send_header("Status", "OK")
        self.end_headers()

        # parse values
        for field in form.keys():
            global dict
            item = form[field]
            # write item to store
            dict[field] = item.value

            print "store now contains ",len(dict), " items"
            for key in dict:
                print key,":", dict[key]

    def get_value(self):
        return dict.get(self.path, None)

if len(sys.argv) == 2:
    PORT = sys.argv[1]

httpd = SocketServer.TCPServer(('', int(PORT)), KeyServer)
print "serving at port", PORT
httpd.serve_forever()
