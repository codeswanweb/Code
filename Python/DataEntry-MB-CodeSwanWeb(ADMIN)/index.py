import os
import sys
import queue
import datetime
import threading
import time
import random
from time import sleep

print("Enter Wanted ID:")
idn = input()
os.makedirs("002/logs/" + idn)
print("Logged!")
sleep(2)
print("Enter Data Now")
de = input()
def writet():
    f = open("002/logs/" + idn + "/log.txt", "w")
    print("Written")
    def write2():
        f = open("002/logs/" + idn + "/log.txt", "w")
        f.write(de + "\n")
        print("Written")
    write2()
    def ask1():
        print("Finish? Or Write More")
        print("Yes or No")
        yon = input()
        if yon == "Yes":
            write2()
        elif yon == "yes":
            write2()
        elif yon == "y":
            write2()
        elif yon == "No":
            print("Done")
        elif yon == "no":
            print("Done")
        elif yon == "n":
            print("Done")
    ask1()
    def readid():
        print("Type folder ID:")
        fid = input()
        f = open("002/logs/" + fid + "/log.txt", "r")
        file_contents = f.read()
        print("File Contents: \n" + "   " + file_contents)
        f.close()
    def ask2():
        print("Read File?")
        print("Yes or No")
        yon = input()
        if yon == "Yes":
            readid()
        elif yon == "yes":
            readid()
        elif yon == "y":
            readid()
        elif yon == "No":
            print("Done")
        elif yon == "no":
            print("Done")
        elif yon == "n":
            print("Done")
        else:
            print("Please Type A correct answer")
            ask2()
    ask2()
writet()