#!/usr/bin/env python3
def change():
    global a
    a = 90
    print(a)
a = 9
print("befort", a)
print("inside", end=' ')
change()
print ("after", a)
