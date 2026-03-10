from selenium.webdriver import Remote
from selenium.webdriver.chrome.options import Options

def setup_driver():

    options = Options()

    options.set_capability("browserName", "Chrome")
    options.set_capability("browserVersion", "latest")

    options.set_capability("bstack:options", {
        "sessionName": "El Pais Scraper Test",
        "buildName": "browserstack-el-pais-scraper",
        "projectName": "browserstack-assignment"
    })

    driver = Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        options=options
    )

    return driver