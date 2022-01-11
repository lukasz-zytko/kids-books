# kids-books - biblioteka książek mojego dziecka
Aplikacja umożliwia następujące funkcje:
* prezentacja listy książek z pliku JSON
* dodwanie nowych książek
* edycję książek w pliku

# RESTowe API aplikacji
Zasoby aplikacji będą obsługiwane przy pomocy następujących metod HTTP i końcówek
* Metoda HTTP > URl > Akcja:
- GET > http://[hostname]/api/v1/books/ > Pobieranie listy books
- GET > http://[hostname]/api/v1/books/[book_id] > Pobiernie konkretnej book
- POST > http://[hostname]/api/v1/books/ > Utworzenie nowego book
- PUT > http://[hostname]/api/v1/books/[book_id] > Edycja isniejącego book
- DELETE > http://[hostname]/api/v1/books/[book_id] > Usuwanie istniejącego book

# Instalacja
Zależoności wykorystane w aplikacji znajdują się w pliku requirements.txt
Do instalacji zależności wystarczy wykonać komendę:
* pip install -r requirements.txt