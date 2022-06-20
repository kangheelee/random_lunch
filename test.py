from slack import get_user_ids, send_mim_msg, send_pub_msg, get_conversations, get_offstage_channel_id
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

if __name__ == '__main__':
    recent_bot_message = get_conversations()
    for mes in recent_bot_message:
        try:
            if mes["bot_id"] == 'B03G012J1UH':
                reactions = mes["reactions"]
                print(reactions)
                break
        except:
            print('key error occured')
