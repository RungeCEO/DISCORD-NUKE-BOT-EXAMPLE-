from discord.ext import commands
import random




client = commands.Bot(command_prefix='?')

async def deletechannels(id):
    guild = client.get_guild(id=id)
    for channel in guild.channels:
        await channel.delete()
        print(f"[Channel deleted] {channel.name}")


async def createchannels(id, amount, name):
    letter = "ABCDEFGHIJKLMNOPQRZ1234567890"
    guild = client.get_guild(id=id)
    for num in range(amount):
        word = ""
        if name == "random":
            for n in range(random.randint(4, 10)):
                w = random.choice(letter)
                word += w
            await guild.create_text_channel(word)
            print(f"[Channel created] {word}")
        else:
            await guild.create_text_channel(name)
            print(f"[Channel created] {name}")

async def main():
    try:
        print("""
        ██████╗ ██╗   ██╗███╗   ██╗ ██████╗ ███████╗
        ██╔══██╗██║   ██║████╗  ██║██╔════╝ ██╔════╝
        ██████╔╝██║   ██║██╔██╗ ██║██║  ███╗█████╗  
        ██╔══██╗██║   ██║██║╚██╗██║██║   ██║██╔══╝  
        ██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝███████╗
        ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
    
        1: Delete all channels
        2: Create amount of channels
    
            """)
        wahl = input("choose:\n")
        if wahl == "1":
            i = input("Enter Guild Id: ")
            await deletechannels(int(i))
        if wahl == "2":
            i = input("Enter Guild Id: ")
            a = input("How much: ")
            n = input("Which name? Press Enter for random names: ")
            if not n:
                n = "random"
            await createchannels(int(i), int(a), n)
    except Exception:
        await main()


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')
    while True:
        await main()


client.run('token')
