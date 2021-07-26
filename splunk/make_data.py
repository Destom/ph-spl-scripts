#log_type can be big or small
number_of_events=50
flie_location='/tmp/'
log_type='big'
#file_name will have a number appended to it for smaller files
file_name='loogy'
#what log format do you want, we currently have time,latin or generic
log_format='generic'



import os, time, random, string
from datetime import datetime

login_msg = ['failed','successful']
domains = ['com','pl','org','gov','ru','net']
companies = ['splunk','dupa','apple','amazon','cia']
orders_msg = ['completed successfully','completed partially','failed','timed out']

def getstamp():
    return datetime.now()

def getoldstamp():
    return datetime.now().replace(year=2018)

def getepoch():
    return str(time.time()).split('.')[0]

def getPseudoEpoch():
    number = "1"
    number += str(random.randrange(4,7))
    for i in range(8):
        number += str(random.randrange(0,10))
    return number

def getoldepoch():
    return str(time.time() - 86400000).split('.')[0]

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def type_select(log_format):
    selector = log_format
    if selector == "time":
      number = [4]
    elif selector == "latin":
      number = [1,2]
    elif selector == "generic":
      number = [3,5,6]
    return number

def write_message(number):
    if number == 1 :
        return f"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam {getoldstamp()}, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
    if number ==2 :
        return f"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore {getoldstamp()} magna aliqua. Ut enim ad minim veniam {getoldstamp()}, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n"
    if number == 3 :
        return f"{getstamp()} login {randomString(random.randrange(4,10))} {random.choice(login_msg)} on server={randomString(random.randrange(4,10))}.{random.choice(companies)}.{random.choice(domains)}\n"
    if number ==4 :
        return f"Two years ago the time was: {getoldstamp()}, but now the time is {getstamp()}\n"
    if number ==5 :
        return f"{getoldepoch()} was the last time user {randomString(random.randrange(4,10))} had a {random.choice(login_msg)} login\n"
    if number ==6 :
        return f"{getepoch()} Connection attempt made to server with IP {random.randrange(1,254)}.{random.randrange(1,254)}.{random.randrange(1,254)}.{random.randrange(1,254)} {random.choice(orders_msg)}. Please notify {random.choice(companies)}\n"

print('im working here')
number = type_select(log_format)

if log_type == 'big':
    for i in range(number_of_events):
        numbers = random.choice(number)
        with open(flie_location+file_name+'.log', 'a') as log_file:
            log_file.write(write_message(numbers))

if log_type == 'small':
    for i in range(number_of_events):
        numbers = random.choice(number)
        with open(flie_location+file_name+str(i)+'.log', 'a') as log_file:
             log_file.write(write_message(numbers))
