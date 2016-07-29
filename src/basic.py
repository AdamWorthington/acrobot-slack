import time
import json
import base64
from slackclient import SlackClient




token='x' +'oxb-64602165441-qTU3kuCfbVMCtRYHbeDUd5Zy'
sc = SlackClient(token)

def handle(message):
	json_string=message
	# obj = json.loads(json_string)
	print(json_string)
	# if obj == 'yolo':
	# 	sc.api_call(
	# 		"chat.postMessage", channel="#general", text="fuck your yolo",
	# 		username='pybot'
	# 		)

if sc.rtm_connect():
	while True:
		handle(sc.rtm_read())
		time.sleep(1)
else:
	print "Connection Failed, invalid token?"


