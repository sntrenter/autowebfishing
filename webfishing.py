import pyautogui
import time
import pydirectinput

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
    # 1:06, 1:40
    # 1:50, 1:55
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


        pydirectinput.press('5')
        time.sleep(1)
        pyautogui.click()
        time.sleep(.1)
        pyautogui.click()
        time.sleep(.1)
        pyautogui.click()
        time.sleep(.1)
        print("wait")
        time.sleep(120)



main()
