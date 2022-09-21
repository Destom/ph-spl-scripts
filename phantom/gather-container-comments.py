#!/usr/local/bin/python3

from pprint import pprint
from xml.etree.ElementTree import tostring
import requests

#disable insecure connection warnins
import urllib3
urllib3.disable_warnings()


    ####    Things to set   ####
hostname = 'XXXXXXXX'
port = 8443
protocol = 'https' 
secure_connection = False
endpoint = 'rest/container/'
username = 'XXXXXX'
password = 'XXXXXX' 

    ### itilailising memory ###
success_count = 0
fail_count = 0 

for x in range(101,1102):
    url = protocol + '://' + hostname + ':' + str(port) + '/' + endpoint + '/' + str(x) + '/' +'comments'
    results = requests.get(url, verify=secure_connection, auth=(username,password) )
    comment = str(results.json()['data'][0]['comment'])
    print(comment)
    if comment.find('This is the container: /mission/') == 0:
        success_count +=1
    else:
        fail_count += 1 

print(f'''
We found {success_count} successes
we found {fail_count} failures
''')
