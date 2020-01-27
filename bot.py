import discord
from discord.ext import commands
from random import randint
from datetime import datetime, timezone
import time
import os

client = commands.Bot(command_prefix='!')
dic = {
    'Skeleton King': ['00:00', '02:00', '04:00', '06:00', '08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00', '22:00'],
    'Event Drop Arcania': ['19:50']
}


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.command()
async def start(ctx):
    await ctx.send('Начал мониторить ивенты')

    while True:
        time_now = datetime.now(timezone.utc).astimezone()
        time_now = time_now + timedelta(hours=3)
        time_now = time_now.strftime('%H:%M')
        for i in dic['Skeleton King']:
            if i == time_now:
                await ctx.send(f'Skeleton King через 10 минут {time_now}')
            else:
                continue
        for i in dic['Event Drop Arcania']:
            if i == time_now:
                await ctx.send(f'Event drop Arcania через 10 минут {time_now}')
            else:
                continue

        time.sleep(60)



token = os.environ.get('BOT_TOKEN')
client.run(str(token))





