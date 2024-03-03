from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

driver_path = r"C:\My stuff\Useful Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
urls_to_scrape = [
    "https://www.sunglasshut.com/au/womens-sunglasses?orderBy=3",
    "https://www.sunglasshut.com/au/womens-sunglasses?orderBy=4"
]


def scrape_sunglasses():
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)

    product_info = []

    for url in urls_to_scrape:
        driver.get(url)

        while True:
            try:
                load_more_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'sgh-load-more__button')))
                load_more_button.click()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'sgh-load-more__button')))
            except:
                break

        product_containers = driver.find_elements(By.CLASS_NAME, 'sgh-tile.container')

        for article in product_containers:
            article_info = {'data': article.find_element(By.CLASS_NAME, 'sgh-tile__badge-container').text,
                            'photo url': article.find_element(By.TAG_NAME, 'img').get_attribute('data-src')}
            product_info.append(article_info)
        time.sleep(5)

    driver.quit()
    return pd.DataFrame(product_info)
