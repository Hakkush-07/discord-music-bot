import discord
from discord.ext import commands
from audio import Audio


class Bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice = None

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user} using discord.py {discord.__version__}")
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="!help"))

    @commands.command(name="play", description="Plays a song from Youtube")
    async def play(self, ctx, *, query):
        if not self.voice:
            await self.join(ctx)
        song = Audio(query)
        self.voice.play(song.sound)
        await ctx.send(embed=discord.Embed(title="Playing",
                                           description=f"[{song.title}]({song.url}) - {ctx.author.mention}",
                                           color=0x0000ff)
                       )

    @commands.command(name="pause", description="Pauses the song currently playing")
    async def pause(self, ctx):
        self.voice.pause()
        await ctx.message.add_reaction("⏸️")

    @commands.command(name="resume", description="Resumes the paused song")
    async def resume(self, ctx):
        self.voice.resume()
        await ctx.message.add_reaction("▶️")

    @commands.command(name="stop", description="Stops playing the song")
    async def stop(self, ctx):
        self.voice.stop()
        await ctx.message.add_reaction("🛑")

    @commands.command(name="join", description="Joins your voice channel")
    async def join(self, ctx):
        self.voice = await ctx.author.voice.channel.connect()
        await ctx.message.add_reaction("👌")

    @commands.command(name="leave", description="Leaves the voice channel")
    async def leave(self, ctx):
        await self.voice.disconnect()
        self.voice = None
        await ctx.message.add_reaction("👋")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("Missing Argument")
        elif isinstance(error, commands.errors.CommandInvokeError):
            print(error)
            await ctx.send(f"Command Invoke Error")
