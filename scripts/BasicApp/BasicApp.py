# coding: utf-8

class BasicApp:
    def __init__(self, Parent):
        self._Parent = Parent
        self.name = None
        self.cmd = None
        self.permission = 'Everyone'
        self.onlyLive = True

        self.cost = 0
        self.cooldown = 0
        self.usercooldown = 0

    def isValidData(self, data):
        ''' Check general validation '''

        isChat  = data.IsChatMessage()
        hasCmd  = data.GetParam(0).lower() == self.cmd
        hasPermission = self._Parent.HasPermission(data.User, self.permission, '')
        onlyLive = (self.onlyLive and self._Parent.IsLive()) or \
                    not self.onlyLive

        return isChat and hasCmd and hasPermission and onlyLive

    def hasPoints(self, userId, points=0):
        ''' Check puntuation of the user '''
        if not self.cost:
            return True
        if not points:
            points = self.cost
        return self._Parent.GetPoints(userId) > points

    def isOnCooldown(self, userId):
        ''' check valid cooldown '''
        if self._Parent.HasPermission(userId, "Admin", ''):
            return False

        if not self.cooldown and not self.usercooldown:
            return False

        return self._Parent.IsOnCooldown(self.name, self.cmd) or \
               self._Parent.IsOnUserCooldown(self.name, self.cmd, userId)

    def AddUserCooldown(self, userId):
        if self.usercooldown:
            self._Parent.AddUserCooldown(self.name,
                                         self.cmd,
                                         userId,
                                         self.usercooldown)

    def AddCooldown(self):
        if self.cooldown:
            self._Parent.AddCooldown(self.name,
                                     self.cmd,
                                     self.usercooldown)


class CoinFlip(BasicApp):
    def __init__(self, Parent):
        super().__init__(Parent)

        self.recompensa = 1

    def flip(self, userId, username):
        ''' Tirar una moneda '''

        coin = self._Parent.GetRandom(0,2)
        if coin == 0:
            reward = self.cost * self.recompensa
            self._Parent.SendStreamMessage("Cara, @%s gana" % username)
            self._Parent.SendStreamMessage(
                "@%s, tienes %i$ más en tu cuenta" % (username, reward)
            )
            self._Parent.AddPoints(userId, username, reward)
        else:
            self._Parent.SendStreamMessage("Cruz, @%s pierde" % username)
            self._Parent.SendStreamMessage(
                "@%s, has perdido %i$" % (username, self.cost)
            )
            self._Parent.RemovePoints(userId, username, self.cost)

        self._Parent.SendStreamWhisper(
            username,
            "Ahora @%s tiene %i$" % (username, self._Parent.GetPoints(userId))
        )




