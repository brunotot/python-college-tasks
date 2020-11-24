# Zadatak 23:
# Napišite program koji za zadani string pronalazi broj podstringova
# koji se čitaju isto s lijeva na desno i s desna na lijevo. Na primjer,
# u stringu "istitisak" postoje dva takva podstringa: "tit" i "iti".


def get_amount_of_substring_palindromes(string):
    counter = 0
    string_length = len(string)
    if string_length > 1:
        for i in range(2, string_length + 1):
            for j in range(0, string_length - i + 1):
                normal_substring = string[j:j + i]
                reversed_substring = normal_substring[::-1]
                if normal_substring == reversed_substring:
                    counter += 1
    return counter


if __name__ == '__main__':
    print(get_amount_of_substring_palindromes("istitisak"))

