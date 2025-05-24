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

browser.get("https://www.migros.com.tr/")
sleep(0.2)
arama_kutusu = browser.find_element(By.ID, "product-search-combobox--trigger")
arama_kutusu.send_keys("kişisel bakım")
arama_kutusu.send_keys(Keys.ENTER)

sayac = 0

for j in range(60):

    if j == 0:
        sleep(0.3)

    sleep(0.1)

    try:
        for i in range(30):
            new_amount = browser.find_element(By.XPATH, '(//*[@id="new-amount"])[%i]' % (i + 1)).text
            print(new_amount)
            sayac += 1
        try:
            browser.find_element(By.XPATH, '//*[@id="pagination-button-next"]').click()
        except :
            print("YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY")
    except:
        browser.find_element(By.XPATH, '//*[@id="pagination-button-next"]').click()


bitis = datetime.datetime.now()
print(bitis-simdi)
print(sayac)