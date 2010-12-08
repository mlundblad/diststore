import sys
import httplib

# TODO: read this from a config file
servers = ["localhost:8000"]

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
            return resp.read()
        else:
            print "Could not read data from key store server"
            return None


if len(sys.argv) <> 2:
    print "Usage: keystore <key>"
    sys.exit()

key_store = KeyStore()
key = sys.argv[1]
print "Lookup key: ", key
value = key_store.lookup_key(key)

if value == None:
    print "Key not found"
else:
    print "Found value: ", value
