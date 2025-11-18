from random import *
from datetime import datetime
from time import time, sleep
from generators import play
from mgen import MorseGenerator
from os import system
from pynput.keyboard import Key, Controller

date = datetime.now().strftime("%Y-%m-%d %H:%M")
test_status = False
window_status = False
quit = False
key_press = Controller()


def _create_filename():
    filename = date.split(" ")
    d = filename[0].replace("-", ".")
    t = filename[1].replace(":", "-")
    return f"{d}_{t}.txt"


def enter_pressed():
    key_press.press(Key.enter)
    key_press.release(Key.enter)


def _groups_generator(start, end, groups):
    group = []
    chars = 5

    if not groups:
        chars = 1

    for _ in range(0, chars):
        rand = randint(start, end)
        group.append(rand)
    return group


def morse_test(start, end, groups=True, tone=800, rate=0.1):
    global test_status
    global window_status
    global quit
    window_status = True
    mg = MorseGenerator(unit=rate, frequency=tone)
    counter = 0
    attempts_counter = 0
    right_answers = 0
    mistakes = 0
    test = ""
    input_string = ""
    symbols = (
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
        "0",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        ".",
        ",",
        ":",
        ";",
        "?",
        "-",
        "_",
        "(",
        ")",
        "'",
        "=",
        "+",
        "/",
        "@",
    )

    if not groups:
        quantity = 250
    else:
        quantity = 60

    if groups and start == 0 and end == 25:
        test_type = "groups (letters only)."
    elif groups and start == 26 and end == 35:
        test_type = "groups (digits only)."
    elif groups and start == 0 and end == 35:
        test_type = "groups (letters and digits)."
    elif groups and start == 36 and end == 49:
        test_type = "groups (other characters)."
    elif not groups and start == 0 and end == 25:
        test_type = "singles (letters only)."
    elif not groups and start == 26 and end == 35:
        test_type = "singles (digits only)."
    elif not groups and start == 0 and end == 35:
        test_type = "singles (letters and digits)."
    elif not groups and start == 36 and end == 49:
        test_type = "singles (other characters)."
    else:
        test_type = "unknown."

    print(
        f'Test: {test_type}\nType what you heard, then press "SPACE" or "ENTER" to continue.'
    )
    while True:
        if input('Press "Y" for start or "N" for quit: ')[:1].upper() == "Y":
            print ('Press "ESC" for interrupt.')
            sleep(1)
            break
        else:
            window_status = False
            system("cls||clear")
            return

    start_time = time()
    test_status = True
    while counter < quantity:

        for index in _groups_generator(start, end, groups):
            test += symbols[index]
        play(mg.generate_text(test))

        input_string = input()[:5].upper().strip()

        if quit:
            window_status = False
            quit = False
            test_status = False
            system("cls||clear")
            return

        if groups == True and len(input_string) != 5:
            print("ERROR! 5 characters required.")
            play(mg.generate_text(test))
            input_string = input()[:5].upper().strip()

        if groups == False and len(input_string) != 1:
            print("ERROR! 1 character required.")
            play(mg.generate_text(test))
            input_string = input()[:1].upper().strip()

        if groups == False and input_string != test:
            while attempts_counter < 2 and input_string != test:
                print(f"ERROR! Try again. {2 - attempts_counter} attempts left.")
                play(mg.generate_text(test))
                input_string = input()[:1].upper().strip()
                if quit:
                    window_status = False
                    quit = False
                    test_status = False
                    system("cls||clear")
                    return
                if attempts_counter == 1 and input_string != test:
                    print(f'ERROR! The right answer is "{test}".')
                    sleep(1)
                attempts_counter += 1
                mistakes += 1
        attempts_counter = 0

        if groups == False and input_string == test:
            print("OK")
            right_answers += 1
        if groups == True and input_string == test:
            right_answers += 1
        elif groups == True and input_string != test:
            mistakes += 1

        test = ""
        counter += 1

    test_status = False
    end_time = time()
    duration = int(end_time - start_time)

    if groups:
        chars_quantity = right_answers * 5
    else:
        chars_quantity = right_answers

    speed = int((chars_quantity / duration) * 60)
    if speed <= 0:
        speed = "less than 1"

    result = f"Current date: {date}.\nTest: {test_type}\nRight answers: {right_answers}. \nMistakes: {mistakes}.\nDuration: {duration //60} minutes, {duration %60} seconds.\nAverage speed: {speed} CpM ({speed //5} WpM)." 
    print(f"\n\n{result}")

    while True:
        if (
            input('Would you like to save results? (Yes - "Y", no - "N")')[:1].upper()
            == "Y"
        ):
            filename = _create_filename()
            file = open(f"results/{filename}", "w")
            file.write(result)
            file.close()
            print(f'Results saved to folder "results/{filename}".')
            sleep(2)
            window_status = False
            system("cls||clear")
            return
        else:
            system('cls||clear')
            window_status = False
            return
