# halmaz létrehozása
reggeli = {'tea', 'vaj', 'piritós'}
    
    # üres halmaz létrehozása
    # ebed = {}  <- SZÓTÁRT hoz létre!!!
ebed = set()

    # bejárható gyűjteményből, pl. listából
ebed = set(['halászlé', 'kenyér', True])
print(ebed)
    # egy elem hozzáadása
reggeli.add('lekvár')

    # egy nem meghatározott elem eltávolítása
reggeli.pop()
    
    # egy bizonyos elem eltávolítása
    # ha nincs ilyen elem, akkor hibát eredményez
reggeli.remove('sajt')

    # egy bizonyos elem eltávolítása
    # ha nincs ilyen elem, nem eredményez hibát
reggeli.discard('sajt')
reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
ebed = {'víz', 'halászlé', 'kenyér'}

    # metszet
print(reggeli & ebed)
    # unio
print(reggeli | ebed)
    # különbség
print(reggeli - ebed)
    # csak az egyikben, vagy csak a másikban
print(reggeli ^ ebed)


# üres szótár létrehozása
raktar = {}
print(raktar)

    # szótár létrehozása adatokkal 
diak = {
	    'vezeteknev': 'Kiss',
	    'keresztnev': 'Péter',
	    'eletkor': 17,
	    'menza': True
}
# szótár elemeinek elérése kulcs alapján
print(diak['eletkor'])
print(diak.get('eletkor'))

    # nem létező kulcsra való hivatkozás -> KeyError
    # print(diak['osztaly'])

    # nem létező kulcsra hivatkozunk a .get metódussal, 
    # ilyenkor a megadott alapértékkel tér vissza
print(diak.get('kollegista', 'nem'))

    # ellenőrzés, hogy létezik-e a kulcs
print('keresztnev' in diak)
# érték módosítása
diak['eletkor'] = 21
    print(diak['eletkor'])

    # még nem létező kulcs megadása értékkel
diak['osztaly'] = '10.A'

    # kulcs-érték törlése
del diak['vezeteknev']
for kulcs in diak:
	    print(kulcs, diak[kulcs])

    for ertek in diak.values():
        print(ertek)

    for kulcs, ertek in diak.items():
        print(kulcs, ertek)