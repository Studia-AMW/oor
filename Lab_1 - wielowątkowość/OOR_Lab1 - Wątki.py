# -*- coding: utf-8 -*-
import time
import datetime
import threading

def licz(x):
    time.sleep(x)
    return x * x

# dodajemy stempelek czasowy do komunikatu

def log(message):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    print ("%s %s" % (now, message))



class UruchomWątek(threading.Thread):
    def __init__(self, value):
        threading.Thread.__init__(self)
        self.value = value
    def run(self):
        result = licz(self.value)
        log("Watek z parametrem %s -> wykonuje sie %s sekund" % (self.value, result))

def main():

# Każde zadanie podniesienia parametru wątku do potęgi 2 zostanie wykonane w osobnym wątku i będzie się wykonywać przez
# liczbę sekund będącą wynikiem obliczeń dzięki czemu wątki o niższym parametrze skończą działanie szybciej (a nie w kolejności uruchomienia)

    log("Wątek główny (wykona się najszybciej, bo nie ma opóźnienia)")

    UruchomWątek(3).start()      # Wątek z parametrem: 3

    UruchomWątek(4).start()      # Wątek z parametrem: 4

    UruchomWątek(0.5).start()    # Wątek z parametrem: 0.5

    UruchomWątek(1).start()      # Wątek z parametrem: 1

    log("Zakończenie działania watku głownego")

if __name__ == "__main__":
    main()