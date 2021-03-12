import discord
from discord.ext import commands
from youtube_search import YoutubeSearch

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['p'])
    async def Play(self, ctx , *args):
        channel = ctx.message.author.voice.channel
        results = YoutubeSearch('felipe neto', max_results=5).to_dict()
        print(results)
        await channel.connect()

def setup(bot):
    bot.add_cog(Music(bot))
