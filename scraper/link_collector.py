from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def accept_cookies(driver):
    wait = WebDriverWait(driver, 10)

    try:
        btn = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Accept')]")
            )
        )
        btn.click()
        time.sleep(2)
        print("Cookies accepted")
    except:
        print("Cookie banner not found")


def get_article_links(driver):
    driver.get("https://elpais.com")
    accept_cookies(driver)

    driver.get("https://elpais.com/opinion/")
    time.sleep(3)

    articles = driver.find_elements(By.CSS_SELECTOR, "h2 a")

    if not articles:
        articles = driver.find_elements(By.TAG_NAME, "a")

    links = []

    for a in articles:
        link = a.get_attribute("href")

        if link and "/opinion/" in link and link not in links:
            links.append(link)

    print(f"Collected {len(links)} candidate links")

    return links