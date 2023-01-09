import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import KeyCode, Listener

toggle_key = KeyCode(char='s') # Stop clikers
cliking = False
mouse = Controller()


def kliker():
    while True:
        if cliking:
            mouse.click(Button.left, 1)
            time.sleep(0.1)


def toggle_event(key):
    if key == toggle_key:
        global cliking
        cliking = not cliking


def main():
    cliking_thread = threading.Thread(target=kliker)
    cliking_thread.start()

    with Listener(on_press=toggle_event) as listener:
        listener.join()


if __name__ == '__main__':
    main()
