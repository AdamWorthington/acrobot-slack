import time
import json
import base64
from acronym import Acronyms
from slackclient import SlackClient

token = 'x' +'oxb-64602165441-qTU3kuCfbVMCtRYHbeDUd5Zy'

class Bot:

    def __init__(self):
        self.sc = SlackClient(token)
        self.ac = Acronyms()
        self.ac.put('yolo', 'you only live once')

    def handleText(self, text):
        x = self.ac.get(text)
        if x == '':
            return

        self.sc.api_call(
            "chat.postMessage", channel="#general", text=x,
            username='pybot'
            )

    def handle(self, message):
        for key, value in message.iteritems():
            print(key, value)
            if key == "text":
                self.handleText(message[key])


    def run(self):
        if self.sc.rtm_connect():
            print "Connection valid, reading from rtm"
            while True:
                messages = self.sc.rtm_read()
                for message in messages:
                    self.handle(message)
                time.sleep(1)
        else:
            print "Connection Failed, invalid token?"

if __name__ == "__main__":
    Bot().run()
