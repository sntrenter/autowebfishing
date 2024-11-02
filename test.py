import pyautogui
import time
import pydirectinput
from PIL import ImageGrab,Image
import pygetwindow as gw
import dxcam

def center_mouse_on_app(app_title):
    try:
        app_window = pyautogui.getWindowsWithTitle(app_title)[0]
        app_window.activate()  # Bring window to front
        x, y, width, height = app_window.left, app_window.top, app_window.width, app_window.height
        center_x = x + (width // 2)
        center_y = y + (height // 2)
        pyautogui.moveTo(center_x, center_y)
    except IndexError:
        print("Application not found.")

def get_window(app_title):
    try:
        app_window = pyautogui.getWindowsWithTitle(app_title)[0]
        app_window.activate()  # Bring window to front
        x, y, width, height = app_window.left, app_window.top, app_window.width, app_window.height
        return x, y, width, height
    except IndexError:
        print("Application not found.")

def buckets():
    time.sleep(1)
    print("pos. 3")
    pydirectinput.press('3')
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

    print("pos. 4")
    pydirectinput.press('4')
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click()

def cast():
    time.sleep(1)
    print("pos. 1")
    pydirectinput.press('1')
    center_mouse_on_app("WEBFISHING v1.08")
    time.sleep(1)
    pyautogui.mouseDown(button='left')
    time.sleep(3.1)
    pyautogui.mouseUp(button='left')

def wait_for_start():
    camera = dxcam.create() 
    frame = camera.grab()
    if frame is None:
        return True
    cur = Image.fromarray(frame)
    cur = cur.crop((375, 450, 575, 575))
    img = Image.open("fishing_start.png")
    start_img = img.crop((375, 450, 575, 575))
    return cur != start_img

def buy_bait():
    print("buying bait")
    time.sleep(1)
    pydirectinput.press('e')
    time.sleep(.5)
    (x,y,width, height) = get_window("WEBFISHING v1.08")
    pyautogui.moveTo(x + 810, y + 365)
    pyautogui.mouseDown(x=x + 810, y=y + 365,button='left')
    pyautogui.mouseUp()
    time.sleep(1)
    pydirectinput.press('esc')
    

def main():
    time.sleep(5)

    loop = 0
    bucket_time = time.time()
    while True:
        time.sleep(1)
        print("loop: ", loop)
        
        if time.time() - bucket_time > 120: #do buckets 
            print("buckets")
            buckets()
            bucket_time = time.time()
        else:# try fishing again
            print("time since last bucket: ", time.time() - bucket_time)
            cast()
            while wait_for_start():
                print("waiting for minigame start")
                time.sleep(1)
            print("minigame detected")
            time.sleep(1)
            mini_game_start = time.time()
            pyautogui.mouseDown(button='left')
            pyautogui.mouseUp(button='left')
            print("initial click")
            time.sleep(1)
            while time.time() - mini_game_start < 17:#15 seemed ok, 17 for safety
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
            print("done clicking")
            buy_bait() 

        if loop == 10:
            break       

        loop += 1


main()


#print(wait_for_start())


#time.sleep(5)
#cast()
#while wait_for_start():
#    print("waiting for start")
#    time.sleep(1)
#time.sleep(3)
#mini_game_start = time.time()
#time.sleep(1)
#pyautogui.mouseDown(button='left')
#time.sleep(.1)
#pyautogui.mouseUp(button='left')
#time.sleep(.1)
#while time.time() - mini_game_start < 15:
#    pyautogui.mouseDown(button='left')
#    time.sleep(.05)
#    pyautogui.mouseUp(button='left')
#print("done")


#for i in range(100):
#    pyautogui.mouseDown(button='left')
#    time.sleep(.1)
#    pyautogui.mouseUp(button='left')


#https://github.com/ra1nty/DXcam

#start bucket timer
# hold for 5 secs to cast reel
#wait until new frames stop coming in 
#"start frame appears"
#click
#while new frames aren't coming in (stuck on "3" frame)
    #start clicking 
    #check for new frame
        #break
#catch menu 1
#possible catch menu 2
#refil bait
#check buckets timer
    #do buckets if 2 min



#fishing time
#:44
#:23
#:52
#:01
#:48
#:59
#:30
#:11
#:13
#1:23
#:25
#:30
#:12
#:16