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

    def handleText(self, text, channel):
        text = text.lower()
        x = self.ac.get(text)
        if x == '':
            return
        message = text + ' is ' + x 
        self.sc.api_call(
            "chat.postMessage", channel=channel, text=message,
            username='acrobot', icon_emoji=':a:'
            )

    def handle(self, message):
        if "text" in message:
            text = message["text"]
            channel = message["channel"]
            self.recog(text, channel)
        for key, value in message.iteritems():
            print(key, value)

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

    def recog(self, text, channel):
        tokens = text.split(' ')
        if len(tokens) > 2 and tokens[0].lower() == 'acronym':
            first_word = tokens[1]
            second_word = ' '.join(tokens[2:])
            self.ac.put(first_word.lower(), second_word)
            self.handleText(first_word, channel)
        elif len(tokens) > 2 and tokens[0].lower() == 'what' and tokens[1].lower() == 'is':
            self.handleText(' '.join(tokens[2:]).strip('?'), channel)

if __name__ == "__main__":
    Bot().run()
