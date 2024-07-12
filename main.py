from webserver import keep_alive
import requests

channelID = PUT THE CHANNEL ID
headers = {
    "authorization":
    "MTEzMzE5NjM0MTg3MTM5OTAxMg.G8vIHQ.dZ6A9jhuTz_90X_aHFnmoUsPAN0umymGznGzbI"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
