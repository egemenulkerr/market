from selenium import webdriver
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Keys, ActionChains
from time import sleep
import datetime

sayac = 0
simdi = datetime.datetime.now() #süre hesaplamka için

opsiyonlar = Options()
opsiyonlar.add_argument("--headless")  # arka planda çalışması için
browser = webdriver.Firefox(opsiyonlar)

browser.get("https://www.a101.com.tr/ekstra")
sleep(5)

#çerezleri kabul ediyor
browser.find_element(By.XPATH, '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]').click()

#giyim & aksesuar kategorisini seçiyor
browser.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div[4]/div/div/div/div/div/a[3]/span').click()
sleep(2)

#boşluğa tıklıyor
el = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[1]/div/div/div[7]/div/div")
action = webdriver.common.action_chains.ActionChains(browser)
action.move_to_element_with_offset(el, 30, 30)
action.click()
#action.perform() , hheadless opsiyonu kullanılmıyorken açılması gerekiyor

for j in range(56):

    try:
        if j == 0:
            sleep(1)

        for i in range(51):
            new_amount = browser.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[2]/div[3]/div[2]/div[3]/ul/div[%i]/div/a/section/span[2]' % ((52 * j)+(i + 1))).text
            print(new_amount)

            sayac += 1
            print(sayac)

            if i % 4 == 0:
                footer = browser.find_element(By.XPATH,
                "/html/body/div[3]/div/div[2]/div[4]/div/div/div/div/div/a[8]")
                scroll_origin = ScrollOrigin.from_element(footer, 0, -40)
                ActionChains(browser).scroll_from_origin(scroll_origin, 0, 385).perform()
            if (i != 0) and (i % 50) == 0:
                sleep(1)
    except:
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


bitis = datetime.datetime.now()
print(sayac)
print(bitis - simdi)