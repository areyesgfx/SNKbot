# Test Id - 32513264779469
# Sizing ID's
# 8.5 - 37419272437965
# 13 - 37419272700109
import json
import requests
import pyautogui
import tkinter as tk
from tkinter import filedialog, Text
import os
from selenium import webdriver
import time

# ---------------------------GUI-------------------------------

HEIGHT = 720
WIDTH = 1366
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='vader.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# ----------------- Personal Information Entry's -----------------

entry1 = tk.Entry(root, bg='#63636b')
canvas.create_window(243, 220, window=entry1, width=303, height=30)

entry2 = tk.Entry(root, bg='#63636b')
canvas.create_window(243, 277, window=entry2, width=303, height=30)

entry3 = tk.Entry(root, bg='#63636b')
canvas.create_window(243, 334, window=entry3, width=303, height=30)

entry4 = tk.Entry(root, bg='#63636b')
canvas.create_window(243, 391, window=entry4, width=303, height=30)

entry5 = tk.Entry(root, bg='#63636b')
canvas.create_window(243, 448, window=entry5, width=303, height=30)

entry6 = tk.Entry(root, bg='#63636b')
canvas.create_window(144, 504, window=entry6, width=105, height=30)

entry7 = tk.Entry(root, bg='#63636b')
canvas.create_window(341, 504, window=entry7, width=105, height=30)

entry8 = tk.Entry(root, bg='#63636b')
canvas.create_window(243, 562, window=entry8, width=303, height=30)

entry9 = tk.Entry(root, bg='#63636b')
canvas.create_window(1117, 292, window=entry9, width=303, height=30)

entry10 = tk.Entry(root, bg='#63636b')
canvas.create_window(1117, 355, window=entry10, width=303, height=30)

entry11 = tk.Entry(root, bg='#63636b')
canvas.create_window(1018, 407, window=entry11, width=105, height=30)

entry12 = tk.Entry(root, bg='#63636b')
canvas.create_window(1215, 407, window=entry12, width=105, height=30)

entry13 = tk.Entry(root, bg='#63636b')
canvas.create_window(1117, 555, window=entry13, width=303, height=30)

def checkout_process():
    size = entry13.get()
    driver = webdriver.Chrome(executable_path=r'/Users/antonioreyes1/Documents/chromedriver')
    driver.get('http://shopnicekicks.com/cart/' + str(size) + ':1')

    # Enter Email
    email = entry1.get()
    driver.find_element_by_xpath('//input[@placeholder="Email"]').send_keys(email)
    time.sleep(0.05)

    # Enter First Name
    first_name = entry2.get()
    driver.find_element_by_xpath('//input[@placeholder="First name"]').send_keys(first_name)
    time.sleep(0.05)

    # Enter Last Name
    last_name = entry3.get()
    driver.find_element_by_xpath('//input[@placeholder="Last name"]').send_keys(last_name)
    time.sleep(0.05)

    # Enter Address
    address = entry4.get()
    driver.find_element_by_xpath('//input[@placeholder="Address"]').send_keys(address)
    time.sleep(0.05)

    # Enter Apt, Suite, Unit, ETC...
    apt = entry5.get()
    driver.find_element_by_xpath('//input[@placeholder="Apartment, suite, etc. (optional)"]').send_keys(apt)
    time.sleep(0.05)

    # Enter City
    city = entry6.get()
    driver.find_element_by_xpath('//input[@placeholder="City"]').send_keys(city)
    time.sleep(0.05)

    # Enter Zip Code
    zip = entry7.get()
    driver.find_element_by_xpath('//input[@placeholder="ZIP code"]').send_keys(zip)
    time.sleep(0.05)

    # Enter Phone Number
    phone = entry8.get()
    driver.find_element_by_xpath('//input[@placeholder="Phone"]').send_keys(phone)
    time.sleep(0.05)

    # Click I agree to Terms & Conditions
    driver.find_element_by_id('i-agree__checkbox').click()
    time.sleep(0.05)

    # Continue to Next Page
    driver.find_element_by_id('continue_button').click()
    time.sleep(1)

    # Continue to Next Page
    driver.find_element_by_id('continue_button').click()
    time.sleep(1)

    # Enter Card Number
    card_number = entry9.get()
    pyautogui.click(200, 760)
    pyautogui.typewrite(card_number)
    time.sleep(0.03)

    card_name = entry10.get()
    pyautogui.click(200, 800)
    pyautogui.typewrite(card_name)
    time.sleep(0.03)

    exp_date = entry11.get()
    pyautogui.click(200, 870)
    pyautogui.typewrite(exp_date)
    time.sleep(0.03)

    cvv = entry12.get()
    pyautogui.click(550, 870)
    pyautogui.typewrite(cvv)
    time.sleep(0.03)

    # Click Paypal as Payment Method
    #driver.find_element_by_id('checkout_payment_gateway_3487187').click()
    #time.sleep(0.05)

    # Complete Order
    driver.find_element_by_id('continue_button').click()


# ------------------------ Button -------------------------

button = tk.Button(fg='black', text="Start", command=checkout_process)
canvas.create_window(685, 650, window=button, width=175, height=100)



root.mainloop()



