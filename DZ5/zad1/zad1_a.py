# Napišite program koji će upotrebom regularnih izraza pronaći u tekstu sve brojeve telefona napisane
# u obliku XXX-XXXX-XXX, gdje je X neka znamenka.


import re


if __name__ == "__main__":
    text = \
        "Marko: 111-1111-111\n" \
        "Ivan: 222-2222-222\n" \
        "Petra: 333-3333-333\n" \
        "Josip: 444-4444-444\n"

    print("Text:")
    print(text)
    phone_number_occurrences = re.findall("([0-9]{3}-[0-9]{4}-[0-9]{3})", text)
    print("Result:")
    for num in phone_number_occurrences:
        print(num)
