from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import warnings
import pymysql
from datetime import date
import random

trnd = random.randint(6, 22)

dt_now = date.today()

warnings.filterwarnings("ignore", category=DeprecationWarning)

connection = pymysql.connect(host="localhost", port=3306, user="XXXXX", passwd="XXXXX", database="new_tokens")
cursor = connection.cursor()

url = 'https://poocoin.app/ape'

driver = webdriver.Chrome('./chromedriver')

driver.get(url)

driver.implicitly_wait(5)

fe = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/label/select/option[2]')

cq = fe.click()

time.sleep(15)

table_labels = []

tb1 = driver.find_elements_by_xpath('//*[@id="root"]/div/div/div[3]/div/table/thead/tr/th')

ln = 0

while ln < 11:
    print(str(dt_now) + " - LOOP: " + str(ln))
    ln += 1
    tkName = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/table/tbody/tr[' + str(ln) + ']/td[1]/a')
    creat_time = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/table/tbody/tr[' + str(ln) + ']/td[2]')
    sc_add = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/table/tbody/tr[' + str(ln) + ']/td[3]/div[1]/a[1]')
    n_holders = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[3]/div/table/tbody/tr[' + str(ln) + ']/td[3]/div[1]/a[2]')
    tn = tkName.text
    ct = creat_time.text
    sca = sc_add.get_attribute('href')
    nh = n_holders.get_attribute('href')
    vls = [(dt_now), (tn), (ct), (sca), (nh)]
    ist = "INSERT INTO collected(date, name, created_in, sc_address, holders) VALUES (%s, %s, %s, %s, %s);"
    cursor.execute(ist, vls)
    connection.commit()
    print("TOKEN NAME: " + str(tn))
    print("CREATION TIME: " + str(ct))
    print("SMART CONTRACT ADD: " + str(sca))
    print("HOLDERS NUMBER: " + str(nh))
    print(" ")
    time.sleep(2)
    if ln == 11:
        ln = 0
        print("sleep...")
        time.sleep(3600)
    else:
        continue

connection.close()
driver.close()
