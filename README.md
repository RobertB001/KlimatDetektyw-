# KlimaDetektyw

Bot na Discorda z AI, który rozpoznaje na zdjęciach rzeczy szkodzące klimatowi, podpowiada, gdzie wyrzucić śmieci, i pomaga z rzeczami nieoczywistymi.

## Typ projektu

Bot Discord, widzenie komputerowe (Teachable Machine), analiza tekstu (NLTK).

## Problem

Wiele rzeczy wokół nas po cichu przyczynia się do zmian klimatu: samochody, spalanie węgla, wycinanie lasów, hodowla zwierząt czy marnowanie prądu. Do tego ludzie często nie wiedzą, co zrobić z nietypowymi rzeczami.

## Rozwiązanie

KlimaDetektyw to bot na Discorda, który ma trzy funkcje:

1. Rozpoznawanie zdjęć - wrzucasz zdjęcie, a AI mówi, czy to szkodzi klimatowi, dlaczego i co zrobić lepiej.
2. Gdzie to wyrzucić? - bot mówi, do którego kosza wyrzucić daną rzecz, także te nieoczywiste.
3. Co się stanie, jeśli...? - bot odpowiada na pytania o skutki różnych sytuacji dla klimatu i przyrody.

Bot odpowiada uczciwie: jeśli coś jest mało szkodliwe, nie straszy, a jeśli jest szkodliwe, wyjaśnia dlaczego.

## Co rozpoznaje AI na zdjęciach

Pojazdy, Produkty, Energia, Przyroda.

Poziomy:
- Wysoki - duży wpływ na klimat
- Średni - umiarkowany wpływ
- Niski - mały wpływ, ale warto zmienić nawyk
- Dobry - pomaga klimatowi

## Jak to działa

Zdjęcia:
1. Użytkownik wysyła zdjęcie z komendą `!sprawdz`.
2. Bot pobiera zdjęcie i przekazuje je do modelu wytrenowanego w Teachable Machine.
3. Model zwraca nazwę rzeczy i pewność rozpoznania.
4. Bot odpisuje z wyjaśnieniem, poradą i poziomem szkodliwości.

Pytania tekstowe (`!gdzie`, `!cojesli`):
1. Bot dostaje pytanie od użytkownika.
2. NLTK dzieli pytanie na słowa i szuka słów kluczowych (np. "szampan", "ocean").
3. Bot znajduje pasującą odpowiedź w bazie wiedzy i ją wysyła.
4. Jeśli nie zna odpowiedzi, mówi to wprost.

## Uwaga

Zasady segregacji śmieci mogą się trochę różnić w zależności od gminy.

Oto typ mojego projektu:
> Bot Discord, widzenie komputerowe (Teachable Machine), analiza tekstu (NLTK)

## Biblioteki, których będę używać:
- [discord.py](https://discordpy.readthedocs.io/en/latest/intro.html) - obsługa bota na Discordzie
- [TensorFlow](https://www.tensorflow.org/) - wczytanie modelu i rozpoznawanie zdjęć
- [teachable-machine](https://pypi.org/project/teachable-machine/) - łatwe wczytanie modelu z Teachable Machine
- [Pillow](https://pillow.readthedocs.io/) - przygotowanie zdjęć dla modelu
- [NumPy](https://numpy.org/) - zamiana zdjęcia na liczby dla modelu
- [NLTK](https://www.nltk.org/) - dzielenie pytań na słowa
- [pystempel](https://pypi.org/project/pystempel/) - rozpoznawanie polskich odmian słów (np. szampana i szampan)

## Przydatne odniesienia:
- [botjack_discord_bot](https://github.com/qlero/botjack_discord_bot) - bot Discord, który rozpoznaje zdjęcia modelem AI
- [Image Classification Using Teachable Machine](https://github.com/c4codersworld/Image-Classification-Using-Teachable-Machine) - wczytanie modelu z Teachable Machine w Pythonie (stara wersja TensorFlow, tylko do inspiracji)
- [Waste Classification](https://github.com/aniass/Waste-Classification) - AI, które rozpoznaje, czy śmieć nadaje się do recyklingu
- [trash-classification](https://github.com/wayofell/trash-classification) - AI, które dzieli śmieci na 10 kategorii
- [discord.py na GitHubie](https://github.com/Rapptz/discord.py) - oficjalne repo z przykładami botów
- [Garbage Classification (Kaggle)](https://www.kaggle.com/datasets/mostafaabla/garbage-classification) - gotowe zdjęcia śmieci do trenowania modelu

## Artykuły przewodniki, które pomogą mi podczas programowania
Jak zrobić pierwszego bota na Discordzie krok po kroku: [discord.py Quickstart](https://discordpy.readthedocs.io/en/latest/quickstart.html)

Jak wytrenować model rozpoznawania zdjęć bez pisania kodu: [Teachable Machine](https://teachablemachine.withgoogle.com/)

Jak używać polskiego stemmera w Pythonie: [pystempel](https://github.com/dzieciou/pystempel/)

Oficjalne zasady segregacji odpadów w Polsce: [Nasze śmieci](http://naszesmieci.mos.gov.pl/)

Gdzie wyrzucić nietypowe odpady, np. styropian albo płyty CD: [Jak segregować śmieci](https://rynekpierwotny.pl/wiadomosci-mieszkaniowe/jak-segregowac-smieci/10949/)

Skąd biorą się zmiany klimatu: [Przyczyny zmian klimatu - Komisja Europejska](https://climate.ec.europa.eu/climate-change/causes-climate-change_pl)

## Autor

Robert
