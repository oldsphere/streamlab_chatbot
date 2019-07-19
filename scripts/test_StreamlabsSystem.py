import sys
import json
import os
import ctypes
import codecs

ScriptName = "Test"
Website = ""
Description = "No"
Creator = "Me"
Version = "1.2.0"

def Init():
    Parent.Log('Test', 'Initialiced')

def Execute(data):
    Parent.Log('Test', 'Data Received')
    Parent.Log('Test', '    UserName: %s' % data.User)
    Parent.Log('Test', '    UserId: %s' % data.UserId)
    Parent.Log('Test', '    Message: %s' % data.Message)


def Tick():
    Parent.Log('Test', 'Tick')

