import poset

# index, name, children

quinze = poset.Poset(15, '1', [])
quatorze = poset.Poset(14, '1', [])
treize = poset.Poset(13, '1', [])
douze = poset.Poset(12, '1', [])
onze = poset.Poset(11, '1', [])
dix = poset.Poset(10, 'Lambda', [quatorze, quinze])
neuf = poset.Poset(9, '2', [treize])
huit = poset.Poset(8, '2', [douze])
sept = poset.Poset(7, '2', [onze])
six = poset.Poset(6, '4', [dix])
cinq = poset.Poset(5, '3', [neuf])
quatre = poset.Poset(4, '5', [sept, huit])
trois = poset.Poset(3, 'lambda', [six])
deux = poset.Poset(2, '9', [quatre, cinq])
p3 = poset.Poset(1, '15', [deux, trois])