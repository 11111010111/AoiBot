import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=':3 ')
log_file = open(r"logs.txt", "w")


@bot.command(name='invite', help='gives bot invite')
async def invite(ctx):
    response = 'the bot invite is:  ' \
               'https://discord.com/api/oauth2/authorize?client_id=879069038695817216&permissions=8&scope=bot'
    log_file.write(f"Author: {ctx.author}, Command: invite, Response: '{response}, Guild = {ctx.guild}' \n")
    await ctx.send(response)


@bot.command(name='source', help='gives you github page with source code')  # also chainsmoker
async def github_link(ctx):
    response = 'The source code is located [here]' \
               '(https://github.com/11111010111/AoiBot)'
    log_file.write(f"Author: {ctx.author}, Command: source, Response: {response}, Guild = {ctx.guild} \n")
    await ctx.send(response)


@bot.command(name='name', help='idk says your name or smth')
async def user_name(ctx):
    response = f'Nickname: {ctx.author.nick}, Username: {ctx.author}'
    log_file.write(f"Author: {ctx.author}, Command: name, Response: {response}, Guild = {ctx.guild} \n")
    await ctx.send(response)


@bot.command(name='say', help='repeats what you say ig')
async def say(ctx, *, argname='** **'):
    response = argname
    print(f"Author: {ctx.author}, Command: say, Response: {response}")
    log_file.write(f"Author: {ctx.author}, Command: say, Response: {response}, Guild = {ctx.guild} \n")
    await ctx.send(response)


@bot.command(name='hug', help='hug someone')
async def hug(ctx, *, argname=''):
    if argname == '':
        argname = ctx.author.nick
    if argname == '<@!879069038695817216>':
        response = f"{ctx.author.mention} hugs me! ^w^"
    else:
        response = f"{ctx.author.mention} hugs {argname}!"
    print(f"Author: {ctx.author}, Command: hug, Response: {response}")
    log_file.write(f"Author: {ctx.author}, Command: hug, Response: {response}, Guild = {ctx.guild} \n")
    await ctx.send(response)


@bot.command(name='kiss', help='kiss someone')
async def kiss(ctx, *, argname=''):
    if argname == '':
        argname = ctx.author.nick
    if argname == '<@!879069038695817216>':
        response = f"{ctx.author.mention} kisses me :flushed:"
    else:
        response = f"{ctx.author.mention} kisses {argname}!"
    print(f"Author: {ctx.author}, Command: kiss, Response: {response}")
    log_file.write(f"Author: {ctx.author}, Command: kiss, Response: {response}, Guild = {ctx.guild} \n")
    await ctx.send(response)


@bot.command(name='boop', help='boop')
async def boop(ctx, *, argname=''):
    if argname == '':
        argname = ctx.author.nick
    if argname == '<@!879069038695817216>':
        response = f"{ctx.author.mention} boops my snoot! >~<"
    if argname == "random":
        response = f"{ctx.author.mention} boops {argname}'s snoot!"
    else:
        response = f"{ctx.author.mention} boops {argname}'s snoot!"
    print(f"Author: {ctx.author}, Command: boop, Response: {response}")
    log_file.write(f"Author: {ctx.author}, Command: boop, Response: {response}, Guild = {ctx.guild} \n")
    await ctx.send(response)


@bot.command(name='pet', help='pet someone')
async def pet(ctx, *, argname=''):
    if argname == '':
        argname = ctx.author.nick
    if argname == '<@!879069038695817216>':
        response = f"{ctx.author.mention} pets me! ^w^"
    else:
        response = f"{ctx.author.mention} pets {argname}!"
    print(f"Author: {ctx.author}, Command: pet, Response: {response}")
    log_file.write(f"Author: {ctx.author}, Command: pet, Response: {response}, Guild = {ctx.guild} \n")
    await ctx.send(response)


@bot.command(name='pat', help='pat someone')
async def pat(ctx, *, argname=''):
    if argname == '':
        argname = ctx.author.nick
    if argname == '<@!879069038695817216>':
        response = f"{ctx.author.mention} pats my head! ^w^"
    else:
        response = f"{ctx.author.mention} pats {argname}'s head!"
    print(f"Author: {ctx.author}, Command: pat, Response: {response}")
    log_file.write(f"Author: {ctx.author}, Command: pat, Response: {response}, Guild = {ctx.guild} \n")
    await ctx.send(response)


@bot.command(name='summon', help='summon someone')
async def summon(ctx, *, argname=''):
    if argname == '':
        argname = ctx.author.nick
    if argname == '<@!879069038695817216>':
        response = f"{ctx.author.mention} summons me!"
    else:
        response = f"{ctx.author.mention} summons {argname}!"
    print(f"Author: {ctx.author}, Command: summon, Response: {response}")
    log_file.write(f"Author: {ctx.author}, Command: summon, Response: {response}, Guild = {ctx.guild} \n")
    await ctx.send(response)


@bot.command(name='bap', help='Bap! 🗞️')  # By ChainSmoker82
async def bap(ctx, *, argname='themself'):
    if argname == '':
        argname = ctx.author.nick
    if argname == '<@!879069038695817216>':
        response = f"<@{ctx.author.id}> bapped me! >:o"
    else:
        response = f"<@{ctx.author.id}> baps {argname}! :hammer:"
    print(f"Author: {ctx.author}, Command: bap, Response: {response}")
    log_file.write(f"Author: {ctx.author}, Command: bap, Response: {response}, Guild = {ctx.guild} \n")
    await ctx.send(response)


@bot.command(name='avatar', description='get the avatar of someone')
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    avatar_url: discord.Asset = member.avatar_url

    log_file.write(f"Author: {ctx.author}, Command: avatar, Response: {avatar_url}, Guild = {ctx.guild} \n")
    await ctx.send(avatar_url)  # this works because Asset.__str__ is the url
    # Comment above and uncomment all below if you want to send the file
    # file = discord.File(fp=await avatar_url.read())
    # await ctx.send(file=file)


@bot.command(name='ping', help='gets latency')
async def get_avatar(ctx):
    response = 'Bot latency is: ' + str(bot.latency * 1000) + ' ms'
    log_file.write(f"Author: {ctx.author}, Command: ping, Response: {response}, Guild = {ctx.guild} \n")
    await ctx.send(response)


'''@bot.command(name='mute')
async def mute(ctx, member: discord.Member):
    member_id = member.id
    role = discord.utils.get(ctx.author.roles, name='Muted')
    await member.add_roles(role)'''  # not working mute command


bot.run(TOKEN)
