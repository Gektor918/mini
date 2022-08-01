import time
import keyboard
import webbrowser
from pywinauto.application import Application
from pynput.keyboard import Key, Controller


keyboard2 = Controller()
path = "C:\Program Files\Google\Chrome\Application\chrome.exe"


def board():
    keyboard2.press(Key.cmd)
    keyboard2.press(Key.up)
    keyboard2.release(Key.up)
    keyboard2.release(Key.cmd)


def webb(path):
    webbrowser.open_new_tab(path)
    try:
        app = Application(backend="win32").connect(title_re="Новая вкладка",timeout=10)
        app.window(title_re="Новая вкладка").set_focus()
        board()
    except:
        return


if __name__ == '__main__':
    keyboard.add_hotkey('win+shift',lambda:webb(path))
    time.sleep(604800)