from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print("Opening Browser...")

driver = webdriver.Chrome()

for x in range(5000):
    print("Requesting BR's page...")
    driver.implicitly_wait(10)
    driver.get("https://audiomack.com/blessedray/album/prodigy-ep-vol-1")
    sleep(10)

    print("Trying to play song..")

    # try:

    btn1 = driver.find_element_by_xpath(
        '//*[@id="react-view"]/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/button[2]')

    driver.execute_script("arguments[0].click();", btn1)

    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "play-button--playing"))
    )

    print("Playing 1 song...")

    sleep(5)

    btn2 = driver.find_element_by_xpath(
        '//*[@id="react-view"]/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/button[2]')

    driver.execute_script("arguments[0].click();", btn2)

    WebDriverWait(driver, 60).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "play-button--playing"))
    )

    print("Playing 2 song...")

    sleep(5)
    # except:
    #     print("Couldn't play song")

driver.quit()
print("Done ✅")
