from model import Igra, nova_igra, izbor_besed, nova_igra

import random

izbor_besed(7)

def pozeni_vmesnik():
    global igra
    igra = nova_igra()
    print(pozdrav(igra))
    while not igra.zmaga() and not igra.poraz():
        rezultat = zahtevaj_vnos(igra)
        print(izpis_igre(rezultat, igra))
    if igra.zmaga():
        print(izpis_zmage(igra))
        print('Upam, da ste v igri uživali :)')
        zakljucek()
    else:
        print(izpis_poraza(igra))
        zakljucek()

def izpis_igre(rezultat, igra):
    if rezultat == '+':
        return 'Izbor črke je bil pravilen. Pravilni del gesla sedaj izgleda tako {}.\nŽe uporabjene napačne črke pa so: {}\n'.format(igra.pravilni_del_gesla(), igra.nepravilni_ugibi()) + risanje(igra.stevilo_napak()) + '\n'
    elif rezultat == '-':
        return 'Izbor črke je bil napačen. Pravilni del gesla sedaj izgleda tako {}.\nŽe uporabjene napačne črke pa so: {}\n'.format(igra.pravilni_del_gesla(), igra.nepravilni_ugibi()) + risanje(igra.stevilo_napak()) + '\n'
    elif rezultat == 'o':
        return 'To črko ste že uporabili. Prosim izberite drugo.'
    else:
        return ''

def izpis_zmage(igra):
    return 'Čestitam! Zmagali ste! Rešitev je torej: {}.'.format(igra.geslo.upper())

def izpis_poraza(igra):
    return 'Žal vam tokrat ni uspelo. Več sreče prihodnjič. Pravilna rešitev je: {}'.format(igra.geslo.upper())

def zahtevaj_vnos(igra):
    crka = input('Prosim, ugibajte črko: ')
    if crka.isalpha() and len(crka) == 1:
        return igra.ugibaj(crka)
    else:
        if len(crka) != 1:
            print('Izberite eno samo črko!')
            return zahtevaj_vnos(igra)
        else:
            print('Izberite ČRKO!')
            return zahtevaj_vnos(igra)

def pozdrav(igra):
    return 'Lepo pozdravljeni! Upam, da ste dobro pripravljeni na igro. Beseda, ki jo ugibate, ima {} črk.'.format(len(igra.geslo))

def zakljucek():
    odgovor = input('Ali bi se želeli ponovno preizkusiti?\n1) Da\n2) Ne \n')
    if odgovor == '1':
        pozeni_vmesnik()
    elif odgovor == '2':
        pass
    else:
        print('Na vprašanje odgovorite tako, da pritisnete tipko 1 ali 2, nato pa prtitisnete enter.'.upper())
        return zakljucek()

def risanje(st_napak):
    if st_napak == 0:
        return ''
    elif st_napak == 1:
        return '\n\n\n\n\n________'
    elif st_napak == 2:
        return '\n |\n |\n |\n |\n_|______'
    elif st_napak == 3:
        return ' ______\n |\n |\n |\n |\n_|______'
    elif st_napak == 4:
        return ' ______\n |    |\n |\n |\n |\n_|______'
    elif st_napak == 5:
        return ' ______\n |    |\n |    o\n |\n |\n_|______'
    elif st_napak == 6:
        return ' ______\n |    |\n |    o\n |    |\n |\n_|______'
    elif st_napak == 7:
        return ' ______\n |    |\n |    o\n |   /|\n |\n_|______'
    elif st_napak == 8:
        return ' ______\n |    |\n |    o\n |   /|\\\n |\n_|______'
    elif st_napak == 9:
        return ' ______\n |    |\n |    o\n |   /|\\\n |   /\n_|______'
    else:
        return ' ______\n |    |\n |    o\n |   /|\\\n |   / \\\n_|______'

pozeni_vmesnik()