# -*- coding: utf-8 -*-
import time
import multiprocessing

def ciąg_fibannaciego(n):
    if n < 0:       # nie można obliczyć ciągu Fibannaciego dla liczb ujemnych
        raise ValueError
    if n < 2:
        return n
    return ciąg_fibannaciego(n-1)+ciąg_fibannaciego(n-2)    #rekurencyjne wywołanie funkcji

def fibonacci(do_kolejki, z_kolejki):
    while True:
        n = do_kolejki.get()
        if n == None: 
            break
        czas_rozpoczęcia = time.time()      # czas rozpoczęcia obliczania ciągu
        wynik = ciąg_fibannaciego(n)        # wynik ciągy
        czas_zakończenia = time.time()      # czas zakończenia obliczania ciągu

        z_kolejki.put((n, wynik, czas_zakończenia-czas_rozpoczęcia))
    z_kolejki.put((None, None, None))

def main():
    czas_rozpoczęcia = time.time()
    do_kolejki = multiprocessing.Queue()
    z_kolejki = multiprocessing.Queue()

    numer_procesu = multiprocessing.cpu_count()

    for _ in range(numer_procesu):
        multiprocessing.Process(target=fibonacci, 
                                args=(do_kolejki, z_kolejki)).start()

    for i in range(28, 36):     # Obliczanie ciągu Fibannaciego dla kolejnych liczb w zakresie 28-35
        do_kolejki.put(i)

    for _ in range(numer_procesu):
        do_kolejki.put(None)

    while True:

        n, wynik, czas_wyliczenia = z_kolejki.get()
        if n == None: 
            numer_procesu -= 1
            if numer_procesu == 0: break
        else:
            print ("Ciąg Fibannaciego z liczby: %3d = %7d   wyliczenie zajęło: %0.3fs" % ( n, wynik, czas_wyliczenia))

    czas_zakończenia = time.time()
    print ("Całkowity czas obliczeń: %0.3fs" % (czas_zakończenia - czas_rozpoczęcia))

if __name__ == "__main__":
    main()
