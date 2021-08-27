import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix=':3 ')


@bot.command(name='invite', help='gives bot invite')
async def invite(ctx):
    response = 'the bot invite is:  ' \
               'https://discord.com/api/oauth2/authorize?client_id=879069038695817216&permissions=8&scope=bot'
    await ctx.send(response)


@bot.command(name='name', help='idk says your name or smth')
async def user_name(ctx):
    response = f'Nickname: {ctx.author.nick}, Username: {ctx.author}'
    await ctx.send(response)


@bot.command(name='say', help='repeats what you say ig')
async def say(ctx, *, argname='** **'):
    response = argname
    await ctx.send(response)


@bot.command(name='hug', help='hug someone')
async def kiss(ctx, *, argname=''):
    if argname == '':
        argname = ctx.author.nick
    if argname == '<@!879069038695817216>':
        response = f"{ctx.author.mention} hugs me! ^w^"
    else:
        response = f"{ctx.author.mention} hugs {argname}!"
    print(f"Author: {ctx.author}, Command: hug, Response: {response}")
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
    await ctx.send(response)


@bot.command(name='boop', help='boop')
async def kiss(ctx, *, argname=''):
    if argname == '':
        argname = ctx.author.nick
    if argname == '<@!879069038695817216>':
        response = f"{ctx.author.mention} boops my snoot! >~<"
    else:
        response = f"{ctx.author.mention} boops {argname}'s snoot!"
    print(f"Author: {ctx.author}, Command: boop, Response: {response}")
    await ctx.send(response)


@bot.command(name='pet', help='pet someone')
async def kiss(ctx, *, argname=''):
    if argname == '':
        argname = ctx.author.nick
    if argname == '<@!879069038695817216>':
        response = f"{ctx.author.mention} pets me! ^w^"
    else:
        response = f"{ctx.author.mention} pets {argname}!"
    print(f"Author: {ctx.author}, Command: pet, Response: {response}")
    await ctx.send(response)


@bot.command(name='pat', help='pat someone')
async def kiss(ctx, *, argname=''):
    if argname == '':
        argname = ctx.author.nick
    if argname == '<@!879069038695817216>':
        response = f"{ctx.author.mention} pats my head! ^w^"
    else:
        response = f"{ctx.author.mention} pats {argname}'s head!"
    print(f"Author: {ctx.author}, Command: pat, Response: {response}")
    await ctx.send(response)


@bot.command(name='summon', help='summon someone')
async def kiss(ctx, *, argname=''):
    if argname == '':
        argname = ctx.author.nick
    if argname == '<@!879069038695817216>':
        response = f"{ctx.author.mention} summons me!"
    else:
        response = f"{ctx.author.mention} summons {argname}!"
    print(f"Author: {ctx.author}, Command: summon, Response: {response}")
    await ctx.send(response)


@bot.command(name='avatar', description='get the avatar of someone')
async def avatar(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.author

    avatar_url: discord.Asset = member.avatar_url

    await ctx.send(avatar_url)  # this works because Asset.__str__ is the url
    # Comment above and uncomment all below if you want to send the file
    # file = discord.File(fp=await avatar_url.read())
    # await ctx.send(file=file)


@bot.command(name='ping', help='gets latency')
async def get_avatar(ctx):
    response = 'Bot latency is: ' + str(bot.latency * 1000) + ' ms'
    await ctx.send(response)


'''@bot.command(name='mute')
async def mute(ctx, member: discord.Member):
    member_id = member.id
    role = discord.utils.get(ctx.author.roles, name='Muted')
    await member.add_roles(role)'''


bot.run(TOKEN)
