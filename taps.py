import json
import urllib2
import pymongo


# connect to mongo
connection = pymongo.Connection("mongodb://localhost", safe=True)

# get a handle to the 3taps database

db=connection.taps #if not exists, will create empty db
data = db.data #if not exists, will create data collection

# get the 3taps api data
taps_data = urllib2.urlopen("http://search.3taps.com/?rpp=100&retvals=body,price&metro=USA-STL&category=SAPL&source=CRAIG&auth_token=7db0b67453620552e2c695855ae41c6e")

# parse the json into python objects
parsed = json.loads(taps_data.read())

#insert bluk object into mongo
data.insert(parsed)


##QUERY DATA##

#use taps
#show collections
#db.taps.find()
