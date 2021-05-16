from twitchAPI.twitch import Twitch
from time import sleep
import json


def get_follow_count(twitch):
    followers = twitch.get_users_follows(to_id=102763163)['total']
    return followers


def main():
    with open("secrets.json") as secrets_file:
        secrets = json.load(secrets_file)
    twitch = Twitch(secrets[0],
                    secrets[1])
    twitch.authenticate_app([])
    followers = get_follow_count(twitch)
    followers_string = f"Followers: {followers}"
    with open("followers.txt", "w") as followers_file:
        followers_file.write(str(followers_string))


while __name__ == "__main__":
    try:
        main()
        sleep(10)
    except Exception:
        sleep(10)
