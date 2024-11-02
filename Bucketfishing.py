import pyautogui
import time
import pydirectinput
import sys

def main():
    print("make sure both buckets are already placed")
    print("and that they are in slot 3 and 4")
    print("also that the tambourine is in slot 5")
    #times when max level gets both fish (seconds)
    # 1:30, 1:45
    # 1:10, 1:40
    # 1:30, 1:30
    # 1:30, 1:30
    # 1:08, 1:20
    # 1:06, 1:40aw
    # 1:50, 1:55dw
    time.sleep(5)
    while True:

        print("3")
        pydirectinput.press('3')
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(3)

        print("4")
        pydirectinput.press('4')
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(3)

        pydirectinput.press('5')
        time.sleep(1)
        pyautogui.click()
        time.sleep(.1)
        pyautogui.click()
        time.sleep(.1)
        pyautogui.click()
        time.sleep(.1)
        print("wait")
        for remaining in range(120, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\r")
        print("done waiting!           ")
        sys.stdout.flush()
        

main()
