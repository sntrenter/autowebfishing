import pyautogui
import time
import pydirectinput
from PIL import ImageGrab,Image
import pygetwindow as gw
import dxcam

def get_bar(img):
    img = img.rotate(25)
    img = img.crop((495, 435, 500, 990))
    return img

def capture_window(window_title):
    window = pyautogui.getWindowsWithTitle(window_title)[0]
    if not window:
        raise Exception(f"Window with title '{window_title}' not found.")
    left, top, width, height = window.left, window.top, window.width, window.height
    screenshot = pyautogui.screenshot(region=(left, top, width, height))

    return screenshot

def main():
    time.sleep(5)

    camera = dxcam.create() 
    n = 0
    same = 0
    last_img = None
    while True:
        time.sleep(.1)
        #pyautogui.press('printscreen')
        #img = ImageGrab.grabclipboard()
        #img = capture_window("WEBFISHING v1.08")
        #img = gw.getWindowsWithTitle("WEBFISHING v1.08")[0]
        #img = ImageGrab.grab(bbox=(img.left, img.top, img.width, img.height))
        #if img is None:
        #    continue

        frame = camera.grab()
        if frame is None:
            continue
        img = Image.fromarray(frame)
        img.save(str(n) + ".png")

        

        n += 1
        #if last_img == img:
        #    same += 1
        #    print("Same Found: ", str(same))
        #last_img = img
     

main()
print("done")


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