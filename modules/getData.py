import requests

# Getting user's UUID from mojang
def getPlayerUUID(playerNickname):
    return (requests.get("https://api.mojang.com/users/profiles/minecraft/" + playerNickname).json())['id']

# Getting skyblock profile's ID from Hypixel
def getSkyblockProfileID(playerUUID, skyblockProfile, api_key):
    data = list(((requests.get("https://api.hypixel.net/player?uuid=" + playerUUID + "&key=" + api_key).json())["player"]["stats"]["SkyBlock"]["profiles"]).values())

    for i in range(len(data)):
        if skyblockProfile == data[i]["cute_name"]:
            a = data[i]["profile_id"]
    return a

# Getting skyblock stats
def player(playerUUID, skyblockProfileID, api_key):
    return requests.get("https://api.hypixel.net/skyblock/profile?key=" + api_key + "&uuid=" + playerUUID + "&profile=" + skyblockProfileID).json()
