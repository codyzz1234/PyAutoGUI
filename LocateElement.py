import pyautogui

def locate_image():
    cords_image = pyautogui.locateOnScreen('youtube.png',confidence=.8)
    print(cords_image)
    cords_center = pyautogui.center(cords_image)
    print(cords_center)
    pyautogui.click(cords_center[0],cords_center[1])
    
    
def main():
    locate_image()
main()