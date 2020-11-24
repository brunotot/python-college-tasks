# Riješite prethodni zadatak tako da prve tri znamenke broja telefona mogu biti
# opcionalne.

import re


if __name__ == "__main__":
    text = \
        "Marko: 111-1111-111\n" \
        "Ivan: 2222-222\n" \
        "Petra: 3-3333-333\n" \
        "Josip: 44-4444-444\n"

    print("Text:")
    print(text)
    phone_number_occurrences = re.findall("(([0-9]{1,3}-)?[0-9]{4}-[0-9]{3})", text)
    print("Result:")
    for num in phone_number_occurrences:
        print(num[0])
