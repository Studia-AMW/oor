# -*- coding: utf-8 -*-
import multiprocessing
import time

dane = (['bardzo szybki ', '2'], ['szybki        ', '4'], ['wolny         ', '6'], ['bardzo wolny  ', '8'], # tej samej długości nazwy procesów, by wydruk był czytelniejszy (dodane spacje)
        ['najszybszy    ', '1'], ['niezbyt szybki', '3'], ['trochę wolny  ', '5'], ['dość wolny    ', '7']
)


def oczyt_wieloprocesowy(procesy):
    for indane in procesy:          # pętla uruchamiająca kolejne procesy z tablicy
        p = multiprocessing.Process(target=wydruk_wieloprocesowy, args=(indane[0], indane[1]))
        p.start()




def wydruk_wieloprocesowy(nazwa_procesu, czas_oczekiwania):
    print (" Proces %s\t czeka %s sekund" % (nazwa_procesu, czas_oczekiwania))
    time.sleep(int(czas_oczekiwania))                  # oczekuje określony w tablicy czas
    print (" Proces %s\t WYKONANY" % nazwa_procesu)    # informacja o wykonanych procesach

if __name__ == '__main__':
    oczyt_wieloprocesowy(dane)
