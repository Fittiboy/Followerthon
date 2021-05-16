from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
from time import sleep
import json


def get_follow_count(twitch):
    followers = twitch.get_users_follows(to_id=102763163)['total']
    return followers


def get_stream_title(twitch):
    info = twitch.get_channel_information(broadcaster_id=102763163)
    data = info["data"]
    dct = data[0]
    title = dct["title"]
    return title


def update_stream_title(twitch, title, followers):
    if "Followers: " in title:
        title = title.split("|")[0]
        new_title = title + f"| Followers: {followers}"
        twitch.modify_channel_information(broadcaster_id=102763163,
                                          title=new_title)
        print("Stream title updated: \n\t", new_title)


def main(followers_prev, twitch):
    followers = get_follow_count(twitch)
    if followers != followers_prev:
        followers_prev = followers
        title = get_stream_title(twitch)
        update_stream_title(twitch, title, followers)
    followers_string = f"Followers: {followers}"
    with open("followers.txt", "w") as followers_file:
        followers_file.write(str(followers_string))
    return followers_prev


if __name__ == "__main__":
    with open("secrets.json") as secrets_file:
        secrets = json.load(secrets_file)
    twitch = Twitch(secrets[0],
                    secrets[1])
    target_scope = [AuthScope.CHANNEL_MANAGE_BROADCAST]
    auth = UserAuthenticator(twitch, target_scope, force_verify=False)
    token, refresh_token = auth.authenticate()
    twitch.set_user_authentication(token, target_scope, refresh_token)
    # followers_prev = get_follow_count(twitch)
    followers_prev = 0
    while True:
        try:
            followers_prev = main(followers_prev, twitch)
            sleep(10)
        except Exception as e:
            print(e)
            sleep(10)
