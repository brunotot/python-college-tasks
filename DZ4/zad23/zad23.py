# Napišite rekurzivnu funkciju predak koja ispisuje tko je kome predak na osnovu podataka kao u sljedećem primjeru:
# rel_predak = [
#   ('petar', 'marko'),
#   ('irena', 'ivan'),
#   ('marko', 'stjepan'),
#   ('ana', 'petra'),
#   ('marko', 'suzana'),
#   ('ivan', 'marija'),
#   ('suzana', 'josip'),
# ]
# Gornja lista sadrži parove (A, B) koji označavaju odnos A je predak od B. Prema toj
# listi Petar je predak od Marka, Stjepana, Suzane i Josipa, a Irena od Ivana i Marije.
# Primjer upotrebe ove funkcije:
# >>> predak(rel_predak , 'petar')
# ['marko', 'stjepan', 'suzana', 'josip']


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
