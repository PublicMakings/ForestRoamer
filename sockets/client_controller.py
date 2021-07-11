#import the tkinter module for the GUI and input control
import tkinter as tk
from tkinter import *

import socket
import sys

#variables
Drive = 'idle'
Steering = 'idle'




#setting up the functions to deal with key presses
def KeyUp(event):
    Drive = 'forward'
    drivelabel.set(Drive)
    labeldown.grid_remove()
    labelup.grid(row=2, column=2)
def KeyDown(event):
    Drive = 'reverse'
    drivelabel.set(Drive)
    labelup.grid_remove()
    labeldown.grid(row=4, column=2)
def KeyLeft(event):
    Steering = 'left'
    steeringlabel.set(Steering)
    labelright.grid_remove()
    labelleft.grid(row=3, column=1)
def KeyRight(event):
    Steering = 'right'
    steeringlabel.set(Steering)
    labelleft.grid_remove()
    labelright.grid(row=3, column=3)
def key(event):
    if event.keysym == 'Escape':
        root.destroy()

#setting up the functions to deal with key releases
def KeyReleaseUp(event):
    Drive = 'idle'
    drivelabel.set(Drive)
    labelup.grid_remove()
def KeyReleaseDown(event):
    Drive = 'idle'
    drivelabel.set(Drive)
    labeldown.grid_remove()
def KeyReleaseLeft(event):
    Steering = 'idle'
    steeringlabel.set(Steering)
    labelleft.grid_remove()
def KeyReleaseRight(event):
    Steering = 'idle'
    steeringlabel.set(Steering)
    labelright.grid_remove()

#connection functions
def AttemptConnection():
    connectionmessagetempvar = connectionmessagevar.get()
    connectionmessagevar.set(connectionmessagetempvar + "\n" + "Attempting to        connect...") 

def transmit(event):
    HOST, PORT = "localhost", 9999
    data = "this here data wont send!! "


    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
         # Connect to server and send data
         sock.connect((HOST, PORT))
         sock.sendall(bytes(data + "\n", "utf-8"))

         # Receive data from the server and shut down
         received = str(sock.recv(1024), "utf-8")
    finally:
         sock.close()

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))




