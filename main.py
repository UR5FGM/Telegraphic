#Telegraphic version 2.0
#Created by Serhii Kolomiitsev <serge.kolomeitsev@gmail.com>
from generators import play
from mgen import MorseGenerator
import cw_test
import subprocess
from adjustment import *
from pynput import keyboard
import os
import message
import help
import intro

set_tone = Tone_level()
set_rate = Rate_level()
select_item = ""

if not os.path.isdir("results"):
    os.mkdir("results")
if not os.path.isdir("audio"):
    os.mkdir("audio")

def generate(char, rate, tone):
    mg = MorseGenerator(unit=rate, frequency=tone)
    play(mg.generate_text(char))

def test(key):
    if key == keyboard.Key.f1:
        print("test")


def additional_menu(key):
    if key == keyboard.Key.space:
        if cw_test.test_status:
            cw_test.enter_pressed()
    if key == keyboard.Key.esc:
        if message.message_window_status:
            message.exit()
        if cw_test.test_status:
            cw_test.enter_pressed()
            cw_test.quit = True
    if key == keyboard.Key.f1:
        if not cw_test.window_status and not message.message_window_status:
            os.system("cls||clear")
            help.morse_code()
    if key == keyboard.Key.f3:
        message.file_write(rate=set_rate.speed, tone=set_tone.freq)
    if key == keyboard.Key.f7:
        if not cw_test.window_status and not message.message_window_status:
            set_tone.down()
            generate("e", rate=set_rate.speed, tone=set_tone.freq)
    if key == keyboard.Key.f8:
        if not cw_test.window_status and not message.message_window_status:
            set_tone.up()
            generate("e", rate=set_rate.speed, tone=set_tone.freq)
    if key == keyboard.Key.f9:
        if not cw_test.window_status and not message.message_window_status:
            set_rate.down()
            generate("v", rate=set_rate.speed, tone=set_tone.freq)
    if key == keyboard.Key.f10:
        if not cw_test.window_status and not message.message_window_status:
            set_rate.up()
            generate("v", rate=set_rate.speed, tone=set_tone.freq)


def menu():
    while True:
        intro.welcome()

        select_item = input('Make a choice, then press "Enter" to confirm:')
        if select_item == "1":
            os.system("cls||clear")
            cw_test.morse_test(0, 25, False, rate=set_rate.speed, tone=set_tone.freq)
        elif select_item == "2":
            os.system("cls||clear")
            cw_test.morse_test(26, 35, False, rate=set_rate.speed, tone=set_tone.freq)
        elif select_item == "3":
            os.system("cls||clear")
            cw_test.morse_test(0, 35, False, rate=set_rate.speed, tone=set_tone.freq)
        elif select_item == "4":
            os.system("cls||clear")
            cw_test.morse_test(36, 49, False, rate=set_rate.speed, tone=set_tone.freq)
        elif select_item == "5":
            os.system("cls||clear")
            cw_test.morse_test(0, 25, rate=set_rate.speed, tone=set_tone.freq)
        elif select_item == "6":
            os.system("cls||clear")
            cw_test.morse_test(26, 35, rate=set_rate.speed, tone=set_tone.freq)
        elif select_item == "7":
            os.system("cls||clear")
            cw_test.morse_test(0, 35, rate=set_rate.speed, tone=set_tone.freq)
        elif select_item == "8":
            os.system("cls||clear")
            cw_test.morse_test(36, 49, rate=set_rate.speed, tone=set_tone.freq)
        elif select_item == "9":
            os.system("cls||clear")
            message.text(rate=set_rate.speed, tone=set_tone.freq)
        elif select_item == "0":
            return""
        else:
            pass
        select_item = ""

listener = keyboard.Listener(on_press=additional_menu)
listener.start()
proc=subprocess.Popen(menu(), shell=True)
proc.terminate()
listener.stop()
