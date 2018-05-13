#-*- coding: UTF-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def menu():
	print(10 * "-", "MENU", 10 * "-")
	print("1. Get Satellite Image")
	print("2. Exit")

loop = True

while loop:
	menu()
	choice = input("\nEnter your choice [1-2]: ")
	choice = int(choice)

	if choice == 1:
		print("\n")
		latitude = input("Enter the latitude, for example 41.008469\n:")
		longitude = input("Enter the longitude, for example 28.980261\n:")
		
		url = "https://www.google.com/maps/@{},{},18z".format(latitude, longitude)
		url2 = "https://www.google.com/maps/@{},{},349m/data=!3m1!1e3".format(latitude, longitude)

		print("\nWill grab the satellite image from: " + "'" + "google.com/maps/@" + latitude + "," +  longitude + "'" )
		
		options = Options()
		options.set_headless(headless=True) 
		driver = webdriver.Firefox(firefox_options=options)
		driver.set_window_size(1920, 1080)
		driver.get(url)
		time.sleep(1)

		delete_button = driver.execute_script("""
			var element = document.querySelector("#omnibox");
			if (element)
			element.parentNode.removeChild(element);""")

		sc = driver.find_element_by_css_selector('body')
		sc.screenshot(latitude + "," + longitude + ".png")
		driver.quit()

		driver = webdriver.Firefox(firefox_options=options)
		driver.set_window_size(1920, 1080)
		driver.get(url2)
		time.sleep(1)

		delete_button = driver.execute_script("""
			var element = document.querySelector("#omnibox");
			if (element)
			element.parentNode.removeChild(element);""")

		sc = driver.find_element_by_css_selector('body')
		sc.screenshot(latitude + "," + longitude + ",2" + ".png")
		driver.quit()
		print("\nDone!")

	elif choice == 2:
		print("\nSee you next time!")
		quit()

	else:
		input("Wrong selection.\nPlease try again.")