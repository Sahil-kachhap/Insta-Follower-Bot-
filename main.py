from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
similar_account = "Write username of the insta page as per your interst/ hobby , Like any food or vlog page."
Username = "Write Your Insta Username here"
Password = "Write Your Insta Password here"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")  # Opens Insta login page
        time.sleep(5)  # A time delay to observe the automation

        # finds username input field in the login page
        username = self.driver.find_element_by_name("username")

        # finds password input field in login page
        password = self.driver.find_element_by_name("password")

        username.send_keys(Username)  # enters username in the input field
        password.send_keys(Password)  # enters password in the password field

        time.sleep(2)  # A time delay to observe the automation
        password.send_keys(Keys.ENTER)  # Press the submit button

    def find_followers(self):
        time.sleep(5)  # A time delay to observe the automation
        self.driver.get(f"https://www.instagram.com/{similar_account}")  # Search for your favorite insta page

        time.sleep(2)  # A time delay to observe the automation
        followers = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')  # Find Followers element on the page
        followers.click()  # Tap on Followers button

        time.sleep(2)  # A time delay to observe the automation
        modal = self.driver.find_element_by_xpath(
            '/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[3]/button')  # Checkout the Popup Consisting of Followers list
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)  # A time delay to observe the automation

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()

# driver.quit()
