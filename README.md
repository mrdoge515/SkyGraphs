# SkyGraphs
## About the program
It automatically gets data about your collection/skill experience from Hypixel API, displays it in the console and makes graphs.
## To-do
- [ ] Threading (tracking multiple resource at the same time)
- [ ] Add modules to all resources (I will do it as I go with my ironman profile, so all resources will be done in +- a month from update of readme)
## How to install
### Requirements
- Python 3
- pip
### Installation
- Open a terminal in script's directory and install required packages: ```pip install -r requirements.txt```
- Then type edit .env file with your data. You can get your API key by typing ```/api new``` in minecraft on Hypixel.
- Then start the script with ```python main.py```
## Credits
I saw this [video](https://www.youtube.com/watch?v=VSzKwkXea1g) and the person that made it posted a script in the comment tracking their wheat extraction. So I decided to change the program to also make graphs of it. In the end I completely rewrote the program so it's more extensible and you can easily add modules of new resources you want to track.