#!/usr/bin/python
# Date: 18/07/2019 13:51:58
# Description:
#   StreamLabs Chatbot Emulator

import os
import random
import datetime

class ChatbotParent():
    def __init__(self, stream_type='twitch'):
        self._cooldown = dict()
        self._name = 'ChatBot'
        self._type = stream_type

        # Auxiliar methods
        self._bank = Bank()
        self._userDB = UserDB()
        self._permissions = {}


    def set_bank(self, bank_dict):
        ''' Set the bank account to a fixed value '''
        self._bank = Bank(bank_dict)

    def set_userIds(self, userIds_dict):
        ''' Set the UserDB '''
        self._userDB = UserDB(userIds_dict)

    def set_permissions(self, permissions_dict):
        ''' Set the permissions '''
        self._permissions = permissions_dict


    # Main methods

    def GetUserName(self, userID):
        self._userDB.GetUserName(userID)

    def GetUserId(self, username):
        userID = self._userDB.GetUserID(username)
        if not userID:
            return self._userDB.AddUser(username)
        return userID

    def SendStreamMessage(self, message):
        print(self._name +': ' + message)

    def SendStreamWhisper(self, target, message):
        print(self._name + ':' + '\w %s %s' % (target, message))

    # Misc methods

    @staticmethod
    def GetRandom(min_v, max_v):
        return random.randint(min_v, max_v)

    @staticmethod
    def Log(scriptName, message):
        print('LOG: (%s) - %s' % (scriptName, message))

    def GetHours(self, UserId):
        ''' Return the user hours of watching '''
        pass

    def GetRank(self, UserId):
        ''' Return the user ranking '''
        pass

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


    # Checking permissions
    def HasPermission(self, userId, permission, info):
        permission_list = self._permission.get(permission,  [])
        return self.GetUserName(userId) in permission_list


    # Currency manipulation:
    def AddPoints(self, userId, username, amount):
        self._bank.AddPoints(username, amount)

    def RemovePoints(self, userId, username, amount):
        self._bank.RemovePoints(username, amount)

    def GetPoints(self, userId):
        return self._bank.GetPoints(self.GetUserName(userId))



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


class Bank:
    def __init__(self, data={}):
        self._data = data

    def AddPoints(self, user, amount):
        if user in self._data.keys():
            self._data[user] += amount
        else:
            self._data[user] = amount

    def RemovePoints(self, user, amount):
        self.AddPoints(user, -amount)

    def GetPoints(user):
        return self._data.get(user, 0)


class UserDB:
    def __init__(self, data={}):
        self._data = data

    def GetUsername(self, userID):
        return self._data.get(userID, '')

    def GetUserID(self, username):
        userId = [uid for uid in self._data.keys()
                  if self._data[uid] == username]
        return userId[0] if userId else 0

    def AddUser(self, username):
        ''' Assign a non repited UserID and return it '''
        maxId = max(list(self._data.keys())) if self._data.keys() else 1
        self._data[maxId+1] = username
        return maxId+1

