import SimpleHTTPServer
import BaseHTTPServer
import SocketServer
import urllib
import cgi

PORT = 8000
dict = {}

class KeyServer(BaseHTTPServer.BaseHTTPRequestHandler):


    def do_GET(self):
        print "got request for:", self.path
        print "found: ", self.get_value()

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
        

httpd = SocketServer.TCPServer(('', PORT), KeyServer)
print "serving at port", PORT
httpd.serve_forever()
