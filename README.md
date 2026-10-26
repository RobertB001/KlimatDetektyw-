# KlimaDetektyw

Bot na Discorda z AI, który rozpoznaje na zdjęciach rzeczy szkodzące klimatowi, podpowiada, gdzie wyrzucić śmieci, i pomaga z rzeczami nieoczywistymi.


## Problem

Wiele rzeczy wokół nas po cichu przyczynia się do zmian klimatu: samochody, spalanie węgla, wycinanie lasów, hodowla zwierząt czy marnowanie prądu. Do tego ludzie często nie wiedzą, co zrobić z nietypowymi rzeczami.

## Rozwiązanie

KlimaDetektyw to bot na Discorda, który ma trzy funkcje:

1. Rozpoznawanie zdjęć** - wrzucasz zdjęcie, a AI mówi, czy to szkodzi klimatowi, dlaczego i co zrobić lepiej.
2. Gdzie to wyrzucić?** - bot mówi, do którego kosza wyrzucić daną rzecz, także te nieoczywiste.
3. Co się stanie, jeśli...? - bot odpowiada na pytania o skutki różnych sytuacji dla klimatu i przyrody.

Bot odpowiada uczciwie: jeśli coś jest mało szkodliwe, nie straszy, a jeśli jest szkodliwe, wyjaśnia dlaczego.

## Co rozpoznaje AI na zdjęciach
Pojazdy, Produkty,  Energia,  Przyroda.


Poziomy:
- **Wysoki** - duży wpływ na klimat
- **Średni** - umiarkowany wpływ
- **Niski** - mały wpływ, ale warto zmienić nawyk
- **Dobry** - pomaga klimatowi


## Jak to działa

Zdjęcia
1. Użytkownik wysyła zdjęcie z komendą `!sprawdz`.
2. Bot pobiera zdjęcie i przekazuje je do modelu wytrenowanego w Teachable Machine.
3. Model zwraca nazwę rzeczy i pewność rozpoznania.
4. Bot odpisuje z wyjaśnieniem, poradą i poziomem szkodliwości.

**Pytania tekstowe (`!gdzie`, `!co jesli`):
1. Bot dostaje pytanie od użytkownika.
2. NLTK dzieli pytanie na słowa i szuka słów kluczowych (np. "szampan", "ocean").
3. Bot znajduje pasującą odpowiedź w bazie wiedzy i ją wysyła.
4. Jeśli nie zna odpowiedzi, mówi to wprost.


## Uwaga

Zasady segregacji śmieci mogą się trochę różnić w zależności od gminy.


## Autor

Robert
