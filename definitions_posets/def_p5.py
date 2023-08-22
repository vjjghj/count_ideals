import poset

# index, name, children

quinze = poset.Poset(15, '1', [])
quatorze = poset.Poset(14, '1', [])
treize = poset.Poset(13, '1', [])
douze = poset.Poset(12, '1', [])
onze = poset.Poset(11, '1', [])
dix = poset.Poset(10, '2', [quinze])
neuf = poset.Poset(9, 'Lambda', [treize, quatorze])
huit = poset.Poset(8, '2', [douze])
sept = poset.Poset(7, '2', [onze])
six = poset.Poset(6, '6', [neuf, dix])
cinq = poset.Poset(5, '3', [huit])
quatre = poset.Poset(4, '3', [sept])
trois = poset.Poset(3, '7', [six])
deux = poset.Poset(2, 'cap', [quatre, cinq])
p5 = poset.Poset(1, '15', [deux, trois])