from pynput.keyboard import Key, Controller
import time

keyboard=Controller()


time.sleep(5)

espera=0.15
espera2=0.4

ciclos=6


for i in range(ciclos):

    time.sleep(espera)
    keyboard.press(Key.alt)
    time.sleep(espera)
    keyboard.press("h")
    time.sleep(espera)
    keyboard.release("h")
    time.sleep(espera)
    keyboard.press("e")
    time.sleep(espera)
    keyboard.release("e")
    time.sleep(espera)
    keyboard.press("i")
    time.sleep(espera)
    keyboard.release("i")
    time.sleep(espera)
    keyboard.release(Key.alt)

    time.sleep(espera2)
    keyboard.press(Key.enter)
    time.sleep(espera2)
    keyboard.release(Key.enter)
    time.sleep(espera2)
    keyboard.press(Key.enter)
    time.sleep(espera2)
    keyboard.release(Key.enter)

    time.sleep(espera2)
    keyboard.press(Key.ctrl)
    time.sleep(espera)
    keyboard.press(Key.tab)
    time.sleep(espera)
    keyboard.release(Key.tab)
    time.sleep(espera)
    keyboard.release(Key.ctrl)
    time.sleep(espera2)
