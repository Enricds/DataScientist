credentials = {"credentials":
{
  "username": "fe1b6cb2-7773-4733-ad2d-97d9228b178f-bluemix",
  "password": "0c607005ec59e5cfb74cb8bf51f3b1c69a57158539f8506feaa79bc60b6af058",
  "host": "fe1b6cb2-7773-4733-ad2d-97d9228b178f-bluemix.cloudant.com",
  "port": 443,
  "url": "https://fe1b6cb2-7773-4733-ad2d-97d9228b178f-bluemix:0c607005ec59e5cfb74cb8bf51f3b1c69a57158539f8506feaa79bc60b6af058@fe1b6cb2-7773-4733-ad2d-97d9228b178f-bluemix.cloudant.com"
}
}

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
from cloudant.client import Cloudant
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
