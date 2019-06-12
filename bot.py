import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import aiohttp
from random import choice, shuffle
import logging
import sys
import traceback
 
client = commands.Bot(description="WaZiBoT Is Awesome", command_prefix=(">"))
client.remove_command('help')

start_time = datetime.datetime.utcnow()

#riddle
answering = False
riddle = ""
riddleAnswer = ""
riddleLine = 0
riddleGuessesLeft = 2
prevRiddleLine = 0

async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='Annoying WASIF', type=0))
        await asyncio.sleep(10)
        await client.change_presence(game=discord.Game(name='>help', type=2))
        await asyncio.sleep(10)
        await client.change_presence(game=discord.Game(name=str(len(set(client.get_all_members())))+' WaZifers', type=3))
        await asyncio.sleep(10)

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print('working properly xD')
    client.loop.create_task(status_task())
    channel = client.get_channel("552868494140506125")
    await client.send_message(channel, ":white_check_mark: I am up!")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.type==discord.ChannelType.private:
        return
    await client.process_commands(message)
    if message.author.server_permissions.kick_members:
        return
    else:    
        if "🖕" in message.content:
            await client.delete_message(message)
            await client.send_message(message.channel, ":x: {} No inappropriate emoji!".format(message.author.mention))
        if "🍆" in message.content:
            await client.delete_message(message)
            await client.send_message(message.channel, ":x: {} No inappropriate emoji!".format(message.author.mention))
        if "👉👌" in message.content:
            await client.delete_message(message)
            await client.send_message(message.channel, ":x: {} No inappropriate emoji!".format(message.author.mention))
        if "🍌" in message.content:
            await client.delete_message(message)
            await client.send_message(message.channel, ":x: {} No inappropriate emoji!".format(message.author.mention))	
        if "🥒" in message.content:
            await client.delete_message(message)
            await client.send_message(message.channel, ":x: {} No inappropriate emoji!".format(message.author.mention))
        if message.content.startswith("dafaque"):
            await client.delete_message(message)
            await client.send_message(message.channel, ":x: {} No inappropriate words!".format(message.author.mention))
        if message.content.startswith("chut"):
            await client.delete_message(message)
            await client.send_message(message.channel, ":x: {} No inappropriate words!".format(message.author.mention))		
		
	
@client.command(pass_context = True)
async def lol(ctx):
    return

@client.command(pass_context = True)
async def fnstats(ctx):
    return

@client.command(pass_context = True, aliases=["level"])
async def rank(ctx):
    return

@client.command(pass_context = True)
async def messages(ctx):
    return

@client.command(pass_context = True, aliases=["p", "clear", "ascii", "weather"])
async def play(ctx):
    return

@client.command(pass_context = True, aliases=["s", "l", "leave", "skip"])
async def stop(ctx):
    return

@client.command(pass_context = True, aliases=["vol", "np", "q", "queue", "pause", "resume"])
async def volume(ctx):
    return

@client.command(pass_context = True) 
async def banlist(ctx):
    if ctx.message.author.server_permissions.ban_members or ctx.message.author.id=="519122918773620747":
        x = await client.get_bans(ctx.message.server)
        x = '\n'.join([y.name for y in x]) 
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = "BANNED IDIOTS", value = "```py\n{0}```".format(x), inline=False)
        await client.say(embed=embed)

@client.command(pass_context = True)
async def riddle(ctx):
    global riddle, riddleLine, prevRiddleLine, riddleAnswer, riddleGuessesLeft, answering
    answering = True
    riddle = ""
    riddleAnswer = ""
    riddleGuessesLeft = 3

    with open("riddles.txt", "r") as f:
        lines = f.readlines()
    while riddle == "" or "=" in riddle or riddleLine == prevRiddleLine:
        riddleLine = random.randrange(0, len(lines))
        riddle = lines[riddleLine]
        riddleAnswer = lines[riddleLine+1]
    prevRiddleLine = riddleLine
    f.close()

    riddleAnswer = riddleAnswer.replace("=", "")
    riddleAnswer = riddleAnswer.replace(" ", "")

    await client.say("Use `>answer <answer>` to solve the riddle in one word or number.You have 2 guesses per riddle.\n\n" + "`"+riddle+"`")

@client.command(pass_context = True)
async def answer(ctx, userAnswer):
    global riddleAnswer, riddleGuessesLeft, answering

    if answering is False:
        await client.say(":x: **No questions were found. Use >riddle to receive another riddle.**")
        return

    userAnswer = userAnswer.strip()
    riddleAnswer = riddleAnswer.strip()

    if str.lower(userAnswer) == str.lower(riddleAnswer):
        await client.say(":white_check_mark: Correct!")
        answering = False
    else:
        riddleGuessesLeft -= 1
        await client.say(":x: Incorrect!  Guesses left:" + str(riddleGuessesLeft))
    if riddleGuessesLeft == 0:
        await client.say("The answer was: " + riddleAnswer)
        answering = False	

@client.command(pass_context = True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name = ':hourglass_flowing_sand: BOT LATENCY :hourglass_flowing_sand:',value = ':timer: `{}ms` :timer:'.format(round((t2-t1)*1000)),inline = False)
    await client.say(embed=embed)	

@client.command(pass_context = True, aliases=["videoidea"])
async def idea(ctx, *, msg: str=None):
    if msg is None:
        await client.say(":x: Please provide a message.")
        return
    else:
        await client.delete_message(ctx.message)
        reactions = ["✅", "❎", "❓"]
        channel = client.get_channel("583891872934658048")
        url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(ctx.message.author)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_thumbnail(url=url)
        embed.set_author(name = "VIDEO IDEA")
        embed.add_field(name = "__**IDEA BY:**__", value = "{}".format(ctx.message.author.mention), inline=False)
        embed.add_field(name = "__**IDEA:**__", value = "{}\n\n✅Good | ❎Bad |❓Inappropriate".format(msg))
        embed.set_footer(text = f"{client.user.display_name}.xyz")
        embed.timestamp = datetime.datetime.utcnow()
        rmsg = await client.send_message(channel, embed=embed)
        for emoji in reactions:
            await client.add_reaction(rmsg, emoji)	
	
@client.command(pass_context = True, aliases=["discord"])
async def discordmeme(ctx):
    if ctx.message.author.bot:
        return
    else:
        ml = ["👍 256", "👍 1K", "👍 6.5K", "👍 203K", "👍 1M", "👍 97K", "👍 500K"]
        co = ["💬 126", "💬 19K", "💬 3K", "💬 70K", "💬 1M", "💬 10M", "💬 2.3K", "💬 917"]
        title = ["Dad, can you put my shoes on? I don't think they'll fit me.", "Toasters were the first form of pop-up notifications.", "What do you get hanging from Apple trees? Sore arms.", "Atheism is a non-prophet organisation.", "Why do mathematicians hate the U.S.? Because it's indivisible.", "Can February march? No, but April may.", "What does a female snake use for support? A co-Bra!", "What do you call a boomerang that won't come back? A stick.", "Why did the coffee file a police report? It got mugged.", "Why did the girl smear peanut butter on the road? To go with the traffic jam.", "A bartender broke up with her boyfriend, but he kept asking her for another shot.", "How many apples grow on a tree? All of them!"]
        like = random.choice(ml)
        comment = random.choice(co)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title='**__DISCORD MEME__**', description=random.choice(title), color = discord.Color((r << 16) + (g << 8) + b))
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.reddit.com/r/Discordmemes/random") as r:
                data = await r.json()
                embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                embed.set_footer(text=f'{random.choice(ml)} | {random.choice(co)}', icon_url=f'{ctx.message.author.avatar_url}')
                embed.timestamp = datetime.datetime.utcnow()
                await client.say(embed=embed)

