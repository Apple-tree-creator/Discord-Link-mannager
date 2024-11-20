# This example requires the 'message_content' intent.

import discord
from discord.ext import tasks, commands # Allows for presense
import re
import requests
from bs4 import BeautifulSoup
import time
import os

clear = lambda: os.system('clear')
 
def Find(string):
 
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


TargetChannel = CHANNELID # Channel for links to be sent to

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

while True:
    @client.event
    async def on_ready():
        f = open("activity.txt", "r", encoding="utf8")
        await client.change_presence(activity=discord.Streaming(name=f.readline(), url=f.readline()))
        f.close
        time.sleep(0.2)
        clear()
        print('Connected')
        print('Logged in as {0.user}'.format(client))
        loop.start()
        
    # loop task
    @tasks.loop(seconds=1)
    async def loop():
        # automatically updates the rich status
        f = open("activity.txt", "r", encoding="utf8")
        active = f.readline()
        name = f.readline()
        url =f.readline()
        f.close()
        if 'streaming' in active: #streaming
            await client.change_presence(activity=discord.Streaming(name=f'{name}', url=f'{url}'))
        elif 'playing' in active: #playing
            await client.change_presence(activity=discord.Game(name=f'{name}'))
        elif 'watching' in active: #Watching
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{name}'))
        elif 'listening' in active: #Listening
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{name}'))
        else:
            print('Status not available')
        f = open("activity.txt", "r", encoding="utf8")
        check1 = f.readline()
        check2 = f.readline()
        check3 =f.readline()
        f.close()

    @client.event
    async def on_message(message):
        if message.author == client.user: # Ignores messages from itself
            return

        if 'http' in message.content.lower():
            string = str(message.content)
            link = str(Find(string))
            link = str(link).replace(link[:2],'')[:-2] # Grabs link and removes the [' '] brackets
            response = requests.get(link)
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.string
            channel = client.get_channel(TargetChannel) # Sets channel to target channel
            print(link)
            await channel.send(f'{title}: {link}')
    try:
        client.run('TOKEN') # bot token
    except discord.HTTPException as e:
        if e.status == 429:
            print("Unable to login due to \"too many requests\"")
            print(
                "Get help from https://stackoverflow.com/questions/66724687/in-discord-py-how-to-  solve-the-error-for-toomanyrequests"
            )
        else:
            raise e


