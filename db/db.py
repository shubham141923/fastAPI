import urllib.parse
from pymongo import MongoClient

username1 = urllib.parse.quote_plus('cmrslpx1b')
password1 = urllib.parse.quote_plus("l@HdEvS#)TR&7dC")
client1 = MongoClient('mongodb://%s:%s@api.srvr2px.cyberads.io/?authSource=admin' % (username1, password1))