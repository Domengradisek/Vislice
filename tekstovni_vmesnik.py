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
        zakljucek()
    else:
        print(izpis_poraza(igra))
        zakljucek()

def izpis_igre(rezultat, igra):
    if rezultat == '+':
        return 'Izbor črke je bil pravilen. Pravilni del gesla sedaj izgleda tako {}.\nŽe uporabjene napačne črke pa so: {}'.format(igra.pravilni_del_gesla(), igra.nepravilni_ugibi())
    elif rezultat == '-':
        return 'Izbor črke je bil napačen. Število napak, ki ste jih storili je {}. Pravilni del gesla sedaj izgleda tako {}.\nŽe uporabjene napačne črke pa so: {}'.format(igra.stevilo_napak(), igra.pravilni_del_gesla(), igra.nepravilni_ugibi())
    elif rezultat == 'o':
        return 'To črko ste že uporabili. Prosim izberite drugo.'
    else:
        return ''

def izpis_zmage(igra):
    return 'Čestitam! Zmagali ste! Rešitev je torej {}.'.format(igra.geslo)

def izpis_poraza(igra):
    return 'Ni vam uspelo. Več sreče prihodnjič. Pravilna rešitev je {}'.format(igra.geslo)

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
    print('Upam, da ste v igri uživali :)')
    odgovor = input('Ali bi se želeli ponovno preizkusiti?(Vtipkajte 1 ali 2)\n1) Da\n2) Ne \n')
    if odgovor == '1':
        pozeni_vmesnik()
    elif odgovor == '2':
        pass

pozeni_vmesnik()