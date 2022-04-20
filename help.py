from email import message
from http import server
import discord
import sys
import traceback
from discord.ext import commands
from datetime import datetime
time = str(datetime.now())

class MyHelp(discord.ext.commands.Cog, name='Greetings module'):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="hey")
    async def adhoc_play(self, ctx):
        await ctx.send(f'Hey {ctx.author.name}')
        
        f = open("logs.log", "a")
        f.write(time  + ctx.author.name + " as utilisé la commande hey \n")
        f.close()
        
    @discord.ext.commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(f'A wild {member.mention} has appeared!')
            f = open("logs.log", "a")
            f.write(time  + member.mention + " as rejoins le serveur \n")
            f.close()

    @discord.ext.commands.Cog.listener()
    async def on_message(self, message):
        pmes = {"ping":"Pong", "bonjour bot":"salut!"}

        for mes, rep in pmes.items():
            if message.content.lower() == mes:
                await message.channel.send(rep) 
                f = open("logs.log", "a")
                f.write(time + message.author.name+" a utilisé la commande "+ rep + "\n")
                f.close()
        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten()
            for each_message in messages:
                await each_message.delete()
                f = open("logs.log", "a")
                f.write(time + message.author.name+" a utilisé la commande !delete" + "\n")
                f.close()
        if message.content.startswith("!help"):
            embed=discord.Embed(title="Commandes additionnelles", color=0x553adf)
            embed.set_author(name="Nicolas")
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/3/38/Info_Simple.svg")
            embed.add_field(name="ping", value="pong", inline=False)
            embed.add_field(name="bonjour bot", value="salut!", inline=False)
            embed.add_field(name="del X", value="supprime les X dernières lignes", inline=False)
            await message.channel.send(embed=embed)
            f = open("logs.log", "a")
            f.write(time + message.author.name+" a utilisé la commande !help" + "\n")
            f.close()

    #bot = commands.Bot(command_prefix = "!", description = "Bot de Sandra")
    #@bot.event
    
    @commands.command()
    @commands.guild_only()
    async def serverinf(self, ctx):
        """Info server"""
        
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon_url)
        
        embed = discord.Embed(
            title=name + " Server Information",
            description=description,
            color=discord.Color.blue()
            )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="Owner", value=owner, inline=True)
        embed.add_field(name="Server ID", value=id, inline=True)
        embed.add_field(name="Region", value=region, inline=True)
        embed.add_field(name="Member Count", value=memberCount, inline=True)
        f = open("logs.log", "a")
        f.write(time + ctx.author.name+" a utilisé la commande !serverinf" + "\n")
        f.close()

        await ctx.send(embed=embed)

    @discord.ext.commands.Cog.listener()
    async def on_reaction_add(self,reaction, user):
        emoji2 = '\U0001F606' #:laughing:
        emoji4 = '\U0001F60E' #:sunglasses:
        emoji5 = '\U0001F973' #:partying_face:
        emoji3 = '\U0001F97A' #:pleading_face:
        emoji1 = '\U0001F4AF' #:100:
        if not user.bot:
            await reaction.message.add_reaction(emoji3)
            time = str(datetime.now())
            f = open("logs.log", "a")
            f.write(time + " un utilisateur a ajouté une réaction" + "\n")
            f.close()


    


      
    
    

    

    