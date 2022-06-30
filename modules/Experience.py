import os
import time
from modules.GetData import *
from datetime import datetime
import matplotlib.pyplot as plt

def experience(api_key, playerNickname, skyblockProfile, skill, display):
    # Getting required data
    playerUUID = getPlayerUUID(playerNickname)
    skyblockProfileID = getSkyblockProfileID(playerUUID, skyblockProfile, api_key)

    # Initializing 'user' and downloading start data
    user = player(playerUUID, skyblockProfileID, api_key)
    experienceStart = user["profile"]["members"][playerUUID][skill]

    # Initializing data for the graph
    xAxis = [0]
    yAxis = [0]
    timePast = 0
    graphFilename = "Graphs\\" + skill + str(datetime.now().strftime(" %H-%M, %d-%m-%Y")) + ".png"

    while(True):
        # Saving old data to variables
        lastExperienceAmount = user["profile"]["members"][playerUUID][skill]

        # Downloading updated data from api
        user = player(playerUUID, skyblockProfileID, api_key)
        # Saving new data to variables
        experienceAmount = user["profile"]["members"][playerUUID][skill]

        # Checking if user want to see data on console and if yes - showing it
        if display == 1:
            print("\n\n\n=-=-=-=- ", skill.capitalize(), " -=-=-=-=")
            print("Experience for player", playerNickname, "on profile", skyblockProfile, "at", datetime.now(), ": ", round(experienceAmount, 2))
            print("Change since start of the script: ", round(experienceAmount - experienceStart, 2))
            print("Change since last request: ", round(experienceAmount - lastExperienceAmount, 2))

        # Adding values to graph lists
        xAxis.append(timePast)
        yAxis.append(round(experienceAmount - lastExperienceAmount, 1))

        # Drawing graph and saving it to a file
        plt.plot(xAxis, yAxis)
        plt.xlabel("Time [minutes]")
        plt.ylabel(skill + " experience change")
        plt.title(skill + "/time graph")
        plt.savefig(graphFilename)
        
        # Suspending the script for 4 minut (hypixel api refreshes once per 4 minutes)
        time.sleep(180)
        timePast += 4