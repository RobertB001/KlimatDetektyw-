import io
import os

import discord
import numpy as np
import tf_keras
from discord.ext import commands
from PIL import Image, ImageOps
from tf_keras.layers import DepthwiseConv2D

from baza_wiedzy import GDZIE_WYRZUCIC, CO_JESLI, PORADY


class NaprawionyDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, *args, groups=None, **kwargs):
        super().__init__(*args, **kwargs)


model = tf_keras.models.load_model(
    "keras_model.h5",
    compile=False,
    custom_objects={"DepthwiseConv2D": NaprawionyDepthwiseConv2D},
)

with open("labels.txt", "r", encoding="utf-8") as plik:
    KLASY = [linia.strip().split(" ", 1)[1] for linia in plik if linia.strip()]


def rozpoznaj(obraz):
    obraz = obraz.convert("RGB")
    obraz = ImageOps.fit(obraz, (224, 224), Image.Resampling.LANCZOS)
    tablica = np.asarray(obraz).astype(np.float32)
    tablica = (tablica / 127.5) - 1
    dane = np.expand_dims(tablica, axis=0)
    wynik = model.predict(dane, verbose=0)[0]
    indeks = int(np.argmax(wynik))
    return KLASY[indeks], float(wynik[indeks])


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

    zalacznik = ctx.message.attachments[0]
    if not zalacznik.content_type or not zalacznik.content_type.startswith("image/"):
        await ctx.send("To nie jest zdjęcie. Wyślij plik JPG albo PNG.")
        return

    dane = await zalacznik.read()
    obraz = Image.open(io.BytesIO(dane))
    klasa, pewnosc = rozpoznaj(obraz)

    if pewnosc < 0.6:
        await ctx.send("Nie jestem pewien, co jest na tym zdjęciu. Spróbuj innego.")
        return

    info = PORADY.get(klasa)
    if info is None:
        await ctx.send(f"Rozpoznałem: {klasa} ({pewnosc:.0%}), ale nie mam jeszcze o tym porady.")
        return

    await ctx.send(
        f"Rozpoznałem: {info['nazwa']} ({pewnosc:.0%})\n"
        f"Wpływ na klimat: {info['poziom']}\n"
        f"Dlaczego: {info['dlaczego']}\n"
        f"Porada: {info['porada']}"
    )


@bot.command()
async def gdzie(ctx, *, rzecz: str = None):
    if not rzecz:
        await ctx.send("Napisz, co chcesz wyrzucić, np. !gdzie paragon")
        return

    odpowiedz = GDZIE_WYRZUCIC.get(rzecz.strip().lower())
    if odpowiedz:
        await ctx.send(odpowiedz)
    else:
        await ctx.send("Jeszcze nie wiem, gdzie to wyrzucić.")


@bot.command()
async def cojesli(ctx, *, pytanie: str = None):
    if not pytanie:
        await ctx.send("Napisz sytuację, np. !cojesli wleję szampana do oceanu")
        return

   
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
    bot.run(os.environ["token"])
