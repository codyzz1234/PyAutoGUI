import pyautogui
import time
#mouse functions

def main():
    #print res of screen
    print(pyautogui.size()) 
    
    #prints where the mouse current position is
    print(pyautogui.position())
    
    #moves the mouse over time(x coordinate,y coordinate,seconds take to move)
    # pyautogui.moveTo(100,1000,3)
    
    #moves the mouse relative to its position
    # pyautogui.moveRel(100,100,3)
    
    #Perform a click python
    # pyautogui.click(clicks=1,button="PRIMARY")
    # pyautogui.doubleClick()
    # pyautogui.tripleClick()
    
    #Scroll UP
    pyautogui.scroll(500)
    
    #ScrollDown
    pyautogui.scroll(500)
    print(pyautogui.FAILSAFE)
main()