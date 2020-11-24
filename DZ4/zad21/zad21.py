# Napišite funkciju slijedi2 tako da riješite zadatak 20 s pretpostavkom da jedna osoba
# može biti povezana s više drugih osoba (i dalje nema kružnih veza). Funkciju slijedi2
# napišite upotrebom rekurzije. Nadalje, neka funkcija vrati listu svih parova osoba
# preko kojih su druge dvije osobe povezane:
# >>> podaci4 = [
#   ('zoran', 'ana'),
#   ('ivo', 'mara'),
#   ('pero', 'ana'),
#   ('ivo', 'sanja'),
#   ('mara', 'sara'),
#   ('ana', 'marko'),
#   ('sara', 'zoran'),
#   ('sara', 'pero'),
#   ('sara', 'marko')]
#
# >>> slijedi2(podaci4 , 'ivo', 'marko')
#
# [
#       ('ivo', 'mara'),
#       ('mara', 'sara'),
#       ('sara', 'zoran'),
#       ('zoran', 'ana'),
#       ('ana', 'marko')
# ]


def recursion(children, parent, search_link, traversed_links):
    if parent == search_link:
        return True
    for child in children[parent]:
        traversed_links.append(parent)
        if child not in traversed_links and recursion(children, child, search_link, traversed_links):
            return traversed_links + [search_link]
        traversed_links.remove(parent)
    return False


def are_links_connected(relations, link1, link2):
    children = {}
    for relation in relations:
        children.setdefault(relation[0], []).append(relation[1])
        children.setdefault(relation[1], []).append(relation[0])
    res = recursion(children, link1, link2, [])
    return [(res[i - 1], res[i]) for i in range(1, len(res))]


if __name__ == "__main__":
    relations_data = [
        ('zoran', 'ana'),
        ('ivo', 'mara'),
        ('pero', 'ana'),
        ('ivo', 'sanja'),
        ('mara', 'sara'),
        ('ana', 'marko'),
        ('sara', 'zoran'),
        ('sara', 'pero'),
        ('sara', 'marko'),
        ('ivan', 'ivana')
    ]
    print(are_links_connected(relations_data, 'ivo', 'marko'))
