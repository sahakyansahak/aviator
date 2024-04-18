from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
import csv

opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(executable_path="chromedriver_win32/chromedriver.exe", chrome_options=opt)
start = True
data_list = []
DATA_LEN = 1
#driver.get("http://fb.com")



while True:
    if start:
        last_num = driver.find_element_by_xpath("/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[1]/div/app-payout-item[1]/div").get_attribute("innerHTML")
        last_num = last_num[:-2]
        while float(last_num) < 2.0:
            last_num = driver.find_element_by_xpath("/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[1]/div/app-payout-item[1]/div").get_attribute("innerHTML")
            last_num = last_num[:-2]
        start = False
    if len(data_list) == DATA_LEN:
        bet_btn = driver.find_element_by_xpath("/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[1]/div[2]/button")
        bet_btn.click()
        curr_num = driver.find_elements_by_xpath("/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[2]/app-play-board/div/div[2]/app-dom-container/div/div[2]/app-payout-coefficient/div")
        while len(curr_num) == 0:
            curr_num = driver.find_elements_by_xpath("/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[2]/app-play-board/div/div[2]/app-dom-container/div/div[2]/app-payout-coefficient/div")
        try:
            while curr_num[0].get_attribute("innerHTML") == "":
                curr_num = driver.find_elements_by_xpath("/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[2]/app-play-board/div/div[2]/app-dom-container/div/div[2]/app-payout-coefficient/div")
            try:
                while float(curr_num[0].get_attribute("innerHTML")[:-1]) < 2.00:
                    curr_num = driver.find_elements_by_xpath("/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[2]/app-play-board/div/div[2]/app-dom-container/div/div[2]/app-payout-coefficient/div")
                cash_btn = driver.find_element_by_xpath("/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[3]/app-bet-controls/div/app-bet-control[1]/div/div[1]/div[2]/button")
                cash_btn.click()
            except: print("Flow")
  
        except: print("Verry soon Flow")
    data = None
    num = driver.find_elements_by_xpath("/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[2]/app-play-board/div/div[2]/app-dom-container/div/div[2]/div[2]")
    while len(num) == 0: 
        num = driver.find_elements_by_xpath("/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[2]/app-play-board/div/div[2]/app-dom-container/div/div[2]/div[2]")
    data = float(num[0].get_attribute("innerHTML")[:-1])
    with open(r'data_all.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([data])
    if data < 2.0 or len(data_list) > DATA_LEN - 1:
        data_list.append(data)
    else: data_list.clear()
    if len(data_list) > DATA_LEN:
        with open(r'data.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(data_list)
            data_list.clear()
    print(data, data_list) 
    while len(num) != 0: 
        num = driver.find_elements_by_xpath("/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[2]/app-play-board/div/div[2]/app-dom-container/div/div[2]/div[2]")
     

print("This is test")
print("This is test2")
print("This is master")
print("This is test3")