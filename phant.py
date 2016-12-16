#!/usr/bin/python
import httplib, urllib   # http and url libs used for HTTP POSTs

class Phant(object):
    def __init__(self, pubkey, pvtkey):
        self.server = "data.sparkfun.com" # base URL of your feed
        self.publicKey = pubkey # "zD9obXl4K3UM1E0MY5q2" # public key, everyone can see this
        self.privateKey = pvtkey #"yourprivatekey"  # private key, only you should know
        self.fields = ["humidity", "pressure", "temp"] # Your feed's data fields

    def post_data(self, humidity, pressure, temp):
        data={} # Create empty set, then fill in with our fields:
        data[self.fields[0]] = humidity
        data[self.fields[1]] = pressure
        data[self.fields[2]] = temp
        # Next, we need to encode that data into a url format:
        params = urllib.urlencode(data)
        # Now we need to set up our headers:
        headers = {} # start with an empty set
        # These are static, should be there every time:
        headers["Content-Type"] = "application/x-www-form-urlencoded"
        # headers["Connection"] = "close"
        headers["Content-Length"] = len(params) # length of data
        headers["Phant-Private-Key"] = self.privateKey # private key header

        # Now we initiate a connection, and post the data
        c = httplib.HTTPConnection(self.server)
        # Here's the magic, our reqeust format is POST, we want
        # to send the data to data.sparkfun.com/input/PUBLIC_KEY.txt
        # and include both our data (params) and headers
        c.request("POST", "/input/" + self.publicKey, params, headers)
        r = c.getresponse() # Get the server's response and print it
        print r.status, r.reason