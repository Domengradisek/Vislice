STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
NAPACNA_CRKA = '-'
PONOVLJENA_CRKA = 'o'
ZMAGA = 'w'
PORAZ = 'x'

class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke

    def pravilne_crke(self):
        seznam = []
        for crka in self.crke:
            if crka in self.geslo:
                seznam.append(crka)
        return seznam

    def napacne_crke(self):
        seznam = []
        for crka in self.crke:
            if not crka in self.geslo:
                seznam.append(crka)
        return seznam

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if crka not in self.crke:
                return False
        return True

    def poraz(self):
        if self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK:
            return True
        else:
            return False

    def pravilni_del_gesla(self):
        niz = ''
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                niz += crka
            else:
                niz += '_'
        return niz

    def nepravilni_ugibi(self):
        niz = ''
        for crka in self.napacne_crke():
            niz += crka + ' '
        niz = niz[::-1]
        niz = niz[1:]
        niz = niz[::-1]
        return niz

    def ugibaj(self, crka):
        crka = crka.upper()
        if crka in self.napacne_crke() or crka in self.pravilne_crke():
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            elif crka in self.geslo:
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA

bazen_besed = []

def izbor_besed(n, a, b):
    seznam = []
    with open('besede.txt', encoding='utf-8') as besede:
        for beseda in besede:
            beseda = beseda[::-1]
            beseda = beseda[1:]
            beseda = beseda[::-1]
            if len(beseda) == n and beseda[0] == a and beseda[-1] == b:
                seznam.append(beseda)
    global bazen_besed
    bazen_besed = seznam

import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    crke = []
    return Igra(geslo, crke)
