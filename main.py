import os
import threading
from os import path
from dotenv import load_dotenv
from modules.Collection import collection
from modules.Experience import experience

def main():
    # Select resource to track
    resources = ["cobblestone", "wheat", "coal"]

    # Select skill to track
    skills = ["experience_skill_mining", "experience_skill_foraging"]

    # Loading environmental variables
    load_dotenv()
    api_key = os.getenv("API_KEY")
    playerNickname = os.getenv("playerNickname")
    skyblockProfile = os.getenv("skyblockProfile")

    # Creating directory for graphs 
    if path.exists('Graphs') == False:
        os.mkdir("Graphs")

    # Required variables for threading
    activeThreads = []
    currentArrayElement = 0

    # Making threads for resources
    for _ in range(len(resources)):
        currentResource = resources[currentArrayElement]
        t = threading.Thread(target=collection, args=[api_key, playerNickname, skyblockProfile, currentResource, 0])
        t.start()
        activeThreads.append(t)
        currentArrayElement += 1

    # Reseting value of variable to 0
    currentArrayElement = 0

    # Making threads for skills
    for _ in range(len(skills)):
        currentSkill = skills[currentArrayElement]
        t = threading.Thread(target=experience, args=[api_key, playerNickname, skyblockProfile, currentSkill, 1])
        t.start()
        activeThreads.append(t)
        currentArrayElement += 1

    # Activating all threads
    for thread in activeThreads:
        thread.join()

# Starting main function
main()

# Made by mrdoge <3