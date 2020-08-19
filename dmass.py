import discord
from discord.ext import commands
import platform
import random
import time

bot = commands.Bot(command_prefix='+', case_insensitive=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}(ID: +{bot.user.id}) |'
          f'Connected to {str(len(bot.guilds))} servers |'
          f'Connected to {str(len(set(bot.get_all_members())))} users')
    print('--------')
    print('CREATED AND HOSTED BY ShaW')


@bot.event
async def on_command_error(ctx, error):
    # Ignore these errors:
    ignored = (
        commands.CommandNotFound, commands.UserInputError, commands.BotMissingPermissions, commands.MissingPermissions, discord.errors.Forbidden, commands.CommandInvokeError, commands.MissingRequiredArgument)
    if isinstance(error, ignored):
        return

@bot.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("faltu") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="sala kutta")
                
                
@bot.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "✺┊ᴡᴇʟᴄᴏᴍᴇ":
            await channel.send(f"""Welcome to the server {member.mention}""")
            
@client.event
async def on_message(message):
    global messages
    messages += 1

    id = client.get_guild(725931924027080725)
    channels = ["setup"]
    valid_users = ["ShaW#0768"]
    bad_words = ["bad", "stop", "45", "kutta", "sala"]

    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)

    if message.content == "+hey":
        embed = discord.Embed(title="ShaW Ka Area", description="Abe Sale, Chal be")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints number of users")
        await message.channel.send(content=None, embed=embed)

    if str(message.channel) in channels and str(message.author) in valid_users:
        if message.content.find("!hello") != -1:
            await message.channel.send("Hi") 
        elif message.content == "!users":
            await message.channel.send(f"""# of Members: {id.member_count}""")
    
    

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def userinfo(ctx, user: discord.Member):
    try:
        embed = discord.Embed(title="{}'s info".format(user.name),
                              description="Here's what I could find.",
                              color=discord.Colour.dark_red())

        embed.add_field(name="Name", value=user.name, inline=True)
        embed.add_field(name="ID", value=user.id, inline=True)
        embed.add_field(name="Status", value=user.status, inline=True)
        embed.add_field(name="Highest role", value=user.top_role)
        embed.add_field(name="Joined", value=user.joined_at)
        embed.set_thumbnail(url=user.avatar_url)

        await ctx.send(embed=embed)
    except:
        await ctx.send("Missing Requrired Args")


@commands.has_permissions(administrator=True)
@bot.command(pass_context=True)
async def send(ctx, *, content: str):
    for member in ctx.guild.members:
        c = await member.create_dm()
        try:
            await c.send(content)
            await ctx.send("Message Sent to Targets")
        except:
            await ctx.send("DM can't send to : {} :x: ".format(member))


bot.run("NzQzNTAwOTQ5NTk0NTcwODMy.XzVlNw.5TV_eZLRG6ajbsxyIJulrT2Ksj8")
