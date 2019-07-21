from Chatbot import ChatbotParent, DataParser
import os
import sys

try:
    input = raw_input
except NameError:
    pass


class ChatRoom:

    def __init__(self):
        self._scripts = []
        self._scriptFolder = 'scripts'
        self._Parent = ChatbotParent()

    def set_scriptFolder(self, folder):
        self._scriptFodler = folder

    def set_Parent(self, parent):
        ''' Asign Parent Object '''
        self._Parent = parent

    def AddScript(self, script):
        mod = __import__(script)
        mod.__dict__['Parent'] = self._Parent
        self._scripts.append(mod)

    def LocateScripts(self, folderpath=''):
        ''' Locate valid scripts '''

        if not folderpath:
            folderpath = self._scriptFolder

        for dirpath, dirnames, filenames in os.walk(folderpath):
            for filename in filenames:
                if filename.endswith('_StreamlabsSystem.py'):
                    sys.path.append(dirpath)
                    self.AddScript(filename.replace('.py',''))

    def run(self):
        ''' Online running of the chat '''
        [script.Init() for script in self._scripts]

        try:
            while True:
                raw_line = input()
                if raw_line.strip():
                    Data = DataParser.parse_data(raw_line)
                    Data.User = self._Parent.GetUserId(Data.UserName)
                    [script.Execute(Data) for script in self._scripts]
                else:
                    [script.Tick() for script in self._scripts]

        except KeyboardInterrupt:
            pass

    def run_log(self, logfile):
        ''' Load a log line by line to react to the content '''
        pass
