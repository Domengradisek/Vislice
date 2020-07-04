STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
NAPACNA_CRKA = '-'
PONOVLJENA_CRKA = 'o'
ZMAGA = 'w'
PORAZ = 'x'
ZACETEK = 'z'

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
        if self.stevilo_napak() >= 10:
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

def izbor_besed(n):
    seznam = []
    with open('besede.txt', encoding='utf-8') as besede:
        for beseda in besede:
            beseda = beseda[::-1]
            beseda = beseda[1:]
            beseda = beseda[::-1]
            if len(beseda) == n:
                seznam.append(beseda)
    global bazen_besed
    bazen_besed = seznam

import random

def nova_igra():
    geslo = random.choice(bazen_besed)
    crke = []
    return Igra(geslo, crke)

class Vislice:

    def __init__(self, igre):
        self.igre = {}

    def prost_id_igre(self):
        n = 1
        if self.igre == {}:
            return 0
        else:
            while n in self.igre:
                n = n + 1
            return n

    def nova_igra(self):
        n = self.prost_id_igre()
        geslo = random.choice(bazen_besed)
        crke = []
        self.igre[n] = (Igra(geslo, crke), ZACETEK)
        nova_igra()
        return n

    def ugibaj(self, id_igre, crka):
        ustrezna_igra = self.igre[id_igre][0]
        stanje = ustrezna_igra.ugibaj(crka)
        self.igre[id_igre] = (ustrezna_igra, stanje)