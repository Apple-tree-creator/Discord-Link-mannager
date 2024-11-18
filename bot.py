# This example requires the 'message_content' intent.

import discord
import re
 
 
def Find(string):
 
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]


TargetChannel = 1308039034328715345 # Channel for links to be sent to

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

while True:
    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if 'http' in message.content.lower():
            string = str(message.content)
            link = str(Find(string))
            link = link.replace(link[:2],'')[:-2]
            channel = client.get_channel(TargetChannel)
            print(link)
            await channel.send(link)

    client.run('TOKEN')

