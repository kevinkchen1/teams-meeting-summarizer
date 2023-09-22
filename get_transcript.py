import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

TENANT = '3bea478c-1684-4a8c-8e85-045ec54ba430'
TEAMS_CLIENT_ID = '075fa40b-2e40-47fd-bd56-7948db4a3354'
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



def retrieve_meetings():
    access_token = refresh_api_key()
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    res = requests.get(f"https://graph.microsoft.com/beta/chats/19:meeting_OWExZWI4MTQtYjEyOS00MjQwLWJlMDQtMWI2NzAzNDY0YTFi@thread.v2/messages/1686854560501/hostedContents/aWQ9MC1ldXMtZDE3LWEyZTk2OTQwZjBjNWIyMGQ5NDJlMzU1Yzk4ZjQxY2JlLHR5cGU9Mix1cmw9aHR0cHM6Ly91cy1wcm9kLmFzeW5jZ3cudGVhbXMubWljcm9zb2Z0LmNvbS92MS9vYmplY3RzLzAtZXVzLWQxNy1hMmU5Njk0MGYwYzViMjBkOTQyZTM1NWM5OGY0MWNiZS92aWV3cy92aWRlbw==/$value?access_token={access_token}")
    print(res.json())

    # response = requests.get('https://graph.microsoft.com/beta/me/chats/', headers=headers)
    # chats = response.json()["value"]

    # for chat in chats:
    #     chat_id = chat["id"]
    #     response = requests.get(f'https://graph.microsoft.com/beta/me/chats/{chat_id}/messages', headers=headers)
    #     try:
    #         data = response.json()["value"]
    #     except KeyError:
    #         continue
    #     for message in data:
    #         try:
    #             url = message["eventDetail"]["callRecordingUrl"]
    #             print(url)
    #             print(message)
    #         except (KeyError, TypeError) as e:
    #             print("nope" + str(e))


print(retrieve_meetings())