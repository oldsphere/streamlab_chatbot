import re

class DataParser():
    def __init__(self, data_dict={}):
        self.UserName = data_dict.get('User')
        self.User = data_dict.get('UserId')
        self.Message = data_dict.get('Message')
        self.RawData = data_dict.get('RawData')
        self.ServiceType = data_dict.get('ServiceType', 'Twitch')
        self._isWhisper = data_dict.get('isWhisper', False)

    def isWhisper(self):
        return self._isWhisper

    def isChatMessage(self):
        return not self._isWhisper

    def GetParam(self, n):
        params = self.Message.split(' ')
        return params[n] if n < len(params) else ''

    def GetParamCount(self):
        params = self.Message.split(' ')
        return len(params)

    def isRawData(self):
        return False if self.Message else True

    @staticmethod
    def parse_data(raw_data):
        userMatch = re.findall('^(.+):', raw_data)
        user = userMatch[0] if userMatch else ''

        whisperMatch = re.search('/w\s*.+ ', raw_data)
        message = re.sub('^.+: (/w\s*[^\s]+\s*)?','',raw_data)

        data = {
            'User' : user,
            'Message' : message,
            'RawData' : raw_data,
            'ServiceType' : 'twich',
            'isWhisper' : True if whisperMatch else False
        }
        return DataParser(data)
