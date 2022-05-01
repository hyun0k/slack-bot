from config    import SLACK_API_BOT_TOKEN
from message   import TEST
from slack     import SlackAPI

token = SLACK_API_BOT_TOKEN
client = SlackAPI(token)

def main():
    channel_id = "C03CG916DJ7"
    message = TEST

    client.post_message(channel_id, message)

if __name__ == "__main__":
    main()