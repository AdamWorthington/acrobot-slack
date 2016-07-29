import time
from slackclient import SlackClient

token = "xoxb-64602165441-HY31HJpU9Oac8vbt8drWAJ0S"# found at https://api.slack.com/web#authentication
sc = SlackClient(token)
print sc.api_call("api.test")
print sc.api_call("channels.info", channel="1234567890")
print sc.api_call(
        "chat.postMessage", channel="#general", text="Hello from Python! :tada:",
        username='pybot', icon_emoji=':robot_face:'
)
if sc.rtm_connect():
        while True:
                print sc.rtm_read()
                time.sleep(1)
else:
	print "Connection Failed, invalid token?"