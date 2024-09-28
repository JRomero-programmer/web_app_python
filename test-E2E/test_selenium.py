import os
import unittest
from xmlrunner import XMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class TestSelenium(unittest.TestCase):

    def setUp(self):
        chrome_bin = os.getenv('CHROME_BIN')
        chromedriver_bin = os.getenv('CHROMEDRIVER_BIN')

        if not chrome_bin or not chromedriver_bin:
            raise EnvironmentError("Las variables de entorno CHROME_BIN y CHROMEDRIVER_BIN deben estar definidas")

        options = webdriver.ChromeOptions()
        options.binary_location = chrome_bin
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        service = Service(executable_path=chromedriver_bin)
        self.driver = webdriver.Chrome(service=service, options=options)

    def test_webpage(self):
        driver = self.driver
        driver.get('http://localhost:3000')
        time.sleep(3)

        heading = driver.find_element(By.CLASS_NAME, 'rt-Heading')
        self.assertIn("Jonatan Romero", heading.text, "El título no es correcto.")

        paragraph = driver.find_element(By.XPATH, '//p[contains(text(), "devsecops-spain")]')
        self.assertIn("devsecops-spain", paragraph.text, "El texto del párrafo no es correcto.")

        linkedin_button = driver.find_element(By.XPATH, '//div[@class="rt-Flex rt-r-fd-row rt-r-ai-center rt-r-gap-3 rx-Stack"]')
        linkedin_button.click()

        time.sleep(3)

        driver.switch_to.window(driver.window_handles[1])

        self.assertIn("linkedin.com", driver.current_url, "No se redirigió correctamente a LinkedIn.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    if not os.path.exists('test-reports'):
        os.makedirs('test-reports')

    with open('test-reports/results.xml', 'wb') as output:
        unittest.main(testRunner=XMLTestRunner(output=output), failfast=False, buffer=False, catchbreak=False)
