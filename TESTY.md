# Lista kontrolna testów - KlimaDetektyw

## Cele testowania
Sprawdzić, czy bot poprawnie rozpoznaje zdjęcia, odpowiada na wszystkie komendy, działa szybko i jest bezpieczny.

## Funkcjonalność

| Zadanie | Oczekiwany wynik | Priorytet |
|---|---|---|
| Wpisz !pomoc | Bot pokazuje listę komend | Wysoki |
| Wyślij zdjęcie auta z !sprawdz | Bot rozpoznaje samochód i daje poradę | Wysoki |
| Wpisz !sprawdz bez zdjęcia | Bot prosi o dodanie zdjęcia | Średni |
| Wyślij plik .txt z !sprawdz | Bot mówi, że to nie jest zdjęcie | Średni |
| Wpisz !gdzie paragon | Bot mówi, że do zmieszanych | Wysoki |
| Wpisz !gdzie PARAGON (wielkie litery) | Bot odpowiada tak samo jak dla małych liter | Średni |
| Wpisz !gdzie kamień | Bot mówi, że jeszcze nie wie | Średni |
| Wpisz samo !gdzie (bez rzeczy) | Bot prosi, żeby wpisać rzecz | Średni |
| Wpisz !cojesli wleję szampana do oceanu | Bot odpowiada o szampanie | Wysoki |

## Model AI

| Zadanie | Oczekiwany wynik | Priorytet |
|---|---|---|
| Wyślij nowe zdjęcie z każdej z 5 klas | Bot rozpoznaje każdą klasę poprawnie | Wysoki |
| Wyślij zdjęcie spoza klas (np. kota) | Bot mówi, że nie jest pewien | Średni |
| Wyślij ciemne albo rozmazane zdjęcie | Bot dalej rozpoznaje albo mówi, że nie jest pewien | Niski |

## Interfejs

| Zadanie | Oczekiwany wynik | Priorytet |
|---|---|---|
| Sprawdź odpowiedzi bota | Polskie znaki (ą, ę, ó) wyświetlają się dobrze | Średni |
| Sprawdź nazwy rozpoznanych rzeczy | Bot pisze np. "Pudełko po pizzy", a nie "pudelko_po_pizzy" | Niski |

## Wydajność

| Zadanie | Oczekiwany wynik | Priorytet |
|---|---|---|
| Zmierz czas odpowiedzi na !sprawdz | Bot odpowiada w mniej niż 5 sekund | Średni |
| Wyślij 5 zdjęć pod rząd | Bot odpowiada na wszystkie i się nie zawiesza | Niski |

## Bezpieczeństwo

| Zadanie | Oczekiwany wynik | Priorytet |
|---|---|---|
| Sprawdź kod na GitHubie | Tokena nie ma nigdzie w kodzie | Wysoki |
| Sprawdź uprawnienia bota | Bot ma tylko potrzebne uprawnienia | Średni |

## Kolejność testowania
1. Najpierw wszystkie zadania z priorytetem Wysoki
2. Potem Średni
3. Na końcu Niski
## Wyniki testów
Wszystkie testy zaliczone.
