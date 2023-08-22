import poset

# index, name, children

quinze = poset.Poset(15, '1', [])
quatorze = poset.Poset(14, '1', [])
treize = poset.Poset(13, '1', [])
douze = poset.Poset(12, '1', [])
onze = poset.Poset(11, '1', [])
dix = poset.Poset(10, '2', [quinze])
neuf = poset.Poset(9, '2', [quatorze])
huit = poset.Poset(8, '2', [treize])
sept = poset.Poset(7, 'Lambda', [onze, douze])
six = poset.Poset(6, '5', [neuf, dix])
cinq = poset.Poset(5, '3', [huit])
quatre = poset.Poset(4, '4', [sept])
trois = poset.Poset(3, '6', [six])
deux = poset.Poset(2, '8', [quatre, cinq])
p4 = poset.Poset(1, '15', [deux, trois])