from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def scrape_article(driver, url, index):
    driver.get(url)

    wait = WebDriverWait(driver, 10)

    try:
        title_element = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        title = title_element.text.strip()

        paragraphs = driver.find_elements(By.CSS_SELECTOR, "article p")

        if not paragraphs:
            paragraphs = driver.find_elements(By.TAG_NAME, "p")

        content = " ".join([p.text for p in paragraphs[:10]])

    except Exception:
        print(f"Skipping problematic article: {url}")
        return None, None

    try:
        img = driver.find_element(By.CSS_SELECTOR, "article img")
        img_url = img.get_attribute("src")

        if img_url:
            img_data = requests.get(img_url).content

            with open(f"images/article_{index}.jpg", "wb") as f:
                f.write(img_data)

    except:
        print("No image found")

    return title, content