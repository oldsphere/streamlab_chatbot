#!/usr/bin/python
# Date: 18/07/2019 13:51:58
# Description:
#   StreamLabs Chatbot Emulator

import os
import random
import datetime

class ChatbotParent():
    def __init__(self):
        self._cooldown = dict()
        self._name = 'ChatBot'

    def SendStreamMessage(self, message):
        print(self._name +': ' + message)

    def SendStreamWhisper(self, target, message):
        print(self._name + ':' + '\w %s %s' % (target, message))

    @staticmethod
    def GetRandom(min_v, max_v):
        return random.randint(min_v, max_v)

    @staticmethod
    def Log(scriptName, message):
        print('LOG: (%s) - %s' % (scriptName, message))

    @staticmethod
    def PlaySound(soundPath, volume):
        soundFile = os.path.basename(soundPath)
        print('$ Playing %s file at %i' % (soundFile, volume))


    # Cooldown managment:

    @staticmethod
    def _composeCmdName(scriptName, command, userId=None):
        cmdName = '%s_%s'  % (scriptName, command)
        if userId:
            cmdName += '_%i' % userId
        return cmdName

    def _AddCooldown(self, cmdName, seconds):
        self._cooldown[cmdName] = CmdCooldown(seconds)

    def _IsOnCooldown(self, cmdName):
        if cmdName in self._cooldown.keys():
            if not self._cooldown[cmdName].isActive():
                del self._cooldown[cmdName]
                return False
            return True
        return False

    def _GetCooldownDuration(self, cmdName):
        if cmdName in self._cooldown.keys():
            if not self._cooldown[cmdName].isActive():
                del self._cooldown[cmdName]
                return 0
        return self._cooldown[cmdName].GetRemainingTime()

    def AddCooldown(self, scriptName, command, duration):
        cmdName = self._composeCmdName(scriptName, command)
        self._AddCooldown(cmdName, duration)

    def IsOnCooldown(self, scriptName, command):
        cmdName = self._composeCmdName(scriptName, command)
        return self._IsOnCooldown(cmdName)

    def GetCooldownDuration(self, scriptName, command):
        cmdName = self._composeCmdName(scriptName, command)
        return self._GetCooldownDuration(cmdName)

    def AddUserCooldown(self,scriptName, command, userId, duration):
        cmdName = self._composeCmdName(scriptName, command, userId)
        self._AddCooldown(cmdName, duration)

    def IsOnUserCooldown(self,scriptName, command, userId):
        cmdName = self._composeCmdName(scriptName, command, userId)
        return self._IsOnCooldown(cmdName)

    def GetUserCooldownDuration(self,scriptName, command, userId):
        cmdName = self._composeCmdName(scriptName, command, userId)
        return self._GetCooldownDuration(cmdName)


class CmdCooldown:
    def __init__(self, duration):
        self._start = self.now()
        self._end = self._start + datetime.timedelta(seconds=duration)

    @staticmethod
    def now():
        return datetime.datetime.now()

    def isActive(self):
        return self.now() < self._end

    def GetRemainingTime(self):
        return (self._end - self.now()).seconds

