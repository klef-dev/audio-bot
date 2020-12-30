from selenium import webdriver
from time import sleep, time
import concurrent.futures


def audiomack(nothing):
    print("Opening Browser...")

    driver = webdriver.Chrome()
    print("Requesting BR's page...")
    driver.get("https://audiomack.com/blessedray/album/prodigy-ep-vol-1")
    sleep(2)

    print("Trying to play song..")

    driver.find_element_by_xpath(
        '//*[@id="react-view"]/div[3]/div/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[2]/ul/li/button[1]').click()

    print("Playing song...")
    sleep(2)


with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for x in range(10):
        futures.append(executor.submit(
            audiomack, nothing=x))
