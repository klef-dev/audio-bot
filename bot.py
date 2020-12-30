from selenium import webdriver
from time import sleep

print("Opening Browser...")

driver = webdriver.Chrome()

for x in range(5000):
    print("Requesting BR's page...")
    driver.get("https://audiomack.com/blessedray/album/prodigy-ep-vol-1")
    sleep(2)

    print("Trying to play song..")

    driver.find_element_by_xpath(
        '//*[@id="react-view"]/div[3]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[2]/ul/li/button[1]').click()

    print("Playing song...")
    sleep(2)

driver.close()
print("Done ✅")