@client.command(pass_context=True, aliases=["ms"])
async def minesweeper(ctx):
    url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(ctx.message.author)	
    choices = ['||:zero:|| ||:bomb:|| ||:one:|| ||:eight:|| ||:one:||\n||:bomb:|| ||:six:|| ||:bomb:|| ||:one:|| ||:bomb:||\n||:one:|| ||:eight:|| ||:four:|| ||:three:|| ||:five:||\n||:bomb:|| ||:two:|| ||:one:|| ||:bomb:|| ||:nine:||', '||:one:|| ||:one:|| ||:two:|| ||:bomb:|| ||:nine:||\n||:bomb:|| ||:one:|| ||:three:|| ||:four:|| ||:six:||\n||:bomb:|| ||:one:|| ||:bomb:|| ||:one:|| ||:five:||\n||:bomb:|| ||:one:|| ||:eight:|| ||:bomb:|| ||:seven:||',  '||:one:|| ||:zero:|| ||:two:|| ||:eight:|| ||:six:||\n||:bomb:|| ||:nine:|| ||:one:|| ||:four:|| ||:three:||\n||:bomb:|| ||:two:|| ||:one:|| ||:bomb:|| ||:five:||\n||:bomb:|| ||:bomb:|| ||:one:|| ||:one:|| ||:seven:||', '||:nine:|| ||:bomb:|| ||:one:|| ||:three:|| ||:eight:||\n||:bomb:|| ||:bomb:|| ||:six:|| ||:one:|| ||:bomb:||\n||:seven:|| ||:four:|| ||:one:|| ||:bomb:|| ||:five:||\n||:bomb:|| ||:eight:|| ||:zero:|| ||:one:|| ||:nine:||', '||:zero:|| ||:one:|| ||:nine:|| ||:three:|| ||:eight:||\n||:one:|| ||:bomb:|| ||:bomb:|| ||:bomb:|| ||:bomb:||\n||:seven:|| ||:one:|| ||:four:|| ||:two:|| ||:five:||\n||:six:|| ||:one:|| ||:eight:|| ||:zero:|| ||:bomb:||']
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url=url)
    embed.add_field(name = '__**WAZEEPER GAME**__',value=random.choice(choices),inline = False)
    embed.set_footer(text=f'Gamewith{client.user.display_name}.xyz', icon_url=f'{client.user.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.say(embed=embed)		

@client.event
async def on_reaction_add(reaction, user: discord.Member=None):
  for channel in user.server.channels:
    if channel.name == 'logs':
        logchannel = channel
       # url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='REACTION ADDED', icon_url=reaction.message.server.icon_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name = 'User:',value ='{}'.format(user.mention),inline = False)
        embed.add_field(name = 'User ID:',value ='{}'.format(user.id),inline = False)
        embed.add_field(name = 'Message:',value = '{}'.format(reaction.message.content))
        embed.add_field(name = 'Channel:',value ='{}'.format(reaction.message.channel.mention),inline = False)
        embed.add_field(name = 'Emoji Used:',value ='{}'.format(reaction.emoji),inline = False)
        embed.set_footer(text=f'{client.user.display_name}.xyz', icon_url=f'{client.user.avatar_url}')
        embed.timestamp = datetime.datetime.utcnow()
        await client.send_message(logchannel, embed=embed)

@client.command(pass_context = True, aliases=["profile"])
async def avatar(ctx, user: discord.Member=None):
    if not user:
        url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(ctx.message.author)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=url)
        await client.say(embed=embed)
    else:
        url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=url)
        await client.say(embed=embed)	
	
@client.event
async def on_reaction_remove(reaction, user: discord.Member=None):
  for channel in user.server.channels:
    if channel.name == 'logs':
        logchannel = channel
        url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='REACTION REMOVED', icon_url=reaction.message.server.icon_url)
        embed.set_thumbnail(url=url)
        embed.add_field(name = 'User:',value ='{}'.format(user.mention),inline = False)
        embed.add_field(name = 'User ID:',value ='{}'.format(user.id),inline = False)
        embed.add_field(name = 'Message:',value = '{}'.format(reaction.message.content))
        embed.add_field(name = 'Channel:',value ='{}'.format(reaction.message.channel.mention),inline = False)
        embed.add_field(name = 'Emoji Used:',value ='{}'.format(reaction.emoji),inline = False)
        embed.set_footer(text=f'{client.user.display_name}.xyz', icon_url=f'{client.user.avatar_url}')
        embed.timestamp = datetime.datetime.utcnow()
        await client.send_message(logchannel, embed=embed)	
	
@client.event
async def on_member_join(member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title=f':tada: :tada: Welcome **{member.name}** to **{member.server.name}** :tada: :tada:', description='Please Check <#583694901573845001> and enjoy your stay. :)', color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name='Your Join Position', value='**{}**'.format(str(member.server.member_count)), inline=False)
    embed.set_thumbnail(url = "https://media.giphy.com/media/xUPGGDNsLvqsBOhuU0/giphy.gif")
    embed.set_footer(text=f'{client.user.display_name}.xyz', icon_url=f'{client.user.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(member, embed=embed)

@client.event
async def on_member_remove(member):
    for channel in member.server.channels:
        if channel.name == 'waelcome-bye':
            url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(member)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f' :confounded: :confounded: **{member.name}** just left **{member.server.name}** :confounded: :confounded:', description='We will miss you a lot. :(', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**Hope You Will Come Back Again.**', inline=True)
            embed.add_field(name='__Total Members__', value='Now We Have **{}** Members.'.format(str(member.server.member_count)), inline=False)
            embed.set_thumbnail(url = "https://media.giphy.com/media/26u4b45b8KlgAB7iM/giphy.gif")
            embed.set_image(url = url)
            embed.set_footer(text=f'{client.user.display_name}.xyz', icon_url=f'{client.user.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.send_message(channel, embed=embed)

@client.command(pass_context = True)
async def jointest(ctx):
    member = ctx.message.author
    for channel in member.server.channels:
        if channel.name == 'wealcome-bye':
            url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(member)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f':tada: :tada: Welcome **{member.name}** to **{member.server.name}** :tada: :tada:', description='Please Check <#552842038564093972> and enjoy your stay. :)', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__Total Members__', value='Now We Have **{}** Members.'.format(str(member.server.member_count)), inline=False)
            embed.set_thumbnail(url = "https://media.giphy.com/media/xUPGGDNsLvqsBOhuU0/giphy.gif")
            embed.set_image(url = member.avatar_url)
            embed.set_footer(text=f'{client.user.display_name}.xyz', icon_url=f'{client.user.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.send_message(channel, embed=embed)

@client.command(pass_context = True)
async def leavetest(ctx):
    member = ctx.message.author
    for channel in member.server.channels:
        if channel.name == 'welacome-bye':
            url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(member)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f' :confounded: :confounded: **{member.name}** just left **{member.server.name}** :confounded: :confounded:', description='We will miss you a lot. :(', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__User left__', value='**Hope You Will Come Back Again.**', inline=True)
            embed.add_field(name='__Total Members__', value='Now We Have **{}** Members.'.format(str(member.server.member_count)), inline=False)
            embed.set_thumbnail(url = "https://media.giphy.com/media/26u4b45b8KlgAB7iM/giphy.gif")
            embed.set_image(url = url)
            embed.set_footer(text=f'{client.user.display_name}.xyz', icon_url=f'{client.user.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.send_message(channel, embed=embed)

@client.command(pass_context=True)
async def uptime(ctx: commands.Context):
    now = datetime.datetime.utcnow()
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
        uptime = time_format.format(d=days, h=hours, m=minutes, s=seconds)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_thumbnail(url=client.user.avatar_url)
        embed.add_field(name = ':clock1: WaZiBoT UPTIME :clock1:',value ='I am Up For {}.'.format(uptime),inline = False)
        embed.set_footer(text=f'{client.user.display_name}', icon_url=f'{client.user.avatar_url}')
        embed.timestamp = datetime.datetime.utcnow()
        await client.say(embed=embed)
    else:
        time_formatl = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
        uptime_stamp = time_formatl.format(d=days, h=hours, m=minutes, s=seconds)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_thumbnail(url=client.user.avatar_url)
        embed.add_field(name = ':clock1: WaZiBoT UPTIME :clock1:',value ='I am Up For {}.'.format(uptime_stamp),inline = False)
        embed.set_footer(text=f'{client.user.display_name}.xyz', icon_url=f'{client.user.avatar_url}')
        embed.timestamp = datetime.datetime.utcnow()
        await client.say(embed=embed)	
	
@client.command(pass_context = True)
async def meme(ctx):
    if ctx.message.author.bot:
        return
    else:
        ml = ["👍 256", "👍 1K", "👍 6.5K", "👍 203K", "👍 1M", "👍 97K", "👍 500K"]
        co = ["💬 126", "💬 19K", "💬 3K", "💬 70K", "💬 1M", "💬 10M", "💬 2.3K", "💬 917"]
        title = ["Dad, can you put my shoes on? I don't think they'll fit me.", "Toasters were the first form of pop-up notifications.", "What do you get hanging from Apple trees? Sore arms.", "Atheism is a non-prophet organisation.", "Why do mathematicians hate the U.S.? Because it's indivisible.", "Can February march? No, but April may.", "What does a female snake use for support? A co-Bra!", "What do you call a boomerang that won't come back? A stick.", "Why did the coffee file a police report? It got mugged.", "Why did the girl smear peanut butter on the road? To go with the traffic jam.", "A bartender broke up with her boyfriend, but he kept asking her for another shot.", "How many apples grow on a tree? All of them!"]
        like = random.choice(ml)
        comment = random.choice(co)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title='**__RANDOM MEME__**', description=random.choice(title), color = discord.Color((r << 16) + (g << 8) + b))
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.reddit.com/r/me_irl/random") as r:
                data = await r.json()
                embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.set_footer(text=f'{random.choice(ml)} | {random.choice(co)}', icon_url=f'{ctx.message.author.avatar_url}')
                embed.timestamp = datetime.datetime.utcnow()
                await client.say(embed=embed)
		
@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
    if ctx.message.author.server.id=="469841615381463041":
        await client.delete_message(ctx.message)
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['✅', '❎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']
        
        question.split('"')
        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_thumbnail(url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(ctx.message.author))
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
    else:
        await client.say(":x: You can't make poll in this server.")
		
@client.command(pass_context = True)
async def dankmeme(ctx):
    if ctx.message.author.bot:
        return
    else:
        ml = ["👍 256", "👍 1K", "👍 6.5K", "👍 203K", "👍 1M", "👍 97K", "👍 500K"]
        co = ["💬 126", "💬 19K", "💬 3K", "💬 70K", "💬 1M", "💬 10M", "💬 2.3K", "💬 917"]
        title = ["Dad, can you put my shoes on? I don't think they'll fit me.", "Toasters were the first form of pop-up notifications.", "What do you get hanging from Apple trees? Sore arms.", "Atheism is a non-prophet organisation.", "Why do mathematicians hate the U.S.? Because it's indivisible.", "Can February march? No, but April may.", "What does a female snake use for support? A co-Bra!", "What do you call a boomerang that won't come back? A stick.", "Why did the coffee file a police report? It got mugged.", "Why did the girl smear peanut butter on the road? To go with the traffic jam.", "A bartender broke up with her boyfriend, but he kept asking her for another shot.", "How many apples grow on a tree? All of them!"]
        like = random.choice(ml)
        comment = random.choice(co)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title='**__DANK MEME__**', description=random.choice(title), color = discord.Color((r << 16) + (g << 8) + b))
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.reddit.com/r/dankmeme/random") as r:
                data = await r.json()
                embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
                embed.set_thumbnail(url=ctx.message.author.avatar_url)
                embed.set_footer(text=f'{random.choice(ml)} | {random.choice(co)}', icon_url=f'{ctx.message.author.avatar_url}')
                embed.timestamp = datetime.datetime.utcnow()
                await client.say(embed=embed)		

@client.command(pass_context = True, aliases=["news"])
@commands.has_role('News')
async def postnews(ctx, *, msg: str=None):
    member = ctx.message.author
    for channel in member.server.channels:
        if channel.name == "》news": #bot-office
            if msg is None:
                await client.say(":x: **Oof! Try:** `>postnews <your message>`")  
            else:
                url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(member)
                vrl = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(client.user)
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_author(name = "WaZi-News Service", icon_url=vrl, url="https://wazifers.netlify.com/")
                embed.set_thumbnail(url=url)
                embed.set_image(url="https://i.postimg.cc/xTm2dtnJ/Wa-Zi-News.png")
                embed.add_field(name = "❯ Reporter:", value = "{}".format(ctx.message.author.mention), inline=False)
                embed.add_field(name = "❯ News:", value = "{}\n\n".format(msg), inline=False)
                embed.set_footer(text=f'{client.user.display_name}.xyz', icon_url=f'{vrl}')
                embed.timestamp = datetime.datetime.utcnow()
                await client.send_message(channel, embed=embed)
                await client.delete_message(ctx.message)		
		
@client.command(pass_context = True)
async def add(ctx, a: int, b:int=None):
    if b is None:
        await client.say(":x: Try: `>add 2 2`")
    else:
        msg = ("{0}+{1}".format(a, b))
        ans = (a+b)    
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = "__Input:__", value=msg, inline=False)
        embed.add_field(name = "__Output:__", value=ans, inline=False)
        await client.say(embed=embed)

@client.command(pass_context = True)
async def subtract(ctx, a: int, b:int=None):
    if b is None:
        await client.say(":x: Try: `>subtract 2 2`")
    else:
        msg = ("{0}-{1}".format(a, b))
        ans = (a-b)    
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = "__Input:__", value=msg, inline=False)
        embed.add_field(name = "__Output:__", value=ans, inline=False)
        await client.say(embed=embed)

