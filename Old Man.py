import discord

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    
@client.event
async def on_message(message):
    if message.author.bot:
        return
    await message.channel.send("GET OF MY LAWN!!!!")

client.run('TOKEN')
