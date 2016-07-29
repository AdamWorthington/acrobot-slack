import time
import json
import base64
from slackclient import SlackClient




token='x' +'oxb-64602165441-qTU3kuCfbVMCtRYHbeDUd5Zy'
sc = SlackClient(token)

def handleText(text):
	if text == "yolo":
        	sc.api_call(
	 		"chat.postMessage", channel="#general", text="fuck your yolo",
	 		username='pybot'
	 		)

def handle(message):
	for key, value in message.iteritems():
		print(key, value)
		if key == "text":
			handleText(message[key])

if sc.rtm_connect():
	print "Connection valid, reading from rtm"
	while True:
		messages = sc.rtm_read()
		for message in messages:
			handle(message)
		time.sleep(1)
else:
	print "Connection Failed, invalid token?"


