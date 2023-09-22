import serial
import pyautogui
import keyboard
Arduino_Serial = serial.Serial('COM3', 9600)
#Exchange the COM3 with your arduino's port

while 1:
    incoming_data = str(Arduino_Serial.readline())
    print(incoming_data)
#     if 'pressA' in incoming_data:
#         pyautogui.press('a')
#     incoming_data = ""
#     if 'pressD' in incoming_data:
#         pyautogui.press('d')
#     incoming_data = ""
#     if 'pressW' in incoming_data:
#         pyautogui.press('w')
#     incoming_data = ""
#     if 'pressS' in incoming_data:
#         pyautogui.press('s')
#     incoming_data = ""

    if "Axis X" in incoming_data and "Axis Y" in incoming_data:
        # Parse sensor incoming_data
        x_value = int(incoming_data.split("Axis X = ")[1].split("  Axis Y")[0])
        y_value = int(incoming_data.split("Axis Y = ")[1].split("  Axis Z")[0])

        # Simulate keyboard presses based on sensor data
        keyboard.release('left')  # Release 'Left Arrow' key
        keyboard.release('right')  # Release 'Right Arrow' key
        keyboard.release('down')  # Release 'Down Arrow' key
        keyboard.release('up')  # Release 'Up Arrow' key

        if x_value < 110:
            keyboard.press('right')  # Press 'Left Arrow' key
        elif x_value > 140:
            keyboard.press('left')  # Press 'Right Arrow' key

        if y_value > 150:
            keyboard.press('up')  # Press 'Down Arrow' key
        elif y_value < 110:
            keyboard.press('down')  # Press 'Up Arrow' key
