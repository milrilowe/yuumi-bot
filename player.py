import pyautogui as auto
import keyboard, time

time.sleep(2)

while True:
    auto.moveTo(1570, 600)
    keyboard.press_and_release('w')
    auto.moveTo(1680, 600)
    keyboard.press_and_release('w')
    auto.moveTo(1790, 600)
    keyboard.press_and_release('w')
    auto.moveTo(1900, 600)
    keyboard.press_and_release('w')
    if keyboard.is_pressed('q'):
        print('you quit')
        break

