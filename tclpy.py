#!/usr/bin/env python
import subprocess
from tkinter import *
import time
# rint('adddsd')


def p1():
    print("AODV")
    subprocess.Popen(
        ['ns', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless-AODV.tcl']).wait()

    subprocess.Popen(
        ['awk', '-f', '/mnt/d/Downloads/Compressed/AODV-master/Project/grphCalc.awk', 'wireless-AODV.tr']).wait()

    subprocess.Popen(
        ['nam', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless.nam']).wait()


def p2():
    print("AODV")
    print("\n\n\n")
    subprocess.Popen(
        ['ns', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless-AODV.tcl']).wait()

    a = subprocess.Popen(
        ['awk', '-f', '/mnt/d/Downloads/Compressed/AODV-master/Project/grphCalc.awk', 'wireless-AODV.tr']).wait()
    # print("end")
    n = subprocess.Popen(
        ['nam', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless.nam']).wait()
    print("\n\n\n")


def aomdv():
    print("AOMDV")
    print("\n\n\n")
    t = subprocess.Popen(
        ['ns', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless-AOMDV.tcl']).wait()
    a = subprocess.Popen(
        ['awk', '-f', '/mnt/d/Downloads/Compressed/AODV-master/Project/grphCalc.awk', 'wireless-AOMDV.tr']).wait()
    n = subprocess.Popen(
        ['nam', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless.nam']).wait()
    # time.sleep(5)
    print("\n\n")


def dsdv():
    print("DSDV")
    print("\n\n\n")
    t = subprocess.Popen(
        ['ns', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless-DSDV.tcl']).wait()
    a = subprocess.Popen(
        ['awk', '-f', '/mnt/d/Downloads/Compressed/AODV-master/Project/grphCalc.awk', 'wireless-DSDV.tr']).wait()
    n = subprocess.Popen(
        ['nam', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless.nam']).wait()
    # time.sleep(5)
    print("\n\n")


def dumb():
    print("Dumb Agent")
    print("\n\n\n")
    t = subprocess.Popen(
        ['ns', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless-Dumb Agent.tcl']).wait()
    a = subprocess.Popen(
        ['awk', '-f', '/mnt/d/Downloads/Compressed/AODV-master/Project/grphCalc.awk', 'wireless-Dumb Agent.tr']).wait()
    n = subprocess.Popen(
        ['nam', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless.nam']).wait()
    print("\n\n\n")

# def wirelessDumbAgenttcl():
# 	subprocess.Popen(['ns', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless-Dumb Agent.tcl'])

# def wirelessDSDVtcl():
# 	subprocess.Popen(['ns', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless-DSDV.tcl'])

# def wirelessAODVtcl():
# 	subprocess.Popen(['ns', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless-AODV.tcl'])

# def wirelessAOMDVtcl():
# 	subprocess.Popen(['ns', '/mnt/d/Downloads/Compressed/AODV-master/Project/wireless-AOMDV.tcl'])


# def comparisonResult():
# 	subprocess.Popen(['awk','-f', '/mnt/d/Downloads/Compressed/AODV-master/Project/grphCalc.awk', 'wireless.tr'])
root = Tk()
root.title("AODV Protocol Simulation")

root.geometry('500x500')

#btn=Button(root, text= 'Main Protocol' , bd=5 , command = p1).place(x=600,y=20)

btn1 = Button(root, text='AODV', bd=5, command=p2).place(x=250, y=100)


btn3 = Button(root, text='AOMDV', bd=5, command=aomdv).place(x=250, y=200)

btn4 = Button(root, text='DSDV', bd=5, command=dsdv).place(x=250, y=300)

btn3 = Button(root, text='Dumb Agent', bd=5, command=dumb).place(x=250, y=400)

# btn3=Button(root, text= 'wireless-AOMDV.tcl' , bd=5, command = wirelessAOMDVtcl).place(x=600, y=400)

#btn2=Button(root, text= 'Comparison' , bd=5,command=p2).place(x=600,y=600)

root.mainloop()
