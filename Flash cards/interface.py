import random
ports = {}

dict2 = open("ports" , "r")

mydict =  {"string 1":"this is a string ","string 2":"this is also a sting "}
dict_tup = tuple(mydict.keys())
dict_length = len(dict_tup)
card = random.randint(0,(dict_length-1))

flash_card = dict_tup[card]

print (flash_card)
print (mydict[flash_card])


test = dict2.read()
dict_card = dict(test)
print (test)
