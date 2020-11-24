# Zadatak 24:
# Dva stringa su anagrami ako se od jednog može dobiti drugi premještanjem znakova.
# Na primjer, stringovi ”abcb” i ”bcab” su anagrami jer sadrže ista slova, samo u
# drugačijem redoslijedu, ali ”abcc” i ”abbc” nisu. Napišite funkciju anagram(s1, s2)
# koja daje True ako su stringovi s1 i s2 anagrami na sljedeće načine:
# (a) Sortiranjem
# (b) Upotrebom mapa
# (c) Upotrebom skupova


from zad25_a import Multiset


def string_sort(string):
    character_list = list(string)
    string_length = len(string)
    for i in range(0, string_length):
        for j in range(0, string_length - i - 1):
            if character_list[j] > character_list[j + 1]:
                character_list[j], character_list[j + 1] = character_list[j + 1], character_list[j]
    return "".join(character_list)


def string_map(string):
    str_map = {}
    string_length = len(string)
    for i in range(0, string_length):
        str_map[string[i]] = str_map[string[i]] + 1 if string[i] in str_map else 1
    return str_map


def anagram_sort(s1, s2):
    return len(s1) == len(s2) and string_sort(s1) == string_sort(s2)


def anagram_map(s1, s2):
    return len(s1) == len(s2) and dict(string_map(s1)) == dict(string_map(s2))


def anagram_set(s1, s2):
    multiset_result = Multiset(s1).intersection(Multiset(s2))
    multiset_result_array = multiset_result.array
    return len(s1) == len(s2) and len(multiset_result_array) == 0


if __name__ == '__main__':
    print(anagram_sort("abcb", "bcab"))
    print(anagram_map("abcb", "bcab"))
    print(anagram_set("abbc", "abcc"))
