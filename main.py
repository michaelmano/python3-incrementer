import keyboard

filename = "codes.txt"
COUNT = 0

def incrementCode():
    global COUNT
    COUNT = COUNT+1

def resetCode():
    global COUNT
    COUNT = 0

def printCode():
    with open(filename) as fp:
        for i, code in enumerate(fp):
            if i == COUNT:
                code = code.strip('\n')
                code = code.strip('\t')
                print('Attempting code', code)
                keyboard.write(code)
                if 'str' in code:
                    break
                break

    incrementCode()

keyboard.add_hotkey('cmd+.', printCode)
keyboard.add_hotkey('cmd+]', resetCode)

keyboard.wait('ctrl+shift+0')