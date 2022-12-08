import pyautogui

def locate_image():
    cords_image = pyautogui.locateOnScreen('youtube.png',confidence=.8)
    print(cords_image)
    cords_center = pyautogui.center(cords_image)
    print(cords_center)
    pyautogui.click(cords_center[0],cords_center[1])

def chromeLaunch():
    chromeImageCords = pyautogui.locateOnScreen(r"C:\Users\kenle\Desktop\PyAutoGUI\PyAutoGUI\Images\Chrome.png",confidence=.8)
    chromeCenter = pyautogui.center(chromeImageCords)
    pyautogui.click(chromeCenter[0],chromeCenter[1])
    
def main():
    chromeLaunch()
    # locate_image()
main()