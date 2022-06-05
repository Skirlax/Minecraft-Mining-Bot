import pyautogui
import MiningOres.ores
from stopwatch import Stopwatch
import BotControl.movement
import BotControl.minining
import Combat.detect_monsters
import BotControl.detect_lava
from time import sleep
from pynput.keyboard import Key, Listener


mine = BotControl.minining.Mining()
move_th = BotControl.movement.Movement()
lava_detect = BotControl.detect_lava.LavaHandle(move_th, mine)
monsters_detect = Combat.detect_monsters.Monsters(mine, move_th)
ores = MiningOres.ores.HandleOres(move_th, mine)

sw = Stopwatch().reset()


class Recon:

    def __init__(self):
        starter = 7
        sw.start()
        while sw.duration < 7:
            print(f"Threads launching in {starter} seconds. Get ready!")
            sleep(1)
            starter -= 1
        # mine.start_thread("Pickaxe")
        # sleep(0.5)
        # move_th.start_thread("forward")
        # with Listener(on_press=self.check_for_exit) as listener:
        #     listener.join()
        while True:
            # lava_detect.check_for_lava()
            # monsters_detect.detect_monsters()
            # ores.detect_ores()
            lava_detect.check_for_lava()


    def check_for_exit(self, key):
        if key == Key.esc:
            move_th.stop_thread()
            mine.stop_thread()
            exit(0)





if __name__ == "__main__":
    Recon()
