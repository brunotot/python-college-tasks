# Napišite program koji će upotrebom regularnih izraza u tekstu zamijeniti sve
# datume oblika DD.MM.GGGG. nizom slova X.

import re


if __name__ == "__main__":
    text = \
        "Marko: 11.11.1111\n" \
        "Ivan: 22.22.2222\n" \
        "Petra: 33.33.3333\n" \
        "Josip: 44.44.4444\n"

    print("Text:")
    print(text)
    result = re.sub("([0-9]{2}.[0-9]{2}.[0-9]{4})", "XX.XX.XXXX", text)
    print("Result:")
    print(result)
