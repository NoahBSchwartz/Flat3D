import bpy
import socket
import os
from _thread import *
import math
import mathutils
import struct
ServerSocket = socket.socket()
host = '10.0.0.40'
port = 8080
senX = "0"
senY = "0"
sen2Y = 0
sen2X = 0
try:
    ServerSocket.bind((host, port))
except socket.error:
    ServerSocket.close()
    raise RuntimeError("Stopping the script here") 
ServerSocket.listen(5)
def threaded_client():
    global Client
    Client.send(str.encode('Welcome to the Server'))
    bpy.app.timers.register(threaded_client_loop)
    
def threaded_client_loop():
    global Client
    global senX
    global senY
    global sen2Y
    global sen2X
    data = Client.recv(2048)
    reply = 'Server Says: ' + data.decode('utf-8')
    senY = data.decode('utf-8')[3:]
    senX = data.decode('utf-8')[:-3]
    try:
       senX = int(senX)
       sen2X = senX
       senY = int(senY)
       sen2Y = senY
    except:
        senX = sen2X
        senY = sen2Y
    camera = bpy.data.objects['Camera']
    looking_direction = camera.location - mathutils.Vector(((senX/9), 90.0, -60.0))#(senX, senY, 0.0))
    rot_quat = looking_direction.to_track_quat('Z', 'Y')
    camera.rotation_euler = rot_quat.to_euler()
    camera.location = rot_quat @ mathutils.Vector((0.0, 0.0, 10.0))
    return .05

def connectionChecker():
        global threadCount
        global Client
        Client, address = ServerSocket.accept()
        threaded_client()
        threadCount += 1
        return .05
bpy.app.timers.register(connectionChecker)