import pyautogui

location = pyautogui.locateOnScreen('google_image.png', confidence=0.9)

# Check if the image was found on the screen
if location:
    print("Image found on screen at:", location)
else:
    print("Image not found on screen")
