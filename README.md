# AsusF11
Make your Asus laptop's F11 key turn on/off the display, instead of taking a screenshot. **OLED ONLY**

## Requirments
- Python
- Microsoft PowerToys or AHK(If you are willing to figure the maping by yourself)
- Keyboard&pyautogui libraries
## Setup
- Download PowerToys from http://github.com/microsoft/powertoys
- In Powertoys, go to Keyboard Manager and in remap shortcuts, map win+shift+s to Run program > python executable location > args: location of python file(in this repo)
- Download the python file in this repo, and put the path in args of powertoys keyboard mapping

## Downsides to using this
- Asus hardwires the F11 key to win+shift+s, which is a windows shortcut to take a screenshot. So with this script, you won't be able to use win+shift+s. You can use the Prt Sc Key instead
- PowerToys / AHK must be running in the backround
- Sometimes acts weird, so use alt+f4, or alt tab and click on X to quit
