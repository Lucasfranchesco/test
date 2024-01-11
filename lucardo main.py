import discord
from discord.ext import commands
import random
import os
import requests

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


ideas_ecologicas = ["Utiliza el transporte público. Nos hemos acostumbrado a utilizar el coche para todo, pero es hora de pensar en el planeta y en nuestro futuro y de usar medios de transporte más sostenibles y respetuosos con el medioambiente. El transporte público es una buena solución, más barata y menos contaminante que el coche."
                    ,"Reduce, reutiliza y recicla: Minimiza tu consumo de productos desechables y trata de reutilizar o reciclar tanto como sea posible. (para dejarlo simple)"
                    ,"Recoger, separar y eliminar los residuos de forma segura para proteger la tierra y el agua, fomentar la reducción de sustancias nocivas para el medio ambiente y fomentar el reciclaje por parte de los ciudadanos y las empresas."
                    ,"Educación y concienciación: Comparte información sobre la importancia de cuidar el medio ambiente con amigos, familiares para crear conciencia sobre la importancia de la sostenibilidad"]



@bot.command(description='For when you wanna settle the score some other way')
async def consejo_ecologico(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(ideas_ecologicas))
    

bot.run("token")
