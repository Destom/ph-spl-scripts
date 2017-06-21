x = 2000
y = 3200
l= []
for number in range(x,y):
    if (number % 7 == 0) and (number % 5 !=0):
        l.append(str(number))
print (",".join(l))
