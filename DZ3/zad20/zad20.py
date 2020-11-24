# Neka sljedeći data označavaju ljude koji su međusobno direktno povezani:
# podaci3 = [('zoran', 'ana'), ('ivo', 'mara'),
# ('pero', 'ana'), ('mara', 'sara'), ('ana', 'marko'),
# ('sara', 'zoran')]
# U ovom primjeru Zoran je povezan s Anom, Ana s Markom, itd. Međutim, Zoran je
# samo indirektno povezan s Markom. U ovom primjeru pretpostavljamo da je jedna
# osoba povezana sa samo jednom drugom osobom i da nema kružnih veza. Napišite
# funkciju slijedi koja daje True ako su dvije zadane osobe povezane (direktno ili indirektno) i False ako nisu:
# >>> slijedi(podaci3 , 'ivo', 'ana')
# True


def recursion(children, parent, search_link, current_link=None):
    if current_link == search_link:
        return True
    for child in children[parent]:
        if not child == current_link and recursion(children, child, search_link, parent):
            return True
    return False


def are_links_connected(data, link1, link2):
    children = {}
    for tuple in data:
        children.setdefault(tuple[0], []).append(tuple[1])
        children.setdefault(tuple[1], []).append(tuple[0])
    for k in children:
        print(k, "-", children[k])
    print()
    return recursion(children, link1, link2)


if __name__ == "__main__":
    data = [('zoran', 'ana'),
            ('ivo', 'mara'),
            ('pero', 'ana'),
            ('mara', 'sara'),
            ('ana', 'marko'),
            ('sara', 'zoran'),
            ('ivan', 'petra')]
    print(are_links_connected(data, 'ivo', 'ana'))
