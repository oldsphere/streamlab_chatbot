from Chatbot import ChatbotParent, DataParser
import os
import sys

class ChatRoom:

    def __init__(self):
        self._scripts = []


    def AddScript(self, script):
        mod = __import__(script)
        mod.__dict__['Parent'] = Parent
        self._scripts.append(mod)

    def LocateScripts(self, folderpath='scripts'):
        ''' Locate valid scripts '''
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
                    [script.Execute(Data) for script in self._scripts]
                else:
                    [script.Tick() for script in self._scripts]

        except KeyboardInterrupt:
            pass

    def run_log(self, logfile):
        ''' Load a log line by line to react to the content '''
        pass


if __name__ == '__main__':

    Parent = ChatbotParent()
    room = ChatRoom()
    room.LocateScripts()
    room.run()
