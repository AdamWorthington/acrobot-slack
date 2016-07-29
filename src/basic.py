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
        text = text.lower()
        x = self.ac.get(text)
        if x == '':
            return
        message = text + ' is ' + x 
        self.sc.api_call(
            "chat.postMessage", channel="#general", text=message,
            username='pybot'
            )

    def handle(self, message):
        for key, value in message.iteritems():
            print(key, value)
            if key == "text":
                self.recog(message[key])


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

    def recog(self, text):
        curr = 'what is ' 
        acronym = 'acronym '
        if text.lower().startswith(curr):
            ret = text[len(curr):]
            self.handleText(ret)
        elif text.lower().startswith(acronym):
            first_space = text.index(' ', len(acronym))
            first_word = text[len(acronym):first_space]
            second_word = text[first_space + 1:]
            self.ac.put(first_word.lower(), second_word)
            self.handleText(first_word)



if __name__ == "__main__":
    Bot().run()
