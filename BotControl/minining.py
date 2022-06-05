import time

import pyautogui
import threading


class Mining:
    def __init__(self):
        self.mine_th = None
        self.stop_event = None

    def _mine(self, tool):
        if tool == "Sword":
            pyautogui.press("1")
            pyautogui.mouseDown(button="left")
        if tool == "Pickaxe":
            pyautogui.press("2")
            pyautogui.mouseDown(button="left")
        elif tool == "Axe":
            pyautogui.press("3")
            pyautogui.mouseDown(button="left")

        elif tool == "Shovel":
            pyautogui.press("4")
            pyautogui.mouseDown(button="left")

        while not self._is_done():
            if tool == "Sword":
                pyautogui.mouseUp(button="left")
                time.sleep(0.3)
                pyautogui.mouseDown(button="left")

    def start_thread(self, tool):
        self.mine_th = threading.Thread(target=self._mine, args=(tool,))
        self.stop_event = threading.Event()
        self.mine_th.start()

    def stop_thread(self):
        self.stop_event.set()
        while not self._is_done():
            pass

    def _is_done(self):
        return self.stop_event.is_set()

    def change_tool(self, new_tool):
        self.stop_thread()
        self.start_thread(new_tool)
