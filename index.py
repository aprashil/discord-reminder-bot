from discord.ext import commands
from discord.ext import tasks
from datetime import datetime
import discord
import json
import os


class var:
    def __init__(self):
        with open('config.json') as configObj:
            config = json.load(configObj)

        self.prefix = config['prefix']
        self.token = config['token']
        self.color = eval(config['colorHEX'])
        self.channel = config['channelID']
        self.tts = config['tts']

        self.antiRepeat = ''
        self.fetchEvents()

    def fetchEvents(self):
        with open('events.json') as eventsObj:
            self.events = json.load(eventsObj)

    def attainTime(self):
        return datetime.now().strftime('%H:%M')

    def attainSched(self):
        day = datetime.now().strftime('%A')
        return self.events[day]

    def attainLastMod(self):
        LMFloat = os.path.getmtime('events.json')
        return datetime.fromtimestamp(LMFloat).strftime('%H:%M')


var = var()

bot = commands.Bot(command_prefix=var.prefix)
bot.remove_command('help')


@bot.event
async def on_ready():
    print(f"Successfully logged in as {bot.user}!")
    print(f"Current local time: {datetime.now()}")
    reminder.start()


@tasks.loop(seconds=30)
async def reminder():
    var.fetchEvents()
    current_time = var.attainTime()

    if var.antiRepeat != current_time:

        sched = var.attainSched()
        currEvent = [sched[i] for i in sched if i == current_time]

        if currEvent:
            reminder_channel = bot.get_channel(var.channel)

            parameters = {
                "title": currEvent[0][0],
                "description": currEvent[0][1],
                "color": var.color
            }

            embed = discord.Embed(**parameters)
            await reminder_channel.send(embed=embed)

            if var.tts:
                await reminder_channel.send(currEvent[0][1], tts=var.tts)

    var.antiRepeat = current_time

bot.run(var.token)
