import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://map.naver.com/v5/search/"
CHROMEDRIVERPATH = "/usr/bin/chromedriver"

# DB_HOST = "localhost"
# DB_USER = "sf-user"
# DB_PW = "A4q8EEdh3c"

def initSelenium(executable_path):
    options = Options()
    options.add_argument('--headless')
    #options.add_argument('--window-size=1920x1080')
    #options.add_argument("--disable-gpu")
    options.add_argument("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    service = Service(executable_path=executable_path)
    return webdriver.Chrome(service=service, options=options)

if __name__ == '__main__':
    driver = initSelenium(CHROMEDRIVERPATH)
    driver.get("https://sauce.foodpolis.kr/home/specialty/foodDbSearch.do?PAGE_MN_ID=SIS-030101")

    # connect = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PW, charset='utf8')
    # cur = connect.cursor()
    # cur.execute("USE SelectFood")

    with open("tags.txt", "w") as out:
        for i in range(2, 413):
            for j in range(1, 12):
                out.write(driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/table/tbody/tr[' + str(j) + ']/td[2]/a').get_attribute("innerText") + "\n")
                # cur.execute("insert ignore into Ingredient (name) values (%s);", 
                #             (driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/table/tbody/tr[' + str(j) + ']/td[2]/a').get_attribute("innerText")))
            driver.execute_script("fn_select(" + str(i) + ");")

    # cur.execute("commit")

