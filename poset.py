class Poset(object):
    def __init__(self, index, name, children):
        self.index = index
        self.name = name  # Differs from name and value to facilitate counting
        self.children = children
        self.value = 1 + sum(c.value for c in children)

    def get_line(self):
        """c'est crade mais ca devrait marcher :)"""
        if self.index == 1:
            return 5
        elif self.index in (2, 3):
            return 4
        elif self.index in (4, 5, 6):
            return 3
        elif self.index in (7, 8, 9, 10):
            return 2
        else:
            return 1

    def contains(self, other):
        if other in self.children or other == self:
            return True
        elif self.get_line() <= other.get_line():
            return False
        else:
            return any(c.contains(other) for c in self.children)

    def contains_or_is_contained(self, other):
        """toujours plus crade yay"""
        return self.contains(other) or other.contains(self)

    def __str__(self):
        for c in self.children:
            print(c)
        return (f'index: {self.index}, name: {self.name}, value: {self.value},'
                f' children: {[c.index for c in self.children]}')

    def get_value_unique(self):
        """de pire en pire"""
        try:
            x = int(self.name)
            return x
        except:
            pass
        if self.name == "Lambda":
            return 3.5
        if self.name == "lambda":
            return 4.5
        if self.name == "cap":
            return 7.5

    def __lt__(self, other):
        return self.get_value_unique() > other.get_value_unique()

    def get_all_subposets(self):
        subposets = [self]
        for c in self.children:
            subposets += c.get_all_subposets()
        return subposets

