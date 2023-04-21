import pandas as pd
import discord
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='?',intents=discord.Intents.all())
 
#bot login
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')

#'verify' Command -> check account exist and give 'verified' role
@bot.command()
async def verify(ctx,account:str): 
    df = pd.read_csv('account.csv',sep=',',header=0)
    if(df['Email']==account).any():
        user=ctx.message.author
        role=ctx.guild.get_role(--)
        await user.add_roles(role)
        await ctx.send(f'you are verified!')
    else:
        await ctx.send(f'please check your email')
        
#'verify' Command error handling
@verify.error
async def verify_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.BadArgument):
        await ctx.send(f'please check your email')

bot.run('--')
