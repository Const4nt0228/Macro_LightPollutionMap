from selenium import webdriver
from bs4 import BeautifulSoup
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

a = []

dataset2 = pd.read_csv('rootkey.csv')
driver = webdriver.Chrome()
url = "https://www.lightpollutionmap.info/#zoom=6.17&lat=35.9759&lon=127.1135&layers=B0FFFFFFFTFFFFFFFFFFF"
driver.get(url)

time.sleep(2)

x_path0 = '//*[@id="CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"]'
x_path1 = '//*[@id="searchBox"]'

# cookiebox = driver.find_element_by_xpath(x_path0)
cookiebox = driver.find_element(By.XPATH, x_path0)
cookiebox.click()

# 여기서 반복문이 이뤄져야함

dataset2 = pd.read_csv('rootkey.csv')
# print(str(dataset2.x.values[0]))
i = 0

for k in dataset2.x.values:
    # print(dataset2.x.values[i])
    # searchWeb.searchUseXY(str(dataset2.x.values[i]), str(dataset2.y.values[i]))

    print(i)
    print(dataset2.x.values[i])
    x = str(dataset2.x.values[i])
    y = str(dataset2.y.values[i])
    print("x, y = ", x, y)

    # time.sleep(0.2)

    # searchbox = driver.find_element_by_xpath(x_path1)
    searchbox = driver.find_element(By.XPATH, x_path1)
    searchbox.click()

    #  element = driver.find_element_by_id("searchBox")
    element = driver.find_element(By.ID, "searchBox")

    # element.send_keys("6,8" + Keys.ENTER)

    element.send_keys(x + ',' + y + Keys.ENTER)
    element.clear()

    # time.sleep(2.5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    sc6 = soup.select('.tableCellValues')

    if not sc6:
        print('empty')
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        sc6 = soup.select('.tableCellValues')

    # print(sc6)
    print(sc6[1].text[0:5])

    # a.append(sc6[1].text[0:5])
    # ax.append(dataset2.x.values[i])
    # ay.append(dataset2.y.values[i])

    a.append(sc6[1].text[0:5])

    i = i + 1

# print(a)

# csv로 내보내는 과정
## dateframe 으로 만든뒤 output
raw_data = {
    'x': dataset2.x.values,
    'y': dataset2.y.values,
    'SQM': a
}
csv_data = pd.DataFrame(raw_data)
print(csv_data)

csv_data.to_csv("sqmResult.csv", mode='w')

driver.quit()
