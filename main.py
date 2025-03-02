import os
import platform
import time

import discord
from colorama import Back, Fore, Style
from discord.ext import commands

# Start of bot code
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

async def setup_hook():
  current_cog = None  # Introduce variable to keep track of the current cog
  try:
      for cog in ["cogs.Hello","cogs.TileRS","cogs.PurgeBot","cogs.RssDepletion"]:
          current_cog = cog  # Update current_cog before attempting to load
          await client.load_extension(cog)
  except Exception as e:
      if current_cog:  # Check if current_cog has been set
          print(f"Failed to load extension {current_cog}:", e)
      else:
          print("Failed to load a cog due to an error before loading:", e)

client.setup_hook = setup_hook

@client.event # This will run each time you restart the bot. 
async def on_ready():
      prfx = (
          Back.BLACK + Fore.GREEN 
          + time.strftime("%H:%M:%S UTC", time.gmtime()) 
          + Back.RESET + Fore.WHITE + Style.BRIGHT
      )
    # this formats the output to the counsole 
      if client is not None and client.user is not None:
        print(prfx + " Logged in as " + Fore.YELLOW + client.user.name)
        print(prfx + " Bot ID " + Fore.YELLOW + str(client.user.id))
        print(prfx + " Discord Version " + Fore.YELLOW + discord.__version__)
        python_version_msg = (prfx + " Python Version " + Fore.YELLOW 
                              + str(platform.python_version()))
        print(python_version_msg) 
        #this is needed for the slash commands to work
        synced = await client.tree.sync()
        print(prfx + " Slash CMDs Synced " + Fore.YELLOW + str(len(synced))
              + " Commands")
        print(prfx + " Current Working Directory:" + Fore.YELLOW + os.getcwd())
        print(prfx + " Bot is Logged in and ready")



# Checks to make sure the token is loaded properly for Discord
token = os.getenv("TOKEN")
if token is not None:
  client.run(token)
else:
  print("Token not loaded properly. Check your environment variables.")