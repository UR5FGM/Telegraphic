from pynput import keyboard
from os import system
import intro

letters = "LETTERS:"
digits = "DIGITS:"
characters = "PUNCTUATIONS:"


def _key_pressed():
    with keyboard.Events() as events:
        for event in events:
            key = event
            break
    return key


def morse_code():
    print(letters.center(len(letters) + 66, " "))
    print(
        "\tA: .-\tB: -...\tC: -.-.\n\tD: -..\tE: .\tF: ..-.\n\tG: --.\tH: ....\tI: ..\n\tJ: .---\tK: -.-\tL: .-..\n\tM: --\tN: -.\tO: ---\n\tP: .--.\tQ: --.-\tR: .-.\n\tS: ...\tT: -\tU: ..-\n\tV: ...-\tW: .--\tX: -..-\n\tY: -.--\tZ: --.."
    )
    print(digits.center(len(digits) + 66, " "))
    print(
        "\t1: .----\t2: ..---\t3: ...--\n\t4: ....-\t5: .....\t6: -....\n\t7: --...\t8: ---..\t9: ----.\t0: -----"
    )
    print(characters.center(len(characters) + 66, " "))
    print(
        '\n\t".": .-.-.-\t",": --..--\t":": ---...\n\t";": -.-.-.\t"?": ..--..\t"-": -....-\n\t"_": ..--.\t"(": -.--.\t")": -.-.-\n\t"\'": .----.\t"=": -...-\t"+": .-.-.\t"/": -..-.\n\t"@": .--.-.'
    )
    print ('Press "ESC" for close.')
    while True:
        stop = _key_pressed()

        if stop.key == keyboard.Key.esc:
            break
    system("cls||clear")
    intro.welcome()
