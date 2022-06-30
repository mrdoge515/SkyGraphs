import os
from dotenv import load_dotenv
from modules.Cobblestone import cobble

# Loading environmental variables
load_dotenv()
api_key = os.getenv("API_KEY")
playerNickname = os.getenv("playerNickname")
skyblockProfile = os.getenv("skyblockProfile")

# Creating directory for graphs
os.mkdir("Graphs")

# Starting cobblestone tracking
cobble(api_key, playerNickname, skyblockProfile, 0)

# Made by mrdoge <3