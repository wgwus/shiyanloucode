#!/usr/bin/env python3
import sys
try:
    arg = sys.argv[1]
    arg = int(arg)
    shudPatix = arg - 3500
except ValueError:
    print("valueerror")
if shudPatix<=1500:
    shudmath = shudPatix*0.03
    print('{:.2f}'.format(shudmath))

if 1500<shudPatix<=4500:
    shudmath = shudPatix*0.1-105
    print('{:.2f}'.format(shudmath))
if 4500< shudPatix<=9000:
    shudmath = shudPatix*0.2-555
    print('{:.2f}'.format(shudmath))
if 9000<shudPatix<=35000:
    shudmath = shudPatix*0.25-1005
    print('{:.2f}'.format(shudmath))
if 35000<shudPatix<=55000:
    shudmath = shudPatix*0.30-2755
    print('{:.2f}'.format(shudmath))
if 55000<shudPatix<=80000:
    shudmath = shudPatix*0.35-5505
    print('{:.2f}'.format(shudmath))
if 80000<shudPatix:
    shudmath = shudPatix*0.45-13505
    print('{:.2f}'.format(shudmath))
