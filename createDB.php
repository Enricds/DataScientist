credentials = {"credentials":
{
  "username": "61e62b6c-03f5-446b-a7d5-96176cda0dfe-bluemix",
  "password": "e9f3a42b5f440b43b13b31d1ece92dba889f63937630eebe968366a9929961aa",
  "host": "61e62b6c-03f5-446b-a7d5-96176cda0dfe-bluemix.cloudant.com",
  "port": 443,
  "url": "https://61e62b6c-03f5-446b-a7d5-96176cda0dfe-bluemix:e9f3a42b5f440b43b13b31d1ece92dba889f63937630eebe968366a9929961aa@61e62b6c-03f5-446b-a7d5-96176cda0dfe-bluemix.cloudant.com"
} }

username = credentials['credentials']['username']
password = credentials['credentials']['password']
host = credentials['credentials']['host']
url = credentials['credentials']['url']

print username
print password
print host
print url

import os
import json
import requests
from cloudant.account import Cloudant
from cloudant.result import Result

#---------------------------------------------------------------------------------------------------------------#
# Authentication details below are extracted from Bluemix Credentials - in this example it is hard coded as this is being
# run external to being hosted on bluemix
#---------------------------------------------------------------------------------------------------------------#
USERNAME = username
PASSWORD = password
auth = ( USERNAME, PASSWORD )
hostname = host

#---------------------------------------------------------------------------------------------------------------#
# Name of database to create
# and the connectection string for cloudant in bluemix
#---------------------------------------------------------------------------------------------------------------#

my_database = 'my_exampledb'

client = Cloudant(USERNAME, PASSWORD, url='https://'+hostname)
client.connect()


#---------------------------------------------------------------------------------------------------------------#
# The code below creates a dataabase (named in the my_database variable)
#---------------------------------------------------------------------------------------------------------------#
requests.put( url + '/' + my_database, auth=auth )
