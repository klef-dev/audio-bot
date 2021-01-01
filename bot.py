from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from pyvirtualdisplay import Display

display = Display(visible=0, size=(800, 800))  
display.start()

for x in range(5000):
    chrome_options = Options()

    print("Opening Browser...")

    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1420,1080')
    chrome_options.binary_location = '/opt/google/chrome/google-chrome'

    driver = webdriver.Chrome(options=chrome_options)

    print("Requesting BR's page...")

    driver.get("https://audiomack.com/blessedray/album/prodigy-ep-vol-1")

    print("Trying to play song..")

    try:
        btn1 = driver.find_element_by_xpath(
            '//*[@id="react-view"]/div[3]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[2]/ul/li/button[1]')

        driver.execute_script("arguments[0].click();", btn1)

        try:
            paused = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "play-button--paused"))
            )

            if paused:
                driver.find_element_by_xpath(
                    '//*[@id="react-view"]/div[7]/div/div[1]/button[2]').click()
        except:
            pass

        playing = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "play-button--playing"))
        )

        print("Playing 1 song...")

        sleep(2)

        print("Done with ", format(x+1))
    except:
        print("Couldn't play song")
    driver.quit()
print("Done ✅")
