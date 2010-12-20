import sys
import httplib
import urllib

# TODO: read this from a config file
servers = ["localhost:8000"]

def usage():
    print "Usage: keystore get <key> [servers]"
    print "       keystore set <key> <value> [servers]"
    sys.exit()


class KeyStore:

    def lookup_key(self, key):
        num_servers = len(servers)
        # compute an index given a the key hash
        index = hash(key) % num_servers
        
        print "Using server# ", index
        conn = httplib.HTTPConnection(servers[index])
        conn.request("GET", key)
        resp = conn.getresponse()
        
        if resp.status == 200 and resp.reason == "OK":
            value = resp.read()
            return value
        else:
            print "Could not read data from key store server"
            return None

    def set_key(self, key, value):
        num_servers = len(servers)
        # compute an index given a the key hash
        index = hash(key) % num_servers
        
        print "Using server# ", index
        conn = httplib.HTTPConnection(servers[index])
        headers = {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"}
        params = urllib.urlencode({key: value})
        conn.request("POST", "/", params, headers)
        resp = conn.getresponse()

        if resp.status == 200 and resp.reason == "OK":
            pass
        else:
            print "Could not add value to server"


if len(sys.argv) < 3 or len(sys.argv) > 5:
    usage()

key_store = KeyStore()
if sys.argv[1] == "get":
    if len(sys.argv) <> 3 and len(sys.argv) <> 4:
        usage()
    if len(sys.argv) == 4:
        # get server list from command line
        servers = sys.argv[3].split(",")
    key = sys.argv[2]
    print "Lookup key: ", key
    value = key_store.lookup_key(key)

    if value == None:
        print "Key not found"
    else:
        print "Found value: ", value

elif sys.argv[1] == "set":
    if len(sys.argv) <> 4 and len(sys.argv) <> 5:
        usage()
    if len(sys.argv) == 5:
        # get server list from command line
        servers = sys.argv[4].split(",")
    key = sys.argv[2]
    value = sys.argv[3]
    print "Setting key: ", key, " to: ", value
    key_store.set_key(key, value)

