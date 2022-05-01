from datetime         import datetime

from slack_sdk        import WebClient
from slack_sdk.errors import SlackApiError

class SlackAPI():

    def __init__(self, token) -> None:
        self.client = WebClient(token)

    def post_message(self, channel_id, text):
        try:
            result = self.client.chat_postMessage(
                        channel=channel_id,
                        text=text
                    )
            return result

        except SlackApiError as e:
            print(f"Error occured : {e}")

    def check_month(date):
        return 0

    def is_working_day(date):
        return True if datetime(date).weekday <= 4 else False

