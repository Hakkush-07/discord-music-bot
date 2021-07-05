from discord.ext import commands
from bot import Bot

token = ""
client = commands.Bot(command_prefix="!")
client.add_cog(Bot(client))
client.run(token)