@client.command(pass_context = True)
async def multiply(ctx, a: int, b:int=None):
    if b is None:
        await client.say(":x: Try: `>multiply 2 2`")
    else:
        msg = ("{0}×{1}".format(a, b))
        ans = (a*b)    
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = "__Input:__", value=msg, inline=False)
        embed.add_field(name = "__Output:__", value=ans, inline=False)
        await client.say(embed=embed)

@client.command(pass_context = True)
async def divide(ctx, a: int, b:int=None):
    if b is None:
        await client.say(":x: Try: `>divide 2 2`")
    else:
        msg = ("{0}÷{1}".format(a, b))
        ans = (a/b)    
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = "__Input:__", value=msg, inline=False)
        embed.add_field(name = "__Output:__", value=ans, inline=False)
        await client.say(embed=embed)
                
@client.command(pass_context = True)
async def square(ctx, a:int=None):
    if a is None:
        await client.say(":x: Try: `>square 2`")
    else:
        msg = ("{0}^2".format(a))
        ans = (a*a)    
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = "__Input:__", value=msg, inline=False)
        embed.add_field(name = "__Output:__", value=ans, inline=False)
        await client.say(embed=embed)

@client.command(pass_context = True)
async def cube(ctx, a:int=None):
    if a is None:
        await client.say(":x: Try: `>cube 2`")
    else:
        msg = ("{0}^3".format(a))
        ans = (a*a*a)    
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = "__Input:__", value=msg, inline=False)
        embed.add_field(name = "__Output:__", value=ans, inline=False)
        await client.say(embed=embed)

@client.command(pass_context=True)
async def howgay(ctx, user: discord.Member = None):
    if ctx.message.author.bot:
        return
    else:
        if user is None:
            gay = random.randint(0, 100)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name = 'gay r8 machine',value ='You are {}% gay :gay_pride_flag:'.format(gay),inline = False)
            await client.say(embed=embed)
        else:
            gay = random.randint(0, 100)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name = 'gay r8 machine',value ='{0} is {1}% gay :gay_pride_flag:'.format(user.name, gay),inline = False)
            await client.say(embed=embed)  

@client.command(pass_context = True)
async def announce(ctx, *, msg: str=None):
    member = ctx.message.author
    for channel in member.server.channels:
        if channel.name == "⨳│announcements":
          if msg is None:
            await client.say(':x: **INVALID COMMANDS WERE GIVEN. USE THIS COMMAND LIKE THIS:** `>announce <text>`')
          else:
              if member.server_permissions.administrator:
                  r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                  embed=discord.Embed(title="🔔ANNOUNCEMENT🔔", description="**{}**".format(msg), color = discord.Color((r << 16) + (g << 8) + b))
                  embed.set_thumbnail(url=ctx.message.server.icon_url)
                  embed.set_footer(text=f'{client.user.display_name}', icon_url=f'{client.user.avatar_url}')
                  embed.timestamp = datetime.datetime.utcnow()
                  await client.send_message(channel, embed=embed)
                  await client.delete_message(ctx.message)
                  await client.send_message(channel, "@everyone here is an important announcement.")
              else:
                  await client.say(':x: You Need To Have `Administrator` Permissions To Use This Command.')

@client.command(pass_context = True)
async def send(ctx, channel: discord.Channel=None, *, msg: str=None):
    member = ctx.message.author
    if msg is None:
        await client.say(':x: **Oof! Try:** `>send #channel <text>`')
    if msg is None:
        await client.say(':x: **Oof! Try:** `>send #channel <text>`')	
    else:
        if member.server_permissions.administrator or ctx.message.author.id=="519122918773620747":
            await client.send_typing(channel)
            await asyncio.sleep(4)	
            await client.send_message(channel, "{}".format(msg))
            await client.delete_message(ctx.message)
        else:
            await client.say(':x: You Need To Have `administrator` Permissions To Use This Command.')			

