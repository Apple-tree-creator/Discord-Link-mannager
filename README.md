# Discord Link Mannaging Bot
## About bot
Bot mannages links by checking messages in channels it has access to for links and then sending those links to a specific channel.

## Required Modules
 - discordpy

## Required files
 - bot.py
 - activity.txt *(required for activity to work)*

## Changing bots status
*(note: You do not need to restart the bot)*

Setting `Playing` status
 - await client.change_presence(activity=discord.Game(name=f.readline))

Setting `Streaming` status
 - await client.change_presence(activity=discord.Streaming(name=f.readline(), url=f.readline()))

Setting `Listening` status
 - await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f.readline()))

Setting `Watching` status
 - await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f.readline))

### Structuring activity.txt 
 - Line 1 is the type of activity
 - Line 2 is for the name of the Game/Stream/Song/Video
 - Line 3 if for stream link (Will be ignored if not required)
