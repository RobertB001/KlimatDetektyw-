%%writefile main.py
import os

import discord
from discord.ext import commands

from baza_wiedzy import GDZIE_WYRZUCIC, CO_JESLI

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Zalogowano jako {bot.user}")


@bot.command()
async def sprawdz(ctx):
    if not ctx.message.attachments:
        await ctx.send("Dodaj zdjęcie do komendy !sprawdz.")
        return
   
    await ctx.send("Mam zdjęcie! Rozpoznawanie będzie gotowe w następnej wersji.")


@bot.command()
async def gdzie(ctx, *, rzecz: str):
    odpowiedz = GDZIE_WYRZUCIC.get(rzecz.lower())
    if odpowiedz:
        await ctx.send(odpowiedz)
    else:
        await ctx.send("Jeszcze nie wiem, gdzie to wyrzucić.")


@bot.command()
async def cojesli(ctx, *, pytanie: str):
    
    for slowo, odpowiedz in CO_JESLI.items():
        if slowo in pytanie.lower():
            await ctx.send(odpowiedz)
            return
    await ctx.send("Jeszcze nie znam odpowiedzi na to pytanie.")


@bot.command()
async def pomoc(ctx):
    await ctx.send(
        "Komendy:\n"
        "!sprawdz + zdjęcie - sprawdzam, czy to szkodzi klimatowi\n"
        "!gdzie <rzecz> - mówię, gdzie to wyrzucić\n"
        "!cojesli <sytuacja> - mówię, co się stanie"
    )


if __name__ == "__main__":
    bot.run(os.environ["DISCORD_TOKEN"])
