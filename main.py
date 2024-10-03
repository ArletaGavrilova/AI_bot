import discord
from model import get_class
from discord.ext import commands
from random import randint

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:

            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"images/{file_name}")
            await ctx.send(f"Сохранили картинку в images/{file_name}")
            await ctx.send(get_class(model_path="keras_model.h5", labels_path="labels_txt", image_path=f"images/{file_name}"))
    else:
        await ctx.send('Вы забыли загрузить кртинку.')




bot.run("")