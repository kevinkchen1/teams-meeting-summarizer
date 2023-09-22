import requests
import webbrowser

TENANT = '3bea478c-1684-4a8c-8e85-045ec54ba430'
TEAMS_CLIENT_ID = '075fa40b-2e40-47fd-bd56-7948db4a3354'
ADMIN_APPROVAL_LINK = "https://login.microsoftonline.com/common/adminconsent?client_id=075fa40b-2e40-47fd-bd56-7948db4a3354&state=12345&redirect_uri=https://login.microsoftonline.com/common/oauth2/nativeclient"
#STEP 1. Authenticate with the URL below in Chrome. If successful, get the 'code=' parameter from the URL, copy below
#        If you need to approve the app, ping Dugan
def open_link():
    SCOPES = "offline_access OnlineMeetingTranscript.Read.All Calendars.Read ChannelMessage.Send Group.ReadWrite.All"
    webbrowser.open(f"https://login.microsoftonline.com/3bea478c-1684-4a8c-8e85-045ec54ba430/oauth2/v2.0/authorize?client_id=075fa40b-2e40-47fd-bd56-7948db4a3354&redirect_uri=https://login.microsoftonline.com/common/oauth2/nativeclient&response_type=code&scope={SCOPES}&response_mode=query")

#  https://login.microsoftonline.com/3bea478c-1684-4a8c-8e85-045ec54ba430/oauth2/v2.0/authorize?client_id=075fa40b-2e40-47fd-bd56-7948db4a3354&redirect_uri=https://login.microsoftonline.com/common/oauth2/nativeclient&response_type=code&scope=offline_access OnlineMeetingTranscript.Read.All Calendars.Read ChannelMessage.Send Group.ReadWrite.All&response_mode=query

CODE = "0.AVgAjEfqO4QWjEqOhQRexUukMAukXwdALv1HvVZ5SNtKM1RYAKY.AgABAAIAAAD--DLA3VO7QrddgJg7WevrAgDs_wUA9P-2d3afjfqfpaJLqssFWuSTxxr4qBtacAxNRTgjV705V4_gwJoY0ObtPAt92R7xW3644Beg418qHlGzoBHc4aIabZO0LcOCns0pt6rvQSIjKeoUqHSfYoD_7NR7VliTmL4ohfiegM5iTARne5ycCBgp_uuVdXkfl-irl3nZWxrbuHiOwtnjK5_ZKTSFJj8mpjJ6G2ydVsX_o7vxGFPaZ783B3YU0pigWrcfoZ1E196uw2z3Ms4m7IHpbp2vts47BCQ4CusauCalCEvMvMutiZ4Mik6H4v6pvcMASzDgij0DIPAcn2FP0oRZlgavF-eKAA5lz2jXcbfzQ6hUlzzJ39A_cnO8zp_bM0zioi1AAVNmr1C1bi6Oa3BI9ZccWE9-X3yaXYaanCzwmwjfefE0I8dTPT-hZxmZPcDU8QFzOGKtT6jxXq5S4kVbD5BxmwDEVNPTJ-4LLBQkF3_DevTaju60byA04tkdG0gS5EmANmOwoRHqOJtU7Zh0_-WvMQdWK3e1qnRRtWgmiXqzqpDm2t8JWGxXKa15D2-8FaHc7m2ogeo-FPWj1qtGkhLF_N2PUMbrFL7uKjlXb7QYZ-BwHBerKrHgBlpjNfOmk1IYSPVJUABOSN4NC6oebfij9WdhVdiMll38kbMfCMjHUeU1FcBmjoap8fM7VmXpImo8yU6QedLuNKjcOZWRV8k9OpDs6kC_SY1R3lEzqS88Edgmnoh6VLiSlsy504ro3b7BQLrNGHc_HQQZjSnIVxvgmMuy_DhgZOhoKCJ-SGZ8iRheU6Cnfn9LE9tjL4EzzUYhhDRWMdFUT-B3h9iv2UoP2v5ZuhdOjmV2AfaKtDtRe5yNB-akDvqE6nJSPKAjbH7nDH5IZQq0LpLPyTtoRWcA7T4DKlmfSQNVPIHzC6wED2a-uztGhrScwpIfLk0d5hYqu1BY8HUz2sBV0OsGn3VaMa3pkdEQy4ZoLedIVh6G_RRRVlnAgBCJr48Q4ZBXToJff6LYlj09cotLFjWUZMEktH--qPJz7ToYPCoiGPHmcvN7KcDPyc0aCty8cTLrsq1NW7vFsyEaDX_K"
#STEP 2. Using the CODE, get an API key. Good for like an hour. Can only get 1 key per CODE, but can refresh with token. Paste into API
def get_api_key():
    SCOPE = "https://graph.microsoft.com/.default"
    GRANT_TYPE = "authorization_code"
    REDIRECT_URI = "https://login.microsoftonline.com/common/oauth2/nativeclient"

    res = requests.post(f"https://login.microsoftonline.com/{TENANT}/oauth2/v2.0/token",
                        headers={"Content-Type": "application/x-www-form-urlencoded"},
                        data=f"client_id={TEAMS_CLIENT_ID}&code={CODE}&redirect_uri={REDIRECT_URI}&scope={SCOPE}&grant_type={GRANT_TYPE}")

    with open("token.json", "w") as file:
        file.write(res.content.decode())

if __name__ == "__main__":
    #open_link()
    get_api_key()