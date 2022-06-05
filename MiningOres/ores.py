import os
from time import sleep

import pyautogui


class HandleOres:
    def __init__(self, movement, mining):
        self.movement = movement
        self.mining = mining

    def detect_ores(self):
        diamond = None
        gold = None
        iron = None
        ores = []
        loop_counter = 0

        while loop_counter < 5:
            diamond = pyautogui.locateOnScreen("Ores/2022-06-04 15_09_56-latest (1920×1017) - Brave.png", region=(0, 0, 1920, 1080), confidence=0.5)

            iron = pyautogui.locateOnScreen("Ores/2022-06-04-131057_231x233_scrot.png", region=(0, 0, 1920, 1080), confidence=0.5)

            loop_counter += 1
            if any([diamond, iron]):
                break
        if all([diamond, gold, iron]) is None:
            return
        ores.append(diamond)
        ores.append(iron)
        loop_counter = 0
        self.mine_ores(ores)

    def mine_ores(self, ores):
        for ore in ores:
            if ore:
                pyautogui.moveTo(ore.left + ore.width / 2, ore.top + ore.height / 2)
                sleep(3)
