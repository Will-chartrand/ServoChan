import time
import RPi.GPIO as GPIO
from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True

#Set GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT) #pin 11 used for servo 1
servo1 = GPIO.PWM(11,50)

servo1.start(0)


browser = webdriver.Firefox(options=options)

browser.implicitly_wait(5)


browser.get('https://www.instagram.com/')
print("on login page")

#login_link = browser.find_element_by_xpath("//a[text()='Log in']")

#login_link.click()

browser.implicitly_wait(10)

sleep(4)


username_input = browser.find_element_by_css_selector("input[name='username']")

password_input = browser.find_element_by_css_selector("input[name='password']")


username_input.send_keys("<put username here>")

password_input.send_keys("<put password here>")

print("username and password input")
login_button = browser.find_element_by_xpath("//button[@type='submit']")

login_button.click()

browser.implicitly_wait(8)

profile_link = browser.find_element_by_class_name("_6q-tv")
#_6q-tv
profile_link.click()

browser.implicitly_wait(8)

prof_bar = browser.find_element_by_class_name("-qQT3")
#-qQT3
prof_bar.click()

browser.implicitly_wait(8)

print("on profile")
followers = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").get_attribute("title")
prevFollowers = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span").get_attribute("title")

#you can make this loop infinite, it doesn't really matter
while(followers < 1000):
    browser.implicitly_wait(10)
    sleep(10)
    prevFollowers = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span"))).get_attribute("title")   
    
    print("followers:", end="")
    print(prevfollowers)

    if(followers != prevFollowers):
        servo1.ChangeDutyCycle(12)
        sleep(2)
        servo1.ChangeDutyCycle(0)
        
        sleep(1)

        servo1.ChangeDutyCycle(2)
        sleep(2)
        servo1.ChangeDutyCycle(0)
        

    followers = prevFollowers
    browser.refresh()


browser.close()

servo1.stop()
GPIO.cleanup()

print("program finished")
