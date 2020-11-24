# Implementirajte strukturu podataka sličnu skupu, ali koja dozvoljava duplikate i koja
# će se zvati Multiset. Ta struktura podataka treba podržavati sljedeće operacije za
# skupove: provjera pripadnosti elementa, unija, presjek, razlika i jednakost. Dva multiseta su jednaka ako imaju isti broj svakog elementa. Nakon implementacije ove
# strukture podataka iskoristite je za rješenje zadatka 24. Ovaj zadatak riješite na dva
# načina:
# (a) Kao samostalna klasa.
# (b) Kao klasa koja je izvedena (nasljeđuje) od ugrađenog tipa set.

¸
class Multiset:
    def __init__(self, *elements):
        self.array = []
        for element in elements:
            self.array.append(element)

    def add(self, elem):
        self.array.append(elem)

    def contains(self, elem):
        return elem in self.array

    def union(self, multiset_object):
        new_array = self.array + multiset_object.array
        union_multiset = Multiset()
        for elem in new_array:
            union_multiset.add(elem)
        return union_multiset

    def intersection(self, multiset_object):
        intersection_array = []
        tmp_array = multiset_object.array.copy()
        for elem in self.array:
            if elem in tmp_array:
                tmp_array.remove(elem)
                intersection_array.append(elem)
        intersection_multiset = Multiset()
        for elem in intersection_array:
            intersection_multiset.add(elem)
        return intersection_multiset

    def difference(self, multiset_object):
        tmp_array = self.array.copy()
        for elem in multiset_object.array:
            if elem in tmp_array:
                tmp_array.remove(elem)
        difference_multiset = Multiset()
        for elem in tmp_array:
            difference_multiset.add(elem) 
        return difference_multiset

    def equals(self, multiset_object):
        multiset_difference = self.difference(multiset_object)
        return len(multiset_difference.array) == 0


if __name__ == '__main__':
    multiset1 = Multiset(2, 5, 5)
    multiset2 = Multiset(2, 3, 5)
    ms = multiset1.intersection(multiset2);
    print(ms.array)