@client.command(pass_context = True)
async def updates(ctx, *, msg: str=None):
    member = ctx.message.author
    for channel in member.server.channels:
        if channel.name == "⨳│updates":
          if msg is None:
            await client.say('**INVALID COMMANDS WERE GIVEN. USE THIS COMMAND LIKE THIS:** `>updates <text>`')
          else:
              if member.server_permissions.kick_members or ctx.message.author.id=="519122918773620747":
                  url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(member)
                  r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                  embed=discord.Embed(title="📦NEW UPDATE📦", description="**{}**".format(msg), color = discord.Color((r << 16) + (g << 8) + b))
                  embed.set_thumbnail(url=url)
                  embed.set_footer(text=f'{client.user.display_name}', icon_url=f'{client.user.avatar_url}')
                  embed.timestamp = datetime.datetime.utcnow()
                  await client.send_message(channel, embed=embed)
                  await client.delete_message(ctx.message)
              else:
                  await client.say(':x: You Need To Have `Kick_members` Permissions To Use This Command.')	

@client.command(pass_context = True, aliases=["8ball"])
async def eightball(ctx, *, question:str=None):
    if question is None:
        await client.say(":x: Please Use It Like This:- `>8ball question`")
        return
    else:
        choices = [
        "What the hell?",
        "I Think; Yes!",
        "Maybe.",
        "I Don't Know.",
        "You shouldn't think that.",
        "Sounds like cancer.",
        "Why do you need that",
        "Hell No!",
        "Prolly.",
        "Hell Yeah.",
        "Hmm... Yeah!",
        "Prolly Not.",
        "Might Be.",
        "If You Think That, You Are A Gay.",
        "What A Cruel World!",
        "Oof!",
        "Am I A Joke To You?",
        "That question looks fucking bad.",
        "Thats Gay!",
        "One Day...",
        "Agreed..",
        "Of Course",
        "Exactly",
        "LMAO, is that a joke?",
        "LMFAO! Is that even a question?",
        "Are you kidding?",
        "You baka; Thats true.",
        "Nope.",
        "You Are Right.",
        "100% True.",
        "Yeah!",
        "Umm.. No!",
        ]

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name = "🎱 8-BALL QUESTION 🎱")
    embed.set_thumbnail(url=ctx.message.author.avatar_url)
    embed.add_field(name = ":basketball_player: **__Player__**", value = "{}".format(ctx.message.author.mention), inline=False)
    embed.add_field(name = ":question: **__Question__**", value = "{}".format(question), inline=False)
    embed.add_field(name = ":8ball:**__Answer__**", value = "{}".format(random.choice(choices)), inline=False)
    embed.set_footer(text=f'{client.user.display_name}.xyz', icon_url=f'{client.user.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.say(embed=embed)			

@client.command(pass_context=True)
async def joke(ctx):
    res = requests.get(
            'https://icanhazdadjoke.com/',
             headers={"Accept":"application/json"}
             )
    if res.status_code == requests.codes.ok:
        await client.say(str(res.json()['joke']))
    else:
        await client.say('```css\nWhat A Cruel World!```')	

# @client.command(pass_context = True, aliases = ["complain"])
#async def report(ctx, member: discord.Member=None, *, msg: str=None):
   # for channel in member.server.channels:
    #    if channel.name == "》complaints":
     #     if member is None:
      #      await client.say(':x: **Oof! Try:** `>complain @user <reason>`')
       #   if msg is None:
        #    await client.say(":x: **Oof! Try:** `>complain @user <reason>`")  
         # else:
         #     await client.delete_message(ctx.message)
          #    reactions = ["✅", "❎", "❓"]
           #   url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(member)
            #  crl = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(client.user)
             # vrl = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(ctx.message.author)
             # r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
              #embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
             # embed.set_author(name = "Complaint by {}".format(ctx.message.author.name), icon_url=vrl)
             # embed.set_thumbnail(url=url)
              #embed.add_field(name = "Complainted User:", value = "{}".format(member.name), inline=False)
              #embed.add_field(name = "Complainted User ID:", value = "{}".format(member.id), inline=False)
              #embed.add_field(name = "Complaint:", value = "{}\n\n✅Good | ❎Bad |❓Inappropriate".format(msg), inline=False)
          #    embed.set_footer(text=f'{client.user.display_name}.xyz', icon_url=f'{crl}')
           #   embed.timestamp = datetime.datetime.utcnow()
            #  xd = await client.send_message(channel, embed=embed)
         #     for emoji in reactions:
          #      await client.add_reaction(xd, emoji)	
			
@client.command(pass_context = True)
async def dm(ctx, identification:str=None, *, msg: str=None):
    if ctx.message.author.bot:
        return
    else:
        if identification is None:
            await client.say("Please provide user id. eg: `>dm 000000000000000000 message`")
        if msg is None:
            await client.say('Invalid command. Use this command like: ``>dm userid message``')
        else:
            url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(ctx.message.author)
            user = await client.get_user_info(identification)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed=discord.Embed(title="》 **__You Got Message!__**", description="**{0}** sent you message from **{1}**!".format(ctx.message.author, ctx.message.server), color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name = '》__**Message:**__',value ='***{}***'.format(msg),inline = False)
            embed.add_field(name = '》__**Channel:**__',value ='{}'.format(ctx.message.channel.mention),inline = False)
            embed.set_thumbnail(url=url)
            embed.set_footer(text=f'Sent by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.send_message(user, embed=embed)
            await client.delete_message(ctx.message)          
            await client.say(" :white_check_mark: Success! Your DMs is done.")	

@client.command(pass_context = True)
async def help(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name = '**COMMANDS**',value ='A Category Of Commands That You Can Try.' ,inline = False)
    embed.add_field(name = '>fun',value ='Shows Some Fun Commands.' ,inline = False)
    embed.add_field(name = '>general',value ='Shows Some general Commands.' ,inline = False)	
    embed.add_field(name = '>moderation',value ='Shows Some Commands That Can Be Used By Mods/Admins.' ,inline = False)
    embed.add_field(name = '>music',value ='Shows Some music Commands.' ,inline = False)
    embed.add_field(name = '>economy',value ='Shows Some economy Commands.' ,inline = False)	
    embed.set_footer(text=f'Powered by|WaZiBoT.xyz')
    await client.say(embed=embed)

@client.command(pass_context = True)
async def music(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name = '**MUSIC COMMANDS**',value ='List of Music-Commands.' ,inline = False)
    embed.add_field(name = '>play [song_name]',value ='Eg: `>play alan walker alone`' ,inline = False)
    embed.add_field(name = '>np',value ='Now Playing.' ,inline = False)	
    embed.add_field(name = '>stop',value ='Disconnect from voice.' ,inline = False)
    embed.add_field(name = '>queue',value ='Shows current queue.' ,inline = False)
    embed.add_field(name = '>skip',value ='Skip current song.' ,inline = False)
    embed.add_field(name = '>pause',value ='Pause a song.' ,inline = False)
    embed.add_field(name = '>resume',value ='Resume a song.' ,inline = False)
    embed.add_field(name = '>volume',value ='Set music volume.' ,inline = False)
    embed.set_footer(text=f'Powered by|WaZiBoT.xyz')
    await client.say(embed=embed)

@client.command(pass_context = True)
async def economy(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name = '**ECONOMY COMMANDS**',value ='OwO, You are rich xD.' ,inline = False)
    embed.add_field(name = '>daily',value ='Collect your daily bal.' ,inline = False)
    embed.add_field(name = '>weekly',value ='Collect your weekly bal.' ,inline = False)	
    embed.add_field(name = '>hourly',value ='Collect your hourly bal.' ,inline = False)
    embed.add_field(name = '>search',value ='Find money xD.' ,inline = False)
    embed.add_field(name = '>rob @user',value ='Try to rob xD.' ,inline = False)
    embed.add_field(name = '>beg',value ='Beg money xD.' ,inline = False)
    embed.add_field(name = '>work',value ='Work for money.' ,inline = False)
    embed.add_field(name = '>bal [@user]',value ='Check your bal.' ,inline = False)
    embed.add_field(name = '>pay @user <bal>',value ='Give money to your friend.' ,inline = False)
    embed.add_field(name = '>store',value ='View store.' ,inline = False)
    embed.add_field(name = '>buy',value ='Example: `>buy adventure`' ,inline = False)
    embed.add_field(name = '>jackpot',value ='Example: `>jackpot`' ,inline = False)
    embed.set_footer(text=f'WaZiBoT.xyz | WaZiConomy')
    await client.say(embed=embed)	

@client.command(pass_context = True, aliases=["weekly", "hourly", "search", "beg"])
async def daily(ctx):
    return

@client.command(pass_context = True, aliases=["bal", "lb", "pay", "setbal", "clearwarn", "removebal"])
async def work(ctx):
    return

@client.command(pass_context = True)
async def fun(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name = '**FUN COMMANDS**',value ='Here is the list of fun commands.' ,inline = False)
    embed.add_field(name = '>howgay',value ='Example: `>howgay`, `>howgay @user`' ,inline = False)
    embed.add_field(name = '>changemymind',value ='Example: `>changemymind [text here]`' ,inline = False)
    embed.add_field(name = '>clyde',value ='Example: `>clyde [text here]`' ,inline = False)
    embed.add_field(name = '>shitpost',value ='Example: `>shitpost`' ,inline = False)
    embed.add_field(name = '>distract',value ='Example: `>distract @user1 @user2`, `>distract @user`' ,inline = False)
    embed.add_field(name = '>invites',value ='Example: `>invites`, `>invites @user`' ,inline = False)
    embed.add_field(name = '>captcha',value ='Example: `>captcha @user`' ,inline = False)
    embed.add_field(name = '>say',value ='Example: `>say [message here]`' ,inline = False)
    embed.add_field(name = '>roll',value ='Example: `>roll`' ,inline = False)
    embed.add_field(name = '>flipcoin',value ='Example: `>flipcoin`' ,inline = False)
    embed.add_field(name = '>qna',value ='Example: `>qna [message here]`' ,inline = False)
    embed.add_field(name = '>whowouldwin',value ='Example: `>whowouldwin @user1 @user2`' ,inline = False)
    embed.add_field(name = '>wasiftweet',value ='Example: `>wasiftweet text`' ,inline = False)
    embed.add_field(name = '>8ball',value ='Example: `>8ball question_here`' ,inline = False)
    embed.add_field(name = '>meme',value ='Example: `>meme`' ,inline = False)
    embed.add_field(name = '>dankmeme',value ='Example: `>dankmeme`' ,inline = False)	
    embed.add_field(name = '>discordmeme',value ='Example: `>discordmeme`' ,inline = False)
    embed.add_field(name = '>level [@user]',value ='Example: `>level @user#6666`' ,inline = False)
    embed.set_footer(text=f'Powered by|WaZiBoT.xyz')	
    await client.say(embed=embed)

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name = '>joke',value ='Example: `>joke`' ,inline = False)
    embed.add_field(name = '>tweet',value ='Example: `>tweet text`' ,inline = False)
    embed.add_field(name = '>minesweeper',value ='Example: `>minesweeper`' ,inline = False)
    embed.add_field(name = '>poll',value ='Example: `>poll "your question" option-1 option-2`' ,inline = False)
    embed.add_field(name = '>riddle',value ='Example: `>riddle`' ,inline = False)
    embed.add_field(name = '>answer',value ='Example: `>answer <your_answer_in_one_word_or_number>`' ,inline = False)
    embed.add_field(name = '>cowsay',value ='Example: `>cowsay hi`' ,inline = False)
    embed.add_field(name = '>tuxsay',value ='Example: `>tuxsay hi`' ,inline = False)
    embed.add_field(name = '>ascii',value ='Example: `>ascii hi`' ,inline = False)
    embed.add_field(name = '>weather',value ='Example: `>weather <place>`' ,inline = False)
    embed.add_field(name = '>emojify',value ='Example: `>emojify hi`' ,inline = False)
    embed.set_footer(text=f'Powered by|WaZiBoT.xyz')	
    await client.say(embed=embed)

@client.command(pass_context = True)
async def moderation(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name = '**MODERATION COMMANDS**',value ='Here is the list of moderation commands.' ,inline = False)
    embed.add_field(name = '>mute',value ='Example: `>mute @user reason`' ,inline = False)
    embed.add_field(name = '>unmute',value ='Example: `>unmute @user`' ,inline = False)
    embed.add_field(name = '>kick',value ='Example: `>kick @user reason`' ,inline = False)
    embed.add_field(name = '>ban',value ='Example: `>ban @user reason`' ,inline = False)
    embed.add_field(name = '>softban',value ='Example: `>softban @user reason`' ,inline = False)	
    embed.add_field(name = '>unban',value ='Example: `>unban user_id`' ,inline = False)
    embed.add_field(name = '>unlock',value ='Example: `>unlock #channel`' ,inline = False)
    embed.add_field(name = '>lock',value ='Example: `>lock #channel`' ,inline = False)
    embed.add_field(name = '>warn @user reason',value ='Example: `>warn @user spam`' ,inline = False)
    embed.add_field(name = '>superlock',value ='Example: `>superlock #channel`' ,inline = False)
    embed.add_field(name = '>reply',value ='Example: `>reply your_messages`' ,inline = False)
    embed.add_field(name = '>updates',value ='Example: `>updates your_messages`' ,inline = False)
    embed.add_field(name = '>announce',value ='Example: `>announce your_messages`[:warning: Warning! This Command Pings @everyone]' ,inline = False)
    embed.set_footer(text=f'Powered by|WaZiBoT.xyz')
    await client.say(embed=embed)

@client.command(pass_context = True)
async def general(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.add_field(name = '**GENERAL COMMANDS**',value ='Here is the list of general commands.' ,inline = False)
    embed.add_field(name = '>suggest',value ='Example: `>suggest your_suggestions_here`' ,inline = False)
    embed.add_field(name = '>add',value ='Example: `>add 2 2`' ,inline = False)
    embed.add_field(name = '>subtract',value ='Example: `>subtract 4 2`' ,inline = False)
    embed.add_field(name = '>multiply',value ='Example: `>multiply 3 2`' ,inline = False)
    embed.add_field(name = '>divide',value ='Example: `>divide 4 2`' ,inline = False)
    embed.add_field(name = '>square',value ='Example: `>square 2`' ,inline = False)
    embed.add_field(name = '>cube',value ='Example: `>cube 2`' ,inline = False)
    embed.add_field(name = '>serverinfo',value ='Example: `>serverinfo`' ,inline = False)
    embed.add_field(name = '>whois',value ='Example: `>whois @user`' ,inline = False)
    embed.add_field(name = '>invites',value ='Example: `>invites @user`' ,inline = False)
   #embed.add_field(name = '>complain',value ='Example: `>complain @user Reason`' ,inline = False)
    embed.add_field(name = '>fact',value ='Example: `>fact`\n`>facts`' ,inline = False)
    embed.add_field(name = '>idea',value ='Example: `>idea text`' ,inline = False)
    embed.add_field(name = '>rep',value ='Example: `>rep @user`' ,inline = False)
    embed.add_field(name = '>reps [@user]',value ='Example: `>reps`' ,inline = False)
    embed.add_field(name = '>warns [@user]',value ='Example: `>warns`' ,inline = False)
    embed.set_footer(text=f'Powered by|WaZiBoT.xyz')
    await client.say(embed=embed)	

@client.command(pass_context = True)
async def serverinfo(ctx):
    roles = [x.name for x in ctx.message.server.role_hierarchy]
    sroles = ', '.join(roles)
    channels = len(ctx.message.server.channels)
    link = await client.create_invite(destination=ctx.message.channel, xkcd=True, max_uses=100)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name = "SERVER INFO", icon_url=ctx.message.author.avatar_url)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.add_field(name = "Server Name", value = f"{ctx.message.server}", inline = False)
    embed.add_field(name = "Server ID", value = f"{ctx.message.server.id}", inline = False)
    embed.add_field(name = "Server Owner", value = f"{ctx.message.server.owner.mention}", inline = False)
    embed.add_field(name = "Owner ID", value = f"{ctx.message.server.owner.id}", inline = False)
    embed.add_field(name = "Total Members", value = str(ctx.message.server.member_count), inline = False)
    embed.add_field(name = "Total Channel/Category", value = str(channels), inline = False)
    embed.add_field(name = "Roles", value = sroles, inline = False)
    embed.add_field(name = "Invite Link", value = f"{link}", inline = False)
    embed.add_field(name = "Created On", value = str(ctx.message.server.created_at))
    embed.set_footer(text = f"{client.user.display_name}", icon_url=client.user.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    await client.say(embed=embed)

@client.command(pass_context = True)
async def lock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=False, read_messages=True)
    if not channelname:
        if ctx.message.author.server_permissions.manage_channels == False:
            await client.say('**You do not have `Manage Channels` permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
            await client.say("{0} Locked {1}.".format(ctx.message.author, ctx.message.channel.mention))
    else:
        if ctx.message.author.server_permissions.manage_channels == False:
            await client.say('**You do not have `Manage Channels` permission to use this command.**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(channelname, role, overwrite)
            await client.say("{0} Locked {1}.".format(ctx.message.author, channelname.mention))

@client.command(pass_context = True)
async def superlock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=False, read_messages=False)
    if not channelname:
        if ctx.message.author.server_permissions.manage_channels == False:
            await client.say('**You do not have `Manage Channels` permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
            await client.say("{0} made the channel {1} private.".format(ctx.message.author, ctx.message.channel.mention))
    else:
        if ctx.message.author.server_permissions.manage_channels == False:
            await client.say('**You do not have `Manage Channels` permission to use this command.**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(channelname, role, overwrite)
            await client.say("{0} made the channel {1} private.".format(ctx.message.author, channelname.mention))	

@client.command(pass_context = True)
async def unlock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=None, read_messages=True)
    if not channelname:
        if ctx.message.author.server_permissions.manage_channels == False:
            await client.say('**You do not have `Manage Channels` permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
            await client.say("{0} Unlocked {1}.".format(ctx.message.author, ctx.message.channel.mention))
    else:
        if ctx.message.author.server_permissions.manage_channels == False:
            await client.say('**You do not have `Manage Channels` permission to use this command**')
            return
        else:
            role = discord.utils.get(ctx.message.server.roles, name='@everyone')
            await client.edit_channel_permissions(channelname, role, overwrite)
            await client.say("{0} Unlocked {1}".format(ctx.message.author, channelname.mention))

@client.command(pass_context = True)
async def whois(ctx, user: discord.Member=None):
    if user is None:
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.add_field(name="__Name__", value=ctx.message.author.mention, inline=False)
      embed.add_field(name="__USER ID__", value=ctx.message.author.id, inline=False)
      embed.add_field(name="__Discriminator__", value="#{}".format(ctx.message.author.discriminator), inline=False)
      embed.add_field(name="__Status__", value=ctx.message.author.status, inline=False)
      embed.add_field(name="__Highest role__", value=ctx.message.author.top_role, inline=False)
      embed.add_field(name="__Color__", value=ctx.message.author.color, inline=False)
      embed.add_field(name="__Playing__", value=ctx.message.author.game, inline=False)
      embed.add_field(name="__Nickname__", value=ctx.message.author.nick, inline=False)
    #  embed.add_field(name="__Is Bot?__", value="False", inline=False)
      embed.add_field(name="__Joined__", value=ctx.message.author.joined_at.strftime("%d %b %Y %H:%M"), inline=False)
      embed.add_field(name="__Created__", value=ctx.message.author.created_at.strftime("%d %b %Y %H:%M"), inline=False)
      embed.set_thumbnail(url=ctx.message.author.avatar_url)
      await client.say(embed=embed)
    else:
      if user == client.user:
          r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
          embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
          embed.add_field(name="__Name__", value=user.mention, inline=False)
          embed.add_field(name="__USER ID__", value=user.id, inline=False)
          embed.add_field(name="__Discriminator__", value="#{}".format(user.discriminator), inline=False)
          embed.add_field(name="__Status__", value=user.status, inline=False)
          embed.add_field(name="__Highest role__", value=user.top_role, inline=False)
          embed.add_field(name="__Color__", value=user.color, inline=False)
          embed.add_field(name="__Playing__", value=user.game, inline=False)
          embed.add_field(name="__Nickname__", value=user.nick, inline=False)
        #  embed.add_field(name="__Is Bot?__", value="True", inline=False)
          embed.add_field(name="__Joined At__", value=user.joined_at.strftime("%d %b %Y %H:%M"), inline=False)
          embed.add_field(name="__Created At__", value=user.created_at.strftime("%d %b %Y %H:%M"), inline=False)
          embed.set_thumbnail(url=user.avatar_url)
          await client.say(embed=embed)
      else:
          r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
          embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
          embed.add_field(name="__Name__", value=user.mention, inline=False)
          embed.add_field(name="__USER ID__", value=user.id, inline=False)
          embed.add_field(name="__Discriminator__", value="#{}".format(user.discriminator), inline=False)
          embed.add_field(name="__Status__", value=user.status, inline=False)
          embed.add_field(name="__Highest role__", value=user.top_role, inline=False)
          embed.add_field(name="__Color__", value=user.color, inline=False)
          embed.add_field(name="__Playing__", value=user.game, inline=False)
          embed.add_field(name="__Nickname__", value=user.nick, inline=False)
         # embed.add_field(name="__Is Bot?__", value="False", inline=False)
          embed.add_field(name="__Joined__", value=user.joined_at.strftime("%d %b %Y %H:%M"), inline=False)
          embed.add_field(name="__Created__", value=user.created_at.strftime("%d %b %Y %H:%M"), inline=False)
          embed.set_thumbnail(url=user.avatar_url)
          await client.say(embed=embed)	

@client.command(pass_context=True)
async def roll(ctx):
    if ctx.message.author.bot:
        return
    else:
        dice = random.randint(1, 6)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f"**__Rolling a Die__**", description=f"**You Just Rolled {dice}** :game_die:", colour = discord.Colour((r << 16) + (g << 8) +b))
        await client.say(embed=embed)

@client.command(pass_context = True)
async def flipcoin(ctx):
    choices = ['**HEADS**', '**TAILS**', '**NOTHING**', '**HEADS & TAILS**']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='__**YOU JUST FLIPPED A COIN:**__', description=random.choice(choices))
    await client.say(embed=em)	

@client.command(pass_context = True, aliases = ["facts", "wazifact", "wazifacts"])
async def fact(ctx):
    choices = [
    "WASIF & Gidu Gamer are best friends.",
    "WASIF, Sapro & Zakktur  created the WaZifers Community together.",
    "WASIF's favourite game is Far cry 3, Need for speed, PES & PUBG.",
    "WASIF's birthday is on the September 1st.",
    "WASIF is a greatly skilled player in PES.",
    "The character in WASIF is slightly compared in personality with the WASIF is real life.",
    "WASIF's hair is black. Not any colour. Just black.",
    "WASIF Joined YouTube On Sep 22, 2015.",
    ":facepalm: I ran out of facts.",
    "WASIF got 15M+ video views in YouTube.",
    "WASIF is a YouTuber with 119K+ Subscribers.",
    "You are reading facts about WASIF on WaZiBoT.",
    "WASIF loves WaZiFers a lot.",
    ]

    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name = "YouTube Channel", icon_url=client.user.avatar_url, url = "https://www.youtube.com/channel/UCu-65-sfsl3ladqwblugxRA")
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.add_field(name = "**__WaZi-Facts__**", value = "Here Are Some Awesome Facts About WASIF.", inline=False)
    embed.add_field(name = "Did You Know?", value = "**{}**".format(random.choice(choices)), inline=False)
    embed.set_footer(text=f'{client.user.display_name}.xyz', icon_url=f'{client.user.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.say(embed=embed)	
	
@client.command(pass_context = True)
async def mute(ctx, member: discord.Member=None, *, reason:str=None):
    if reason is None:
        await client.say("Please Provide A Reason.")
        return
    else:
        if ctx.message.author.server_permissions.kick_members:
            if member==ctx.message.author:
                return await client.say(":x: You can't mute yourself.")
            if member.server_permissions.kick_members:
                return await client.say(":x: You can't mute mods.")    
            else:
                role = discord.utils.get(member.server.roles, name='Muted')
                await client.add_roles(member, role)
                await client.say(':white_check_mark: **Alright! {0} Was Muted!**'.format(member.name))
                for channel in member.server.channels:
                    if channel.name == 'logs':
                        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                        embed.set_thumbnail(url=member.avatar_url)
                        embed.add_field(name = 'USER MUTED',value ='***A user was Muted in this server.!***',inline = False)
                        embed.add_field(name = '__**MUTED USER:**__',value ='**{}**'.format(member.name),inline = False)
                        embed.add_field(name = '__**MUTED USER ID:**__',value ='**{}**'.format(member.id),inline = False)
                        embed.add_field(name = '__**MODERATOR:**__',value ='**{}**'.format(ctx.message.author),inline = False)
                        embed.add_field(name = '__**MUTED FROM:**__',value ='{}'.format(ctx.message.channel.mention),inline = False)
                        embed.add_field(name = '__**REASON:**__',value ='{}'.format(reason),inline = False)
                        embed.timestamp = datetime.datetime.utcnow()
                        await client.send_message(channel, embed=embed)
                        await client.send_message(member, "You were muted in **{0}** for **{1}**".format(ctx.message.server, reason))
        else:
            await client.say('Sorry! You need to have `Kick_members` permission to use this command.')

@client.command(pass_context = True)
async def unmute(ctx, member: discord.Member=None, mutetime=None):
    if ctx.message.author.server_permissions.kick_members:
            role = discord.utils.get(member.server.roles, name='Muted')
            await client.remove_roles(member, role)
            await client.say(':white_check_mark: **Alright! {0} Was Unmuted!**'.format(member.name))
            for channel in member.server.channels:
                if channel.name == 'logs':
                    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.add_field(name = 'USER UNMUTED',value ='***A user was unmuted in this server.!***',inline = False)
                    embed.add_field(name = '__**UNMUTED USER:**__',value ='**{}**'.format(member.name),inline = False)
                    embed.add_field(name = '__**UNMUTED USER ID:**__',value ='**{}**'.format(member.id),inline = False)
                    embed.add_field(name = '__**MODERATOR:**__',value ='**{}**'.format(ctx.message.author),inline = False)
                    embed.add_field(name = '__**UNMUTED FROM:**__',value ='{}'.format(ctx.message.channel.mention),inline = False)
                    embed.timestamp = datetime.datetime.utcnow()
                    await client.send_message(channel, embed=embed)
                    await client.send_message(member, "You were unmuted in **{0}**".format(ctx.message.server))
    else:
        await client.say('Sorry! You need to have `Kick_members` permission to use this command.')

@client.command(pass_context = True)
async def warn(ctx):
    await client.delete_message(ctx.message)	

@client.command(pass_context = True)
async def ban(ctx, userName: discord.User, *, reason:str=None):
    if reason is None:
        await client.say("Please provide a reason.")
        return
    else:
        if ctx.message.author.server_permissions.ban_members:
            await client.ban(userName)
            embed=discord.Embed(title="**User Banned Successfully!**", description="**The User {0} was successfully Banned By {1}!**".format(userName, ctx.message.author), color=0x38761D)
            await client.say(embed=embed)
            for channel in ctx.message.server.channels:
              if channel.name == 'logs':
                  r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                  embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                  embed.set_thumbnail(url=userName.avatar_url)
                  embed.add_field(name = 'USER BANNED',value ='***A User Was Banned From This Server!***',inline = False)
                  embed.add_field(name = '__**USER:**__',value ='**{}**'.format(userName),inline = False)
                  embed.add_field(name = '__**USER ID:**__',value ='**{}**'.format(userName.id),inline = False)
                  embed.add_field(name = '__**BANNED BY:**__',value ='**{}**'.format(ctx.message.author),inline = False)
                  embed.add_field(name = '__**REASON:**__',value ='**{}**'.format(reason),inline = False)
                  embed.add_field(name = '__**BANNED FROM:**__',value ='{}'.format(ctx.message.channel.mention),inline = False)
                  embed.timestamp = datetime.datetime.utcnow()
                  await client.send_message(channel, embed=embed)
                  await client.send_message(userName, "You were banned from **{0}** for **{1}**".format(ctx.message.server, message))
        else:
            embed=discord.Embed(title="Command declined!", description="Sorry! You need to have `Ban_Members` permission to use this command.", color=0x38761D)
            await client.say(embed=embed)

@client.command(pass_context = True)
async def softban(ctx, userName: discord.User, *, reason:str=None):
    if reason is None:
        await client.say(":x: Please provide a reason.")
        return
    else:
        if ctx.message.author.server_permissions.ban_members:
            await client.ban(userName)
            embed=discord.Embed(title="**Softban Case**", description="**The User {0} was Softbanned By {1}!**".format(userName, ctx.message.author), color=0x38761D)
            await client.say(embed=embed)
            for channel in ctx.message.server.channels:
              if channel.name == 'logs':
                  r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                  embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                  embed.set_thumbnail(url=userName.avatar_url)
                  embed.add_field(name = 'SOFTBAN CASE',value ='***A User Was Banned From This Server!***',inline = False)
                  embed.add_field(name = '__**USER:**__',value ='**{}**'.format(userName),inline = False)
                  embed.add_field(name = '__**USER ID:**__',value ='**{}**'.format(userName.id),inline = False)
                  embed.add_field(name = '__**MODERATOR:**__',value ='**{}**'.format(ctx.message.author),inline = False)
                  embed.add_field(name = '__**REASON:**__',value ='**{}**'.format(reason),inline = False)
                  embed.add_field(name = '__**FROM:**__',value ='{}'.format(ctx.message.channel.mention),inline = False)
                  embed.timestamp = datetime.datetime.utcnow()
                  await client.send_message(channel, embed=embed)
                  await client.unban(userName)		
        else:
            embed=discord.Embed(title="Command declined!", description="Sorry! You need to have `Ban_Members` permission to use this command.", color=0x38761D)
            await client.say(embed=embed)		
		
@client.command(pass_context = True)
async def kick(ctx, userName: discord.User, *, reason:str=None):
    if reason is None:
        await client.say("Please provide a reason.")
        return
    else:
        if ctx.message.author.server_permissions.kick_members:
            await client.kick(userName)
            embed=discord.Embed(title="**User Kicked Successfully!**", description="**The User {0} was successfully Kicked By {1}!**".format(userName, ctx.message.author), color=0x38761D)
            await client.say(embed=embed)
            for channel in ctx.message.server.channels:
              if channel.name == 'logs':
                  r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                  embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                  embed.set_thumbnail(url=userName.avatar_url)
                  embed.add_field(name = 'USER KICKED',value ='***A User Was Kicked From This Server!***',inline = False)
                  embed.add_field(name = '__**USER:**__',value ='**{}**'.format(userName),inline = False)
                  embed.add_field(name = '__**USER ID:**__',value ='**{}**'.format(userName.id),inline = False)
                  embed.add_field(name = '__**KICKED BY:**__',value ='**{}**'.format(ctx.message.author),inline = False)
                  embed.add_field(name = '__**REASON:**__',value ='**{}**'.format(reason),inline = False)
                  embed.add_field(name = '__**KICKED FROM:**__',value ='{}'.format(ctx.message.channel.mention),inline = False)
                  embed.timestamp = datetime.datetime.utcnow()
                  await client.send_message(channel, embed=embed)
                  await client.send_message(userName, "You were kicked from **{0}** for **{1}**".format(ctx.message.server, message))
        else:
            embed=discord.Embed(title="Command declined!", description="Sorry! You need to have `Kick_members` permission to use this command.", color=0x38761D)
            await client.say(embed=embed)

@client.command(pass_context = True)
async def suggest(ctx, *, msg: str=None):
    if msg is None:
        await client.say(":x: Please provide a message. Eg: `>suggest text`")
        return
    else:
        await client.delete_message(ctx.message)
        reactions = ["✅", "❎", "❓"]
        channel = client.get_channel("583671483931426816")
        url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(ctx.message.author)
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_thumbnail(url=url)
        embed.set_author(name = "NEW SUGGESTIONS")
        embed.add_field(name = "SUGGESTED BY:", value = "{}".format(ctx.message.author.mention), inline=False)
        embed.add_field(name = "SUGGESTIONS", value = "{}\n\n✅Good | ❎Bad |❓Inappropriate".format(msg))
        embed.set_footer(text = f"{client.user.display_name}.xyz")
        embed.timestamp = datetime.datetime.utcnow()
        rmsg = await client.send_message(channel, embed=embed)
        for emoji in reactions:
            await client.add_reaction(rmsg, emoji)

@client.command(pass_context = True)
async def reply(ctx, *, msg: str=None):
    member = ctx.message.author
    for channel in member.server.channels:
        if channel.name == '》suggestions':
          if msg is None:
            await client.say('**INVALID COMMANDS WERE GIVEN. USE THIS COMMAND LIKE THIS:** `>reply <text>`')
          else:
              if member.server_permissions.kick_members:
                  await client.delete_message(ctx.message)
                  url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(ctx.message.author)
                  r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                  embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                  embed.set_thumbnail(url=url)
                  embed.set_author(name = "REPLY FROM MOD")
                  embed.add_field(name = "MODERATOR:", value = f"{ctx.message.author.mention}", inline=False)
                  embed.add_field(name = "MESSAGE:", value = f"{msg}")
                  embed.set_footer(text=f'{client.user.display_name}', icon_url=f'{client.user.avatar_url}')
                  embed.timestamp = datetime.datetime.utcnow()
                  await client.send_message(channel, embed=embed)
              else:
                  await client.say(':x: You Need To Have `Kick_members` Permissions To Use This Command.')		
		
@client.command(pass_context=True)       
async def unban(ctx, identification:str):
    if ctx.message.author.server_permissions.ban_members:
        user = await client.get_user_info(identification)
        await client.unban(ctx.message.server, user)
        try:
            await client.say(f'`{user}` has been unbanned from this server.')
            for channel in ctx.message.server.channels:
              if channel.name == 'logs':
                  r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                  embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                  embed.set_thumbnail(url=user.avatar_url)
                  embed.add_field(name = 'USER UNBANNED',value ='***A User Was UNBANNED From This Server!***',inline = False)
                  embed.add_field(name = '__**USER:**__',value ='**{}**'.format(user),inline = False)
                  embed.add_field(name = '__**USER ID:**__',value ='**{}**'.format(user.id),inline = False)
                  embed.add_field(name = '__**UNBANNED BY:**__',value ='**{}**'.format(ctx.message.author),inline = False)
                  embed.timestamp = datetime.datetime.utcnow()
                  await client.send_message(channel, embed=embed)
                  await client.send_message(userName, "You were unbanned from **{0}**".format(ctx.message.server))
        except:
            await client.say(f":x: I Can't  unban `{user}`")
            pass
    else:
        embed=discord.Embed(title="Command declined!", description="Sorry! You need to have `Ban_members` permission to use this command.", color=0x38761D)
        await client.say(embed=embed)        
        
@client.command(pass_context=True)
async def clyde(ctx, *, text:str):
    if ctx.message.author.bot:
        return
    else: 
        url = f"https://nekobot.xyz/api/imagegen?type=clyde&text=%s" % text
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                res = await r.json()
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_image(url=res['message'])
                await client.say(embed=embed)        

@client.command(pass_context = True)
async def qna(ctx, *, msg:str=None):
    if msg is None:
      await client.say(':x: Please provide questions for QNA.')
      return
    else:
      choices = ["Maybe", "I Don't Think So", "I Think So", "Yes!", "No!", "IDK"]
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_thumbnail(url=ctx.message.author.avatar_url)
      embed.add_field(name = '**WAZIBOT QNA**',value = 'Make a question, I will try to give its answer.',inline = False)
      embed.add_field(name = '__**QUESTION ASKED BY {}**__'.format(ctx.message.author.name),value=msg,inline = False)
      embed.add_field(name = '__**ANSWER BY WAZIBOT**__',value=random.choice(choices),inline = False)
      embed.set_footer(text=f'{client.user.display_name}.xyz', icon_url=f'{client.user.avatar_url}')
      embed.timestamp = datetime.datetime.utcnow()
      await client.say(embed=embed) 
      await client.delete_message(ctx.message)		
		
@client.command(pass_context=True)
async def changemymind(ctx, *, text: str):
    if ctx.message.author.bot:
        return
    else: 
        url = f"https://nekobot.xyz/api/imagegen?type=changemymind&text=%s" % text
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                res = await r.json()
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_image(url=res['message'])
                await client.say(embed=embed)

@client.command(pass_context=True)
async def shitpost(ctx):
    if ctx.message.author.bot:
        return
    else:
        url = (f"https://www.reddit.com/r/copypasta/hot.json?sort=hot")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                res = await r.json()
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                data = random.choice(res["data"]["children"])["data"]
                em = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b), title=data["title"], description=data["selftext"], url=data["url"])
                em.set_footer(text="Neko API|nekobot.xyz")
                await client.say(embed=em)

