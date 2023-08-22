from definitions_posets.def_p2 import p2
import count
from itertools import combinations

def sum_dict(d):
    return sum(d.values())

if __name__ == '__main__':
    for j in range(1, 6):
        for i in range(1, 16):
            print(i, j, count.count(p2, i, j))
