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
six = poset.Poset(6, '3', [dix])
cinq = poset.Poset(5, 'lambda', [neuf])
quatre = poset.Poset(4, '5', [sept, huit])
trois = poset.Poset(3, '4', [six])
deux = poset.Poset(2, '10', [quatre, cinq])
p2 = poset.Poset(1, '15', [deux, trois])