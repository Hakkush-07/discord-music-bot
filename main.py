import discord
from discord.ext import commands
import asyncio
from bot import Bot

token = ""
client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

async def main():
    await client.add_cog(Bot(client))
    async with client:
        await client.start(token)

asyncio.run(main())
