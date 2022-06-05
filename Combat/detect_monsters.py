import pyautogui


class Monsters:
    def __init__(self, miningIn, movementIn):
        self.mining = miningIn
        self.movement = movementIn

    def detect_monsters(self):
        zombie = None
        skeleton = None
        spider = None
        creeper = None
        loop_counter = 0

        while loop_counter < 4:
            skeleton = pyautogui.locateOnScreen("/home/skyr4me/Screenshots/2022-06-04-110644_210x216_scrot.png",
                                                region=(0, 0, 1920, 1080), confidence=0.6)
            zombie = pyautogui.locateOnScreen("/home/skyr4me/Screenshots/2022-06-05-135428_149x157_scrot.png",
                                              region=(0, 0, 1920, 1080), confidence=0.6)
            if any([skeleton, zombie]):
                break
            loop_counter += 1

        self.fight_monsters([zombie, skeleton, spider, creeper])

    def fight_monsters(self, monster_image):
        # self.mining.change_tool("Sword")
        for x in monster_image:
            if x is not None:
                pyautogui.moveTo(x.left + x.width / 2, x.top + x.height / 2)
        # self.movement.stop_thread()
