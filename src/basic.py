import time
import json
import base64
from acronym import Acronyms
from slackclient import SlackClient


token='x' +'oxb-64602165441-qTU3kuCfbVMCtRYHbeDUd5Zy'
sc = SlackClient(token)
bot = Acronyms()
bot.put('yolo', 'you only live once')

def handleText(text):
	x=bot.get(text)
	if x == '':
		return
	
	sc.api_call(
		"chat.postMessage", channel="#general", text=x,
		username='pybot'
		)

def handle(message):
	for key, value in message.iteritems():
		print(key, value)
		if key == "text":
			handleText(message[key])




def main():
	



	if sc.rtm_connect():
		print "Connection valid, reading from rtm"
		while True:
			messages = sc.rtm_read()
			for message in messages:
				handle(message)
			time.sleep(1)
	else:
		print "Connection Failed, invalid token?"




main()