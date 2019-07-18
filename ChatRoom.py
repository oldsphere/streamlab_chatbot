from Chatbot import Parent, DataParser, ScriptLoader

class ChatRoom:

    def __init__(self):
        self._scripts = []


    def AddScript(self, script):
        self._script.append(script)

    def run(self):

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


if __name__ == '__main__':
    room = ChatRoom()
    room.run()
