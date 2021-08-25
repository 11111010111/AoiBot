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


@bot.command(name='hug', help='pretty obvious i think')
async def hug(ctx, *, argname='** **'):
    response = f'<@{ctx.author.id}> hugs {argname}'
    await ctx.send(response)


@bot.command(name='kiss', help='yup')
async def kiss(ctx, *, argname='themself'):
    response = f'<@{ctx.author.id}> kisses {argname}'
    await ctx.send(response)


@bot.command(name='boop', help='boop')
async def kiss(ctx, *, argname=''):
    if argname == '':
        argname = ctx.author.nick
    response = f"<@{ctx.author.id}> boops {argname}'s snoot"
    await ctx.send(response)


@bot.command(name='pet', help='well... pets')
async def kiss(ctx, *, argname='themself'):
    response = f'<@{ctx.author.id}> pets {argname}'
    await ctx.send(response)


@bot.command(name='summon', help='summon something')
async def summon(ctx, *, argname='nothing'):
    response = f'<@{ctx.author.id}> summons {argname}'
    await ctx.send(response)


@bot.command(name='avatar', help='avatar')
async def get_avatar(ctx):
    response = ctx.author.avatar_url
    await ctx.send(response)


bot.run(TOKEN)
