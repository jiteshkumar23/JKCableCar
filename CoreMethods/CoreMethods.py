import datetime
import os
import random
import string
import tkinter as tk
from datetime import datetime
from tkinter import simpledialog
import cv2
import keyboard
import numpy as np
import pyautogui
from autoit import autoit
from pynput import mouse
import time

from config import mobileNumber, emailAddress, card_number, Month, Year, CVV, NameOnCard, machine, \
    number_of_visitors, Route, Slot, BookingType, visitDateForRegularBooking, nationality, \
    firstPersonName, secondPersonName, fifthPersonName, fourthPersonName, thirdPersonName

fifth = False
currentPerson = 0

global image_directory, visitor1_image_path, robot_image_path, check_image_path, calendar_image_path, \
    CreditCard_image_path, Tatkal_image_path, visit_time_dropdown_image_path, ticket_soldout_error_image_path,\
    CardNumber_image_path


def printDateTime():
    print(f"End time: {datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]}")


def multiplePressUsingPyAutoGUI(key, times):
    print("pressing " + " " + key + " " + str(times))
    pyautogui.press(key, presses=times)


def speed_for_first_page(speed):
    time.sleep(speed)


def wait_for_image1_or_image2_and_click(image_path, image_path2, timeout_duration=60, check_interval=0.001):
    timeout_end = time.time() + timeout_duration

    print(f"Waiting for {image_path} to appear on the screen...")

    while time.time() < timeout_end:
        try:
            # Locate the image on the screen
            location = pyautogui.locateCenterOnScreen(image_path, grayscale=True)

            # If the image is found, click on it and break the loop
            if location is not None:
                print(f"Image found at {location}, clicking on it...")
                pyautogui.click(location)
                break
        except pyautogui.ImageNotFoundException:
            # Handle the case where the image is not found
            print(f"Image not found: {image_path}")
            try:
                location = pyautogui.locateCenterOnScreen(image_path2, grayscale=True)
                if location is not None:
                    print(f"Image found at {location}, clicking on it...")
                    pyautogui.click(location)
                    break
            except pyautogui.ImageNotFoundException:
                print(f"Image not found: {image_path2}")

        # Wait for the specified interval before checking again
        time.sleep(check_interval)
    else:
        print("Timeout reached. Image not found.")

    print("Task completed.")
    return location


def wait_for_image_and_click(image_path, timeout_duration=60, check_interval=0.001):
    timeout_end = time.time() + timeout_duration

    print(f"Waiting for {image_path} to appear on the screen...")

    while time.time() < timeout_end:
        try:
            # Locate the image on the screen
            location = pyautogui.locateCenterOnScreen(image_path, grayscale=True)

            # If the image is found, click on it and break the loop
            if location is not None:
                print(f"Image found at {location}, clicking on it...")
                pyautogui.click(location)
                break
        except pyautogui.ImageNotFoundException:
            # Handle the case where the image is not found
            print(f"Image not found: {image_path}")

        # Wait for the specified interval before checking again
        time.sleep(check_interval)
    else:
        print("Timeout reached. Image not found.")

    print("Task completed.")
    return location


def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    user_input = None

    while user_input != "1":
        user_input = simpledialog.askstring("Input", "Enter 1 to continue:")
        if user_input is None:  # User closed the dialog
            print("User cancelled the input.")
            root.destroy()
            exit()

    root.destroy()  # Close the popup


