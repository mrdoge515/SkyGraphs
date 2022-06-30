import os
import time
from modules.getData import *
from datetime import datetime
import matplotlib.pyplot as plt

def cobble(api_key, playerNickname, skyblockProfile, display):
    # Getting required data
    playerUUID = getPlayerUUID(playerNickname)
    skyblockProfileID = getSkyblockProfileID(playerUUID, skyblockProfile, api_key)

    # Initializing 'user' and downloading start data
    user = player(playerUUID, skyblockProfileID, api_key)
    collectionStart = user["profile"]["members"][playerUUID]["collection"]["COBBLESTONE"]
    experienceStart = user["profile"]["members"][playerUUID]["experience_skill_mining"]

    # Initializing data for the graph
    xAxis = [0]
    yAxis = [0]
    timePast = 0
    graphFilename = "Graphs\Cobblestone" + str(datetime.now().strftime(" %H-%M, %d-%m-%Y")) + ".png"

    while(True):
        # Saving old data to variables
        lastCollectionAmount = user["profile"]["members"][playerUUID]["collection"]["COBBLESTONE"]
        lastExperienceAmount = user["profile"]["members"][playerUUID]["experience_skill_mining"]

        # Downloading updated data from api
        user = player(playerUUID, skyblockProfileID, api_key)
        # Saving new data to variables
        collectionAmount = user["profile"]["members"][playerUUID]["collection"]["COBBLESTONE"]
        experienceAmount = user["profile"]["members"][playerUUID]["experience_skill_mining"]

        # Checking if user want to see data on console and if yes - showing it
        if display == 1:
            print("\n\n\n=-=-=-=- Cobblestone -=-=-=-=")
            print("Collection for player", playerNickname, "on profile", skyblockProfile, "at", datetime.now(), ": ", collectionAmount)
            print("Change since start of the script: ", collectionAmount - collectionStart)
            print("Change since last request: ", collectionAmount - lastCollectionAmount)
            print("=-=-=-=- Mining XP -=-=-=-=")
            print("Experience for player", playerNickname, "on profile", skyblockProfile, "at", datetime.now(), ": ", round(experienceAmount, 2))
            print("Change since start of the script: ", round(experienceAmount - experienceStart, 2))
            print("Change since last request: ", round(experienceAmount - lastExperienceAmount, 2))

        # Adding values to graph lists
        xAxis.append(timePast)
        yAxis.append(collectionAmount - lastCollectionAmount)

        # Drawing graph and saving it to a file
        plt.plot(xAxis, yAxis)
        plt.xlabel("Time [minutes]")
        plt.ylabel("Cobblestone collection change")
        plt.title("Cobblestone/time graph")
        plt.savefig(graphFilename)
        
        # Suspending the script for 4 minut (hypixel api refreshes once per 4 minutes)
        time.sleep(180)
        timePast += 4