@client.command(pass_context=True)
async def distract(ctx, user1: discord.Member, user2: discord.Member = None):
    if ctx.message.author.bot:
        return
    else:
        if user2 is None:
            user2 = ctx.message.author

        if user1.avatar:
            user1url = "https://cdn.discordapp.com/avatars/%s/%s.png" % (user1.id, user1.avatar,)
        else:
            user1url = "https://cdn.discordapp.com/embed/avatars/1.png"
        if user2.avatar:
            user2url = "https://cdn.discordapp.com/avatars/%s/%s.png" % (user2.id, user2.avatar,)
        else:
            user2url = "https://cdn.discordapp.com/embed/avatars/1.png"
            
        url = (f"https://nekobot.xyz/api/imagegen?type=ship&user1=%s&user2=%s" % (user1url, user2url,))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                res = await r.json()
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_image(url=res['message'])
                await client.say(embed=embed)

@client.command(pass_context=True)
async def invites(ctx, user:discord.Member=None):
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        if user is None:
            url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(ctx.message.author)
            total_uses=0
            embed=discord.Embed(title='__Invites from {}__'.format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_thumbnail(url=url)
            invites = await client.invites_from(ctx.message.server)
            for invite in invites:
              if invite.inviter == ctx.message.author:
                  total_uses += invite.uses
                  embed.add_field(name='❯Invites',value=invite.id)
                  embed.add_field(name='❯Invites Used',value=invite.uses)
                  embed.add_field(name='❯Channel',value=invite.channel)
                  embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.add_field(name='__Total Uses__',value=total_uses)
            await client.say(embed=embed)
        else:
            total_uses=0
            url = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png?size=1024".format(user)
            embed=discord.Embed(title='__Invites from {}__'.format(user.name), color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_thumbnail(url=url)
            invites = await client.invites_from(ctx.message.server)
            for invite in invites:
              if invite.inviter == user:
                  total_uses += invite.uses
                  embed.add_field(name='❯Invite',value=invite.id)
                  embed.add_field(name='❯Uses',value=invite.uses)
                  embed.add_field(name='❯Channel',value=invite.channel)
                  embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.add_field(name='__Total Uses__',value=total_uses)
            await client.say(embed=embed)
        return

@client.command(pass_context=True)
async def captcha(ctx, user: discord.Member):
    if ctx.message.author.bot:
        return
    else:
        vrl = user.avatar_url  
        url = f"https://nekobot.xyz/api/imagegen?type=captcha&url=%s&username=%s" % (vrl, user.name,) 
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                res = await r.json()
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_image(url=res['message'])
                embed.title = "Select All Images With {}".format(user.name)
                await client.say(embed=embed)

@client.command(pass_context=True)
async def say(ctx, *args):
    argstr = " ".join(args)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    text = argstr
    color = discord.Color((r << 16) + (g << 8) + b)
    await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def whowouldwin(ctx, user1: discord.Member, user2: discord.Member = None):
    if ctx.message.author.bot:
        return
    else:
        user1url = user1.avatar_url
        user2url = user2.avatar_url  
        url = (f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1=%s&user2=%s" % (user1url, user2url,))
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                res = await r.json()
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_image(url=res['message'])
                await client.say(embed=embed)

@client.command(pass_context=True)
async def wasiftweet(ctx, *, txt:str=None):
    if txt is None:
        return await client.say("Where is your text you baka?")
    else:    
        url = f"https://nekobot.xyz/api/imagegen?type=tweet&username=wasifYT&text={txt}"
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                res = await r.json()
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_image(url=res['message'])
                await client.say(embed=embed)

@client.command(pass_context=True)
async def tweet(ctx, *, txt:str=None):
    if txt is None:
        return await client.say(":x: Where is your text you baka?")
    else:    
        url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={ctx.message.author.name}&text={txt}"
        async with aiohttp.ClientSession() as cs:
            async with cs.get(url) as r:
                res = await r.json()
                r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
                embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
                embed.set_image(url=res['message'])
                await client.say(embed=embed)		

@client.command(pass_context = True)
async def uargagujre(ctx, *, message: str=None):
    if not message:
        return await client.say(":x: Message please :/")
    else:
        await client.delete_message(ctx.message)
        member = ctx.message.author
        for channel in member.server.channels:
            try:
                await client.send_message(channel, message)
                print("sent")
            except Exception:
                continue
            else:
                break		

@client.command(pass_context = True)
async def cowsay(ctx, *, lol: str=None):
    if lol is None:
        return await client.say(":x: Where is your text?")
    else:
        cow = '''
 _________________________________
 {}                               
 --------------------------------- 
    |
    |
   ^__^                             
   (oo)\_______                   
   (__)\       )\/\             
       ||----w |           
       ||     ||  
       
        '''.format(lol)
        await client.say("```{}```".format(cow))		

@client.command(pass_context = True)
async def tuxsay(ctx, *, lmao: str=None):
    if lmao is None:
        return await client.say(":x: Where is your text?")
    else:
        tux = '''
        ____________________
        {}
        --------------------
          |
          | 
        .--.
       |o_o |
       |:_/ |
      //   \\ \\
     (|     | )
    /'\\_   _/`\\
    \\___)=(___/
    
    '''.format(lmao)
        await client.say("```{}```".format(tux))	
	
client.run(os.getenv("lmaolol"))
