from generators import play, write_wav
from mgen import MorseGenerator
from datetime import datetime
from pynput.keyboard import Key, Controller
from os import system

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
key_press = Controller()
string_text = ""
message_window_status = False
quit = False


def _create_filename():
    filename = date.split(" ")
    d = filename[0].replace("-", ".")
    t = filename[1].replace(":", "-")
    return f"{d}_{t}"


def exit():
    global quit
    global string_text
    quit = True
    string_text = ""
    key_press.press(Key.enter)
    key_press.release(Key.enter)


def file_write(tone=800, rate=0.1):
    mg = MorseGenerator(unit=rate, frequency=tone)
    filename = _create_filename()
    global string_text
    if string_text == "":
        pass
    else:
        print("\nPlease wait...\n")
        audio_sorce = mg.generate_text(string_text)
        with open(f"audio/message{filename}.wav", "wb") as f:
            write_wav(f, audio_sorce)
        print(f'Text saved to "audio/{filename}.wav.')
    string_text = ""


def text(tone=800, rate=0.1):
    global message_window_status
    global string_text
    global quit
    message_window_status = True
    mg = MorseGenerator(unit=rate, frequency=tone)
    print(
        'Press "ENTER" for play message.\n"F3" - save text after playing as audio file.\n     Press "ESC" for quit.'
    )
    while not quit:
        string_text = input("Text:")
        if string_text == "":
            pass
        else:
            play(mg.generate_text(string_text))
    message_window_status = False
    quit = False
    system("cls||clear")
