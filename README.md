# Discord Link Mannaging Bot
## About bot
Bot mannages links by checking messages in channels it has access to for links and then sending those links to a specific channel.

## How to use bot
Send a message with both a link and the words 'pin' and 'url'/'link' to a channel the bot is in.

## Setting up bot
 - [Install required modules](#modules)
 - Change TOKEN to a Discord Bot Token
 - Change ChannelID to the channel ID of the channel you want the links pinned in

<a name="modules" />

## Required Modules
 - discordpy

## Required files
 - bot.py
 - activity.txt *(required for activity to work)*

## Structuring activity.txt 
 - Line 1 is the type of activity
 - Line 2 is for the name of the Game/Stream/Song/Video
 - Line 3 if for stream link (Will be ignored if not required)
