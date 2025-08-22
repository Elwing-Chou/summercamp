import undetected_chromedriver as uc
import time
import re
import urllib.parse as parse
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    driver = uc.Chrome(use_subprocess=False)
    driver.get('https://www.google.com/')
    driver.maximize_window()
    # 找到元素->點/輸入/捲動
    e = driver.find_element(By.CLASS_NAME, "gLFyf")
    # click() 滑鼠點 send_keys() 鍵盤輸入
    e.send_keys("吉伊卡哇")
    e.send_keys(Keys.ENTER)

    # 找第二個[1]做點及
    time.sleep(3)
    e = driver.find_elements(By.CLASS_NAME, "C6AK7c")[1]
    e.click()

    # 找到所有圖片的超連結
    time.sleep(3)
    elist = driver.find_elements(By.CLASS_NAME, "ob5Hkd")
    for e in elist:
        try:
            # 因為剛拿a的時候他還沒有超連結
            # 故意先點他一下讓他產生他的超連結
            # 拿超連結(get_attribute("href"))
            link = e.find_element(By.TAG_NAME, "a")
            link.click()
            # time.sleep(0.5)
            href = link.get_attribute("href")
            result = re.search("imgurl=(.*(jpg|jpeg|gif|png|webp))", href)
            imgurl = parse.unquote(result.group(1))
            print(imgurl)
        except:
            print("這個放棄")

    time.sleep(5)
    driver.quit()