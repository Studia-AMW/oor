import threading
import time

class mójWątek(threading.Thread):
    
    def __init__(self, idWątku, nazwa, licznik):
        threading.Thread.__init__(self)
        self.idWątku = idWątku
        self.nazwa = nazwa
        self.licznik = licznik
        
    def run(self):
        print ("Uruchamianie wątku: " + self.nazwa)
        # Blokada w celu synchronizacji wątków
        threadLock.acquire()
        print_time(self.nazwa, self.licznik, 4)  # Ilość wykonań wątku
        # Zwolnienie blokady w celu uruchomienia kolejnego wątku
        threadLock.release()

def print_time(nazwaWątku, opóźnienie, licznik):
    while licznik:
        time.sleep(opóźnienie)
        print ("%s: %s" % (nazwaWątku, time.ctime(time.time())))
        licznik -= 1
threadLock = threading.Lock()
threads = []

# Utworzenie nowych wątków

wątek1 = mójWątek (1,"Wątek 1", 1)  # (id, nazwa, licznik==opóźnienie)

wątek2 = mójWątek (2,"Wątek 2", 2)

wątek3 = mójWątek (3,"Wątek 3", 3)

wątek4 = mójWątek (4,"Wątek 4", 4)

# Uruchomienie nowych wątków

wątek1.start()

wątek2.start()

wątek4.start()  # Wątek 4 zostanie uruchomiony przed wątkiem 3

wątek3.start()

# Dodawanie wątków do listy wątków

threads.append(wątek1)
threads.append(wątek2)
threads.append(wątek4)
threads.append(wątek3)

# Oczekiwanie na zakończenie wszystkich wątków

for t in threads:
    t.join()

print ("Kończenie wątku głównego")

