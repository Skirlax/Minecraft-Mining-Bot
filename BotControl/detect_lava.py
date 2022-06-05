import os
import BotControl.movement
from stopwatch import Stopwatch
import pyautogui

sw = Stopwatch()
move = BotControl.movement.Movement()
sw_run_back = Stopwatch().reset()


class LavaHandle:
    def __init__(self, movement, mining):
        self.movement_passed = movement
        self.mining_passed = mining

    def check_for_lava(self):
        lava = None
        for file in os.listdir("Images"):
            sw.start()
            while lava is None and sw.duration < 0.5:
                lava = pyautogui.locateOnScreen(f"Images/{file}", region=(0, 0, 1920, 1080), confidence=0.6)
            if lava is not None:
                break
            sw.reset()

        if lava is not None:
            pyautogui.moveTo(lava.left + lava.width / 2, lava.top + lava.height / 2)

    def run_away(self):
        self.movement_passed.change_direction("back")
        move.start_thread("jump")
        sw_run_back.start()
        while sw_run_back.duration < 3:
            pass
        sw_run_back.reset()
        move.stop_thread()
        pyautogui.moveRel(-90, 0)
        self.movement_passed.change_direction("forward")