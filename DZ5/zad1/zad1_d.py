# Napišite program koji će upotrebom regularnih izraza u tekstu naći sve dijelove
# koji se nalaze u uglatim zagradama i ispisati samo te dijelove.

import re


if __name__ == "__main__":
    text = \
        "Marko: [Marko test]\n" \
        "Ivan: [Ivan test]\n" \
        "Petra: [Petra test]\n" \
        "Josip: [Josip test\n" \
        "u novom redu]"

    print("Text:")
    print(text)

    print()
    print("Result:")
    uglate_zagrade_sadrzaj = re.findall("\\[([^]]+)\\]", text)
    for sadrzaj in uglate_zagrade_sadrzaj:
        print(sadrzaj.replace("\n", " "))
