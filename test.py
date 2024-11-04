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
    time.sleep(2)
    pydirectinput.press('e')
    time.sleep(3)
    (x,y,width, height) = get_window("WEBFISHING v1.08")
    pyautogui.moveTo(x + 810, y + 365)
    pyautogui.scroll(1000)
    pyautogui.mouseDown(x=x + 810, y=y + 365,button='left')
    pyautogui.mouseUp()
    time.sleep(5)
    pydirectinput.press('esc')
    time.sleep(2)

def check_if_store_empty():
    camera = dxcam.create() 
    frame = camera.grab()
    #if frame is None:
    #    return True
    cur = Image.fromarray(frame)
    cur = cur.crop((225, 500, 330, 625))
    img = Image.open("empty_store.png")
    start_img = img.crop((225, 500, 330, 625))
    return cur != start_img

def sell_fish():
    print("selling fish")
    (x,y,width, height) = get_window("WEBFISHING v1.08")
    pyautogui.moveTo(x + 810, y + 365)
    camera = dxcam.create() 
    time.sleep(2)
    pydirectinput.press('e')
    time.sleep(3)
    #pyautogui.moveTo(x + 280, y + 800)

    while check_if_store_empty():
        pyautogui.mouseDown(x=x + 280, y=y + 585,button='left')
        pyautogui.mouseUp()
        time.sleep(.25)
        frame = camera.grab()
        new_frames = 0
        while True: #wait for new frame
            frame = camera.grab()
            if frame is None:
                if new_frames > 10:
                    break
            else:
                new_frames += 1
        time.sleep(.5)
    time.sleep(2)
    pydirectinput.press('esc')
    time.sleep(1)

def change_bait_lure(bait="",lure=""):
    time.sleep(1)
    (x,y,width, height) = get_window("WEBFISHING v1.08")
    pyautogui.moveTo(x + 810, y + 365)
    pydirectinput.press('b')
    time.sleep(1)
    match bait:
        case "no bait":
            y_offset = 450
        case "worms":
            y_offset = 490
        case "crickets":
            y_offset = 530
        case "leaches":
            y_offset = 570
        case "minnows":
            y_offset = 610
        case "squid":
            y_offset = 650
        case "nautalis":
            y_offset = 690
        case "":
            pass
    if bait != "":
        pyautogui.mouseDown(x + 600, y + y_offset)
        pyautogui.mouseUp()
        time.sleep(1)
    
    match lure:
        case "patient":
            pyautogui.moveTo(x + 1000, y + 560)
            pyautogui.scroll(1000)
            y_offset = 560
        case "fresh":
            pyautogui.moveTo(x + 1000, y + 560)
            pyautogui.scroll(1000)
            y_offset = 680
        case "magnet":
            pyautogui.moveTo(x + 1000, y + 560)
            pyautogui.scroll(-1000)
            y_offset = 480
    if lure != "":
        pyautogui.mouseDown(x + 1000, y + y_offset)
        pyautogui.mouseUp()
        time.sleep(1)

    pydirectinput.press('esc')
    time.sleep(1)

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
            time_since_cast = time.time()  
            while wait_for_start():
                print("waiting for minigame start")
                print("time since cast: ", time.time() - time_since_cast)
                if time.time() - time_since_cast > 120:
                    print("stuck somewhere, pressing esc to try and break out")
                    pydirectinput.press('esc')
                    break
                time.sleep(1)
            print("minigame detected")
            time.sleep(1)
            mini_game_start = time.time()
            pyautogui.mouseDown(button='left')
            pyautogui.mouseUp(button='left')
            print("initial click")
            time.sleep(1)
            while time.time() - mini_game_start < 25:#15 seemed ok, 17 for safety,20 not safe enough for large fish, 25 seems ok
                pyautogui.mouseDown(button='left')
                pyautogui.mouseUp(button='left')
            print("done clicking")
            
            if loop % 15 == 0:
                sell_fish()
                buy_bait()

        #if loop == 10:
        #    break       

        loop += 1



#main()

camera = dxcam.create() 
frame = camera.grab()
#if frame is None:
#    return True
cur = Image.fromarray(frame)
cur = cur.crop((375, 450, 575, 575))
img = Image.open("fishing_start.png")
start_img = img.crop((375, 700, 475, 800))
#return cur != start_img
start_img.show()
#cur.show()

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