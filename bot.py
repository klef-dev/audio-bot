from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

print("Opening Browser...")

chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

for x in range(5000):
    print("Requesting BR's page...")
    driver.get("https://audiomack.com/blessedray/album/prodigy-ep-vol-1")
    sleep(10)

    print("Trying to play song..")

    try:
        driver.find_element_by_xpath(
            '//*[@id="react-view"]/div[3]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[2]/ul/li/button[1]').click()

        print("Playing song...")
    except:
        try:
            driver.find_element_by_xpath(
                '//*[@id="react-view"]/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/button[2]/span[2]/span/span[1]').click()

            print("Playing 1 song...")

            sleep(10)

            driver.find_element_by_xpath(
                '//*[@id="react-view"]/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/button[2]/span[2]/span/span[1]').click()

            print("Playing 2 song...")

            sleep(10)

            driver.find_element_by_xpath(
                '//*[@id="react-view"]/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/div/button[2]/span[2]/span/span[1]').click()

            print("Playing 3 song...")

            sleep(10)

            driver.find_element_by_xpath(
                '//*[@id="react-view"]/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div[4]/div/button[2]/span[2]/span/span[1]').click()

            print("Playing 4 song...")

            sleep(10)

            driver.find_element_by_xpath(
                '//*[@id="react-view"]/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div[5]/div/button[2]/span[2]/span/span[1]').click()

            print("Playing 5 song...")

            sleep(10)
        except:
            print("Couldn't play song")

driver.quit()
print("Done ✅")
