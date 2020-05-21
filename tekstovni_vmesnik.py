from model import Igra, nova_igra, izbor_besed, nova_igra

import random

izbor_besed(5)

def pozeni_vmesnik():
    global igra
    igra = nova_igra()
    print(pozdrav(igra))
    while not igra.zmaga() and not igra.poraz():
        zahtevaj_vnos(igra)
        print(izpis_igre(igra))
    if igra.zmaga():
        print(izpis_zmage())
    else:
        print(izpis_poraza(igra))

def izpis_igre(igra):
    return ('Vaše število napak je {stevilo_napak}; črke, ki ste jih že ugibali in so napačne so sledeče: {nepravilni_ugibi}.\n'
           'Pravilni del gesla sedaj izgleda tako {pravilni_del_gesla}'.format(stevilo_napak=igra.stevilo_napak(), nepravilni_ugibi=igra.nepravilni_ugibi(), pravilni_del_gesla=igra.pravilni_del_gesla()))

def izpis_zmage():
    return 'Čestitam! Zmagali ste!'   

def izpis_poraza(igra):
    return 'Ni vam uspelo. Več sreče prihodnjič. Pravilna resitev je {}'.format(igra.geslo)

def zahtevaj_vnos(igra):
    crka = input('Prosim, ugibajte crko ')
    if not crka.isalpha or len(crka) > 1:
        print('Prosim izberite črko! ')
    else:
        igra.ugibaj(crka)

def pozdrav(igra):
    return 'Lepo pozdravljeni! Upam, da ste dobro pripravljeni na igro. Beseda, ki jo ugibate, ima {} črk.'.format(len(igra.geslo))

pozeni_vmesnik()