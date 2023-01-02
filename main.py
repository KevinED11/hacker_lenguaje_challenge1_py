'''
* Escribe un programa que reciba un texto y transforme lenguaje natural a
* "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
*  se caracteriza por sustituir caracteres alfanuméricos.
* - Utiliza esta tabla(https: // www.gamehouse.com/blog/leet-speak-cheat-sheet/)
*   con el alfabeto y los números en "leet".
*   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''


def translate_to_hacker_leet(text):

    leet_map = {
        'a': '4',
        'b': '6',
        'c': '(',
        'd': '|)',
        'e': '3',
        'f': '|=',
        'g': '6',
        'h': '|-|',
        'i': '1',
        'j': '_|',
        'k': '|<',
        'l': '|_',
        'm': '|\/|',
        'n': '|\|',
        'o': '0',
        'p': '|D',
        'q': '(,)',
        'r': '|2',
        's': '5',
        't': '7',
        'u': '|_|',
        'v': '\/',
        'w': '\/\/',
        'x': '><',
        'y': '`/',
        'z': '2',
    }

    result = ''

    for char in text.lower():
        if char in leet_map:
            result += leet_map[char]
        else:
            result += char

    print(result)


if __name__ == "__main__":
    translate_to_hacker_leet('hacker')  # Output # |-|4(|<3|2
