# 1. Import module
import unittest #untuk mejalankan tetsing
from selenium import webdriver #untuk membuka browser
from selenium.webdriver.common.keys import Keys #untuk action contoh input text
from selenium.webdriver.common.by import By #untuk get element
from selenium.webdriver.support import expected_conditions as EC #action untuk menunggu element yang definisi
from selenium.webdriver.support.wait import WebDriverWait #untuk menemtukan berapa lama waktu menunggu loading
from colorama import Fore, Style #untuk memberikan warna pada terimal (PASSED/FAIL)

# 2. Create test module
class sampletest(unittest.TestCase):
    
    # 3. Initialization
    def setUp(self):
        self.driver = webdriver.Chrome()

    # 4. Test scenario
    def test_open_page(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element(By.NAME, "q")
        elem.send_keys("Python")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    # 5. End session / close browser
    def tearDown(self):
        self.driver.close()

# 6. Running Test
if __name__ == "__main__":
    unittest.main()
