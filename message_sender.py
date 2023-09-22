import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

TENANT = "3bea478c-1684-4a8c-8e85-045ec54ba430"
TEAMS_CLIENT_ID = "075fa40b-2e40-47fd-bd56-7948db4a3354"
TEAMS_CLIENT_SECRET = os.environ.get("TEAMS_CLIENT_SECRET")

def refresh_api_key():
    SCOPE = "https://graph.microsoft.com/.default"
    GRANT_TYPE = "refresh_token"

    with open("token.json", "r") as file:
        data = json.load(file)
        REFRESH_TOKEN = data["refresh_token"]

    res = requests.post(f"https://login.microsoftonline.com/{TENANT}/oauth2/v2.0/token",
                        headers={"Content-Type": "application/x-www-form-urlencoded"},
                        data=f"client_id={TEAMS_CLIENT_ID}&refresh_token={REFRESH_TOKEN}&scope={SCOPE}&grant_type={GRANT_TYPE}")

    with open("token.json", "w") as file:
        file.write(res.content.decode())

    data = json.loads(res.content.decode())
    return data["access_token"]

#STEP 3. Send the message.
def send_message(message):
    with open("summary.txt", "r") as textfile:
        data = textfile.read().splitlines()

    API_KEY = refresh_api_key()
    channel_id = "19:fe1e33ff6ae24e48bde6ef0ce20edf74@thread.tacv2"
    team_id = "c8bca1d2-486b-4ca2-8657-a2469459d2c3"

    chat_id = "19:26b32ca6-59d8-4f80-947d-3bf23801cbd9_c6167638-8de1-42fa-8dca-d952b87f86fb@unq.gbl.spaces"

    data.insert(0, "MEETING SUMMARY:")
    data = "<br/>".join(data)
    print(data)
    res = requests.post(url = f"https://graph.microsoft.com/v1.0/teams/{team_id}/channels/{channel_id}/messages",
                        json = {
                            "subject": None,
                            "body": {
                                "contentType": "html",
                                "content": data
                            },
                        },
                        headers={"Authorization": API_KEY, "Content-type": "application/json"}
                        )

    #CHAT SEND
    # res = requests.post(url = f"https://graph.microsoft.com/v1.0//chats/{chat_id}/messages",
    #                     json = {"body": {"content": message}},
    #                     headers={"Authorization": API_KEY, "Content-type": "application/json"}
    #                     )

send_message("")