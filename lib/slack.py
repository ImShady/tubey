from lib.config import Config
from slackclient import SlackClient

class Tubey():

    def __init__(self, **kwargs):
        # Cache the client in memory
        self._client = None


    def send_message(self, message):
        # Sends message to the user/channel
        params = {'channel': 'tubeydev', 'text': message}
        client = self.get_client()
        client.api_call("chat.postMessage", **params)


    def get_client(self):
        # Fetch a cached slack client or create one and return it
        if self._client is not None:
            return self._client

        token = Config.get_variable('tubey_credentials', 'bot_oauth_token')
        sc = SlackClient(token)
        self._client = sc
        return self._client

    def play_video(self, video_id):
        # Plays a video in the current channel using the video id
        video_url = "https://www.youtube.com/watch?v={}".format(video_id)
        self.send_message(video_url)

    def send_channel(self, channel_id, channel_name, thumbnail_url):
        # Sends the youtube channel to the active user/slack channel
        channel_url = "https://www.youtube.com/channel/{}".format(channel_id)

        params = {'channel': 'tubeydev', 'text': "Here's the channel:", 'attachments':
                  [{'fallback': channel_name + ' thumbnail', 'title': channel_name, "title_link": channel_url,
                    "image_url": thumbnail_url}]}
        client = self.get_client()
        client.api_call("chat.postMessage", **params)


if __name__ == "__main__":

    tubey = Tubey()
    tubey.send_channel('UCDWIvJwLJsE4LG1Atne2blQ', 'h3h3Productions',
                       'https://yt3.ggpht.com/-QWMKBXNBE2E/AAAAAAAAAAI/AAAAAAAAAAA/rEARmBXfgHw/s240-c-k-no-mo-rj-c0xffffff/photo.jpg')