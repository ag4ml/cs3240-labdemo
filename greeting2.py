#!/usr/bin/python3.4
import random

def greeting2(msg):
    print(msg*(random.randint(1,5)))

if __name__=='__main__':
    greeting2("hello")
