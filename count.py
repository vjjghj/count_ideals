from poset import Poset
from itertools import combinations
from collections import defaultdict


def name_posets(posets):
    return '-'.join((x.name for x in sorted(posets)))


def count(poset, i, j):
    """
    :param i: size of the ideal
    :param j: number of maximal elements
    :return:
    """
    results = defaultdict(lambda : 0)
    for ideals in combinations(poset.get_all_subposets(), j):
        if any(x.contains_or_is_contained(y) for x, y in combinations(ideals, 2)):
            continue
        if sum(p.value for p in ideals) == i:
           results[str(name_posets(ideals))] += 1
    return results.items(), sum(results.values())

