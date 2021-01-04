#!/usr/bin/env python3

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from users import users


def favorite():
    for user in users:
        chrome_options = Options()

        print("Opening Browser...")

        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')

        driver = webdriver.Chrome(options=chrome_options)

        print("Requesting BR's page...")

        driver.get("https://audiomack.com/blessedray/album/prodigy-ep-vol-1")

        print("Clicking on sign in...")

        driver.find_element_by_xpath(
            '//*[@id="main-header"]/div[3]/div[2]/div/span/a[1]').click()

        email = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.NAME, "email"))
        )

        print('Entering ' + user['email'])

        if email:
            driver.find_element_by_name('email').send_keys(user['email'])

        try:
            driver.find_element_by_xpath(
                '//*[@id="am-modal"]/div[2]/div/div/div[2]/div/form/button').click()

            password = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.ID, "password"))
            )

            print("Entering " + user['username'] + "'s " + " password...")

            if password:
                driver.find_element_by_xpath(
                    '//*[@id="password"]').send_keys(user['password'])

            driver.find_element_by_xpath(
                '//*[@id="am-modal"]/div[2]/div/div/div[2]/div/div/form/div[4]/button').click()

            print("Logging in...")

            sleep(5)

            print('Adding song to favorite...')

            try:
                already = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.CLASS_NAME, "MusicActionButton-module__active--3fZrX"))
                )

                if already:
                    print("Song already added to favorite")
            except:
                try:
                    btn1 = driver.find_element_by_xpath(
                        '//*[@id="react-view"]/div[3]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[2]/ul/li/button[2]')

                    driver.execute_script("arguments[0].click();", btn1)

                    try:
                        favorite = WebDriverWait(driver, 10).until(
                            EC.visibility_of_element_located(
                                (By.CLASS_NAME, "toast-notification"))
                        )

                        if favorite:
                            print("Song added to favorite")

                    except:
                        print("Favorite toast not found")

                except expression as identifier:
                    print("Couldn't add song to favorite")

            print("Done with " + user['username'])
        except:
            print("Couldn't login")
        driver.quit()
    print("Done ✅")


favorite()
