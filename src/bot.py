'''
    Module for handling discord bot
'''

from discord.ext import commands
from googlesearch import search

from src.data_storage import DataStorage

bot = commands.Bot(command_prefix='!')

@bot.command()
async def google(ctx, keyword):
    '''
        bot command to search keyword on google
    '''
    # searching the keyword
    search_results = list(search(keyword, num=5, stop=5))
    if search_results:
        message = '\n'.join(search_results)
    else:
        message = f'No result found for "{keyword}"'

    # save search to DB
    with DataStorage() as storage_obj:
        storage_obj.save_keyword(ctx.author.id, keyword)

    await ctx.send(message)

@bot.command()
async def recent(ctx, keyword):
    '''
        bot command to find matched keyword from user's history
    '''
    with DataStorage() as storage_obj:
        results = storage_obj.get_matched_keywords(ctx.author.id, keyword)
        if results:
            message = '\n'.join([result[0] for result in results])
        else:
            message = f'No Matching data found for "{keyword}"'

    await ctx.send(message)

@bot.event
async def on_ready():
    '''
        Handles event when the bot is ready.
    '''
    print(f'{bot.user} logged in successfully')

@bot.event
async def on_message(message):
    '''
        Handles event when a new message pushed on the channel
    '''

    # ignoring message, if send by bot itself
    if message.author == bot.user:
        return

    # respond to hi
    if message.content.lower() == 'hi':
        await message.channel.send('hey')

    # processing custom commands
    await bot.process_commands(message)

def run_bot(token):
    '''
        method to start discord bot
    '''
    bot.run(token)
