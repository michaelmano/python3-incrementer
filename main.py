#!/usr/bin/python
# -*- coding: utf-8 -*-
import keyboard
import time

filename = 'codes.txt'
COUNT = 0


def incrementCode():
    global COUNT
    COUNT = COUNT + 1


def resetCode():
    global COUNT
    COUNT = 0


def printCode():
    with open(filename) as fp:
        for (i, code) in enumerate(fp):
            if i == COUNT:
                code = code.strip('\n')
                code = code.strip('\t')
                print ('Attempting code', code)
                for num in list(code):
                    time.sleep(0.22)
                    keyboard.press(num)
                    time.sleep(0.05)
                    keyboard.release(num)

                if 'str' in code:
                    break
                break

    incrementCode()


keyboard.add_hotkey('ctrl+.', printCode)
keyboard.add_hotkey('ctrl+]', resetCode)

keyboard.wait('ctrl+shift+0')
