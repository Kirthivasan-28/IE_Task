from venv import create
from selenium import webdriver
from selenium.webdriver.common.by import By
from csv import DictWriter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException

lst =[]
data = {}
driver = webdriver.Chrome(executable_path="C:\\Users\\Kirthi\\Downloads\\IE Task\\chromedriver.exe")
driver.maximize_window()
url="https://hub.jhu.edu/events/?pg="
pg_count=1
count = 1
condition=1
while condition:
    try:
        driver.get(url+str(pg_count))
        date_lst = driver.find_elements(By.XPATH,"(//div[@class='meta date'])")
        for i in date_lst:
            data["header"] = driver.find_element(By.XPATH,"(//h5)["+str(count)+"]").text
            data["date"] = i.text
            data["url"] = driver.find_element(By.XPATH,"(//h5//a)["+str(count)+"]").get_attribute("href")
            lst.append(data.copy())
            ele = driver.find_element(By.XPATH,"//a[@class='next button x-small']")
            driver.implicitly_wait(10)
            count=count+1
        pg_count=pg_count+1
        count=1
    except Exception as e:
        print(len(lst))
        print(lst)
        condition=0



with open('Book1.csv','w') as outfile:
    writer = DictWriter(outfile, ('header','date','url'))
    writer.writeheader()
    writer.writerows(lst)