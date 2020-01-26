import discord
from discord.ext import commands
from random import randint
from datetime import datetime, timezone
import time

client = commands.Bot(command_prefix='!')
dic = {
    'Skeleton King': ['00:00', '02:00', '04:00', '06:00', '08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00'],
    'Event Drop Arcania': ['19:50']
}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def time(ctx):
    await ctx.send(datetime.now(timezone.utc).astimezone())
 
@client.command()
async def start(ctx):
    await ctx.send('Начал мониторить ивенты')

    while True:
        time_now = datetime.now(timezone.utc).astimezone()
        time_now = time_now.strftime('%H:%M')
        for i in dic['Skeleton King']:
            if i == time_now:
                await ctx.send('Skeleton King через 10 минут')
            else:
                continue
        for i in dic['Event Drop Arcania']:
            if i == time_now:
                await ctx.send('Event drop Arcania через 10 минут')
            else:
                continue

        time.sleep(60)









client.run('NjcwMDAyMzgwMjUwODA4Mzgx.XioCrw.90Nghmo-FcqpIje9LRuQhoU-qzo')