def click_on_image_in_region(left, top, width, height, image):
    time.sleep(1)
    # Define the region of interest (left, top, width, height)
    region = (left, top, width, height)
    # Print debug information
    print(f"Capturing screenshot of region: {region}")

    # Capture a screenshot of the region
    screenshot = pyautogui.screenshot(region=region)

    # Print debug information
    print("Searching for image 'indian_flag.png' within the captured region...")

    try:
        # Locate the image 'indian_flag.png' within the specified region on the screen
        image_location = pyautogui.locateOnScreen(image, region=region)

        if image_location is not None:
            # Click in the center of the image location
            center = pyautogui.center(image_location)
            pyautogui.click(center)
            print("Image found and clicked.")
        else:
            print("Image not found in the specified region.")
    except pyautogui.ImageNotFoundException:
        print("Image not found on the screen.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def human_typing(text):
    for char in text:
        autoit.send(char)
        time.sleep(random.uniform(0.05, 0.15))


def human_typing_age(text):
    for char in text:
        autoit.send(char)
        time.sleep(random.uniform(0.05, 0.15))


def autoit_slow_type_with_error(text):
    if len(text) <= 4:
        for character in text:
            autoit.send(character)
            time.sleep(random.uniform(0.05, 0.2))
        return

    # Choose a few random positions to make typing errors
    num_errors = random.randint(1, 4)  # Randomly decide how many errors to make
    error_positions = random.sample(range(len(text)), num_errors)
    error_chars = string.ascii_lowercase + string.ascii_uppercase
    for i, character in enumerate(text):
        if i in error_positions:
            # Choose a random wrong character
            wrong_character = random.choice(error_chars)
            # Type the wrong random character
            autoit.send(wrong_character)
            # Backspace to delete the wrong character
            time.sleep(random.uniform(0.2, 0.5))  # Random delay for error
            autoit.send("{BACKSPACE}")
            time.sleep(random.uniform(0.2, 0.4))  # Random delay for correction
        # Type the correct character
        autoit.send(character)
        time.sleep(random.uniform(0.05, 0.2))  # Random delay for typing speed


def generate_3_random_numbers():
    return random.sample(range(1, 7), 3)


def generate_3_random_numbers_2():
    return random.sample(range(1, 7), 3)


def generate_1_random_number():
    return random.sample(range(1, 7), 1)


def random_number_between_min_and_max(min_val, max_val):
    return random.randint(min_val, max_val)


def pyautogui_slow_type_with_error(text):
    delay_correct = 0.1  # Adjust these values to fine-tune typing speed
    delay_error = 0.3

    # Choose a random position to make a typing error
    error_position = random.randint(0, len(text) - 1)
    # Choose a random alphabet as the incorrect character
    wrong_character = random.choice('abcdefghijklmnopqrstuvwxyz')

    for i, character in enumerate(text):
        if i == error_position:
            # Type the wrong random character
            pyautogui.typewrite(wrong_character)
            # Backspace to delete the wrong character
            time.sleep(delay_error)
            pyautogui.press('backspace')
            time.sleep(delay_correct)

        # Random slight delay before typing the next correct character
        random_delay = delay_correct + random.uniform(-0.05, 0.05)
        pyautogui.typewrite(character)
        time.sleep(random_delay)

        # Occasional longer pause to simulate thinking/hesitating
        if random.random() < 0.1:  # 10% chance of a pause
            time.sleep(random.uniform(0.11, 0.22))


def playback_mouse_movements(fileName):
    mouse_movements = []
    with open(fileName, 'r') as file:
        for line in file:
            mouse_movements.append(eval(line.strip()))

    # Playback the mouse movements
    controller = mouse.Controller()
    start_time = mouse_movements[0][-1]

    for movement in mouse_movements:
        action, x, y, *rest, timestamp = movement
        delay = timestamp - start_time

        # Sleep to synchronize the playback
        if delay > 0:
            time.sleep(delay)

        if action == 'move':
            controller.position = (x, y)
        elif action == 'click':
            button = mouse.Button[rest[0]]
            pressed = rest[1]
            if pressed:
                controller.press(button)
            else:
                controller.release(button)
        elif action == 'scroll':
            dx, dy = rest[0], rest[1]
            controller.scroll(dx, dy)

        start_time = timestamp


def custom_hotkey():
    # Define your desired hotkey combination
    return keyboard.is_pressed("ctrl+alt+x")  # Example: Ctrl+Alt+X


def debounce_key(key):
    # Wait for key release
    while keyboard.is_pressed(key):
        pass


def selectDateFromCalendar():
    pyautogui.click(find_image_on_screen_using_opencv(calendar_image_path, 10))
    time.sleep(0.25)
    print(days_difference_with_checkInDate(visitDateForRegularBooking))
    multiplePressUsingPyAutoGUI('right', days_difference_with_checkInDate(visitDateForRegularBooking))
    autoit.send("{ENTER}")



def firstPageFill():
    # pyautogui.click(find_image_on_screen_using_opencv(robot_image_path, 10))
    # URL Correction
    # Open this URL in a new tab if not found --https://eticket.webfront.in/jkcc/
    # pyautogui.hotkey('alt', 'k')
    # time.sleep(1)
    while True:
        if Route == "Phase 1":
            pyautogui.hotkey('alt', 'q')
        elif Route == "Phase 2":
            pyautogui.hotkey('alt', 'w')
        time.sleep(0.75)

        # Press hotkey for date selection
        if BookingType == "Tatkal":
            pyautogui.hotkey('alt', 't')
            print("Pressed alt+t for Tatkal Date Selection")
            time.sleep(0.25)
            # Select slot for Tatkal
            print("Clicking on visit time dropdown")
            pyautogui.click(find_image_on_screen_using_opencv(visit_time_dropdown_image_path, 1))
            time.sleep(0.2)
            # Check for Tatkal image and click if found
            tatkal_image = find_image_on_screen_using_opencv(Tatkal_image_path, 0.2, 0.95)
            if tatkal_image is not None:
                print("Tatkal image was found in dropdown")
                print(tatkal_image)
                pyautogui.click(tatkal_image)
                time.sleep(0.05)
                sold_out_error_message = find_image_on_screen_using_opencv(ticket_soldout_error_image_path, 0.2, 0.75)
                if sold_out_error_message is None:
                    print("Tatkal was found in dropdown and Sold out error message was Not displayed, breaking loop")
                    break  # Exit the loop if the image is found
                else:
                    print("Tatkal was found in dropdown and Sold out error message was displayed, trying again")
                    print("Press F5")
                    autoit.send("{F5}")  # Refresh the page if the image is not found
                    time.sleep(0.5)
            else:
                print("Tatkal image was NOT found")
                print("Press F5")
                autoit.send("{F5}")  # Refresh the page if the image is not found
                time.sleep(0.5)
                # Wait for a short period to allow the page to refresh
        if BookingType == "Regular":
            selectDateFromCalendar()
            time.sleep(0.25)
            # Press hotkey for Slot selection for Regular Flow
            if Slot == "Slot 1":
                pyautogui.hotkey('alt', 'y')
            if Slot == "Slot 2":
                pyautogui.hotkey('alt', 'u')
            if Slot == "Slot 3":
                pyautogui.hotkey('alt', 'i')
            break

    time.sleep(0.05)

    sold_out_error_message = find_image_on_screen_using_opencv(ticket_soldout_error_image_path, 0.2, 0.75)
    if sold_out_error_message is None:
        # Press Proceed to Next Button
        pyautogui.hotkey('alt', 'p')
        time.sleep(0.5)

        # Select Indian or Foreigner
        if nationality == "Indian":
            pyautogui.hotkey('alt', 'a')
        if nationality == "Foreigner":
            pyautogui.hotkey('alt', 's')

        time.sleep(0.5)

        # Click on Add Visitor button
        print("Start - Click on Add Visitor button")
        for _ in range(number_of_visitors - 1):
            pyautogui.hotkey('alt', 'd')
        print("End - Click on Add Visitor button")

        pyautogui.click(find_image_on_screen_using_opencv(visitor1_image_path, 10))
        # autoit.send(firstPersonName)
        print("Start - Enter Member Details")
        pyautogui.typewrite(firstPersonName)

        if number_of_visitors >= 2:
            autoit.send("{TAB 2}")
            # autoit.send(secondPersonName)
            pyautogui.typewrite(secondPersonName)
        if number_of_visitors >= 3:
            autoit.send("{TAB 2}")
            # autoit.send(thirdPersonName)
            pyautogui.typewrite(thirdPersonName)
        if number_of_visitors >= 4:
            autoit.send("{TAB 2}")
            # autoit.send(fourthPersonName)
            pyautogui.typewrite(fourthPersonName)
        if number_of_visitors >= 5:
            autoit.send("{TAB 2}")
            # autoit.send(fifthPersonName)
            pyautogui.typewrite(fifthPersonName)
        print("End - Enter Member Details")

        # Enter mobile number
        print("Start - Enter Mobile Number")
        autoit.send("{TAB 2}")
        # autoit.send(mobileNumber)
        pyautogui.typewrite(mobileNumber)
        print("End - Enter Mobile Number")

        # Enter Email
        print("Start - Enter Email")
        autoit.send("{TAB}")
        # autoit.send(emailAddress)
        pyautogui.typewrite(emailAddress)
        time.sleep(0.5)
        print("End - Enter Email")

        # Press Checkbox
        print("Start - Click Capcha Checkbox")
        autoit.send("{TAB}")
        time.sleep(0.1)
        autoit.send("{ENTER}")
        print("End - Click Capcha Checkbox")

        # Press Proceed to Pay Button
        print("wait for capcha to clear and check image to appear")
        pyautogui.click(find_image_on_screen_using_opencv(check_image_path, 60))
        print("Capcha is cleared , check has appeared")
        print("Start - Click Proceed to Pay Button")
        time.sleep(1)
        autoit.send("{TAB 3}")
        autoit.send("{ENTER}")
        print("End - Click Proceed to Pay Button")
        makePayment()

    else:
        print("Sold Out Error message was displayed")


def makePayment():
    pyautogui.click(find_image_on_screen_using_opencv(CreditCard_image_path, 60))
    pyautogui.click(find_image_on_screen_using_opencv(CardNumber_image_path, 60))
    autoit.send("{TAB}")
    autoit.send(card_number)
    time.sleep(0.2)
    autoit.send(Month)
    time.sleep(0.2)
    autoit.send(Year)
    time.sleep(0.2)
    autoit.send(CVV)
    time.sleep(0.2)
    autoit.send(NameOnCard)
    autoit.send("{TAB}")
    autoit.send("{ENTER}")

def find_image_on_screen_using_opencv(template_path1, timeout, threshold=0.5):
    template = cv2.imread(template_path1, 0)
    w, h = template.shape[::-1]
    start_time = time.time()

    while True:
        # Capture a screenshot
        screenshot = pyautogui.screenshot()

        # Convert screenshot to numpy array and then to grayscale
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

        # Perform template matching
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # Check if the match value is above the threshold
        if max_val >= threshold:
            # Return the location of the matched region
            return max_loc[0], max_loc[1], w, h

        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            return None

        time.sleep(0.5)


def setImagePath():
    global image_directory
    if machine == "laptop":
        image_directory = os.getcwd() + '\\images_laptop'
    elif machine == "desktop":
        image_directory = os.getcwd() + '\\images_desktop'

    global robot_image_path
    robot_image_path = os.path.join(image_directory, 'robot.png')

    global check_image_path
    check_image_path = os.path.join(image_directory, 'check.png')

    global calendar_image_path
    calendar_image_path = os.path.join(image_directory, 'calendar.png')

    global visitor1_image_path
    visitor1_image_path = os.path.join(image_directory, 'visitor1.png')

    global CreditCard_image_path
    CreditCard_image_path = os.path.join(image_directory, 'CreditCard.png')

    global Tatkal_image_path
    Tatkal_image_path = os.path.join(image_directory, 'Tatkal.png')

    global visit_time_dropdown_image_path
    visit_time_dropdown_image_path = os.path.join(image_directory, 'visit_time_dropdown.png')

    global ticket_soldout_error_image_path
    ticket_soldout_error_image_path = os.path.join(image_directory, 'ticket_soldout_error.png')

    global CardNumber_image_path
    CardNumber_image_path = os.path.join(image_directory, 'CardNumber.png')

def check_current_month(checkInDatePassed):
    input_month = datetime.strptime(checkInDatePassed, "%Y-%m-%d").month
    current_month = datetime.now().month
    return input_month == current_month


def days_difference_with_checkInDate(checkInDate):
    # Get the current date and time
    current_date = datetime.now()

    # Parse checkOutDate
    checkInDate = datetime.strptime(checkInDate, "%Y-%m-%d")

    # Calculate the difference in days between the current date and the checkOutDate
    difference_in_days = abs((checkInDate - current_date).days)
    difference_in_days = difference_in_days + 1
    print(f"Difference in days: {difference_in_days}")
    return difference_in_days


def days_difference_with_checkInDate_checkOutDate(checkInDate1, checkOutDate1):
    # Convert strings to datetime objects if they aren't already
    if isinstance(checkInDate1, str):
        checkInDate1 = datetime.strptime(checkInDate1, "%Y-%m-%d")
    if isinstance(checkOutDate1, str):
        checkOutDate1 = datetime.strptime(checkOutDate1, "%Y-%m-%d")

    # Calculate the difference in days and ensure it's positive
    difference_in_days = abs((checkOutDate1 - checkInDate1).days) - 1
    return difference_in_days


def find_any_of_two_images_on_screen_using_opencv(template_path1, template_path2, timeout, threshold=0.7):
    template1 = cv2.imread(template_path1, 0)
    template2 = cv2.imread(template_path2, 0)
    w1, h1 = template1.shape[::-1]
    w2, h2 = template2.shape[::-1]
    start_time = time.time()

    while True:
        # Capture a screenshot
        screenshot = pyautogui.screenshot()
        # Convert screenshot to numpy array and then to grayscale
        screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)

        # Perform template matching for the first image
        res1 = cv2.matchTemplate(screenshot, template1, cv2.TM_CCOEFF_NORMED)
        min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(res1)

        # Perform template matching for the second image
        res2 = cv2.matchTemplate(screenshot, template2, cv2.TM_CCOEFF_NORMED)
        min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(res2)

        # Check if the first image match value is above the threshold
        if max_val1 >= threshold:
            # Take action for the first image
            return ("Image 1", max_loc1[0], max_loc1[1], w1, h1)

        # Check if the second image match value is above the threshold
        if max_val2 >= threshold:
            # Take action for the second image
            return ("Image 2", max_loc2[0], max_loc2[1], w2, h2)

        # Check if the timeout has been reached
        if time.time() - start_time > timeout:
            return None

        time.sleep(0.1)
