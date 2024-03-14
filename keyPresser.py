import keyboard as kb, time

def keyPresser(self, keys, length, delay):
    time.sleep(5)
    keys = keys
    while True:
        for key in keys:
            kb.press(key)
            time.sleep(length)
            kb.release(key)
        time.sleep(delay)