# coding: utf-8
import clr
import sys
import json
import os
import ctypes
import codecs

from BasicApp import CoinFlip

ScriptName = "Coin Minigame"
Website = "http://www.github.com/Bare7a/Streamlabs-Chatbot-Scripts"
Description = "Coin Minigame for Streamlabs Bot"
Creator = "Bare7a"
Version = "1.2.8"

def ScriptToggled(state):
    return

def Init():
    global settings, App

    App = CoinFlip(Parent)
    App.name = ScriptName
    App.cmd = '!flip'
    App.cost = 0
    App.cooldown = 0
    App.usercooldown = 300

    App.recompensa = 2

def Execute(data):

    if not App.isValidData(data):
        return

    userId = data.User
    username = data.UserName

    if not App.hasPoints(userId):
        Parent.SendStreamMessage(
            "Te has flipao @%s, no tienes puntos" % username
        )
        return

    if App.isOnCooldown(userId):
        Parent.SendStreamMessage(
            "Te toca esperar @%s" % username)
        return

    App.flip(userId, username)
    App.AddUserCooldown(userId)
    App.AddCooldown()

    return

def ReloadSettings(jsonData):
    Init()
    return

def OpenReadMe():
    location = os.path.join(os.path.dirname(__file__), "README.txt")
    os.startfile(location)
    return

def Tick():
    return
