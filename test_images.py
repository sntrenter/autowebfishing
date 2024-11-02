import pyautogui
import time
import pydirectinput
from PIL import ImageGrab,Image
import pygetwindow as gw
import dxcam

def main():
    camera = dxcam.create() 
    frame = camera.grab()
    cur = Image.fromarray(frame)
    cur = cur.crop((375, 435, 600, 575))
    cur.show()
    #if frame is None:
    #    pass
    #else:
    #    img = Image.fromarray(frame)
    #    img.save("fishing_start" + ".png")
    img = Image.open("fishing_start.png")
    start_img = img.crop((375, 435, 600, 575))
    #start_img.show()
    print(cur == start_img)


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