import threading
import pyautogui


class Movement:
    def __init__(self):
        self.thread = None
        self.stop_event = None

    def _move(self, direction):
        if direction == "forward":
            pyautogui.keyDown("w")
        elif direction == "back":
            pyautogui.keyDown("s")
        elif direction == "left":
            pyautogui.keyDown("a")
        elif direction == "right":
            pyautogui.keyDown("d")

        elif direction == "jump":
            pyautogui.keyDown("space")
        else:
            print("Invalid direction")
        while not self.is_done():
            pass

    def start_thread(self, direction):
        self.thread = threading.Thread(target=self._move, args=(direction,))
        self.stop_event = threading.Event()
        self.thread.start()

    def stop_thread(self):
        self.stop_event.set()
        while not self.is_done():
            pass

    def is_done(self):
        return self.stop_event.is_set()


    def change_direction(self, direction):
        self.stop_thread()
        self.start_thread(direction)
