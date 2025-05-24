from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Keys
from time import sleep
import datetime

simdi = datetime.datetime.now()


opsiyonlar = Options()
opsiyonlar.add_argument("--headless")  # arka planda çalışması için
browser = webdriver.Firefox()

browser.get("https://www.a101.com.tr/ekstra")
sleep(5)

browser.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()
browser.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/div[4]/div/div/div/div/div/a[3]/span').click()

for j in range(48):
    if j == 0:
        sleep(1)
    sleep(0.05)
    try:
        for i in range(56):
            new_amount = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[3]/div[2]/div[3]/ul/div[i]/div/a/section/span[2]' % (i + 1)).text
            print(new_amount)
            product_name = browser.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[2]/div[3]/div[2]/div[3]/ul/div[i]/div/a/div/header/hgroup/h3' % (i + 1)).text
            print(product_name)
        try:
            browser.sendKeys(Keys.PAGE_DOWN)
        except :
            continue
    except:
        print("XXX")