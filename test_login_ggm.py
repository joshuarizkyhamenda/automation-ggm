import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from colorama import Fore, Style

class logintest(unittest.TestCase):
    #setup browser
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_logintest(self):
        #oper browser & fullscreen
        driver = self.driver
        driver.maximize_window()
        
        #Step login
        driver.get("https://staging.demopreview.link/login")
        email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[1]/section[1]/div[2]/div/div[1]/input')))
        email.send_keys("joshua.hamenda@fabindonesia.com")

        password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[1]/section[1]/div[2]/div/div[2]/div/input')))
        password.send_keys("12345678")
        
        btn_login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[1]/section[1]/div[2]/div/div[3]/button')))
        btn_login.click()
        
        #kondisi 1 - Gagal login
        try:
            validation_password = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div[1]/section[1]/div[2]/div/div[2]/div[2]')))
            assert "Password tidak sesuai, masukkan password dengan benar" in validation_password.text
            print(Fore.RED + 'FAIL! - ' + validation_password.text)
            print(Style.RESET_ALL)
        #kondisi 2 - Sukses login
        except: 
            print(Fore.GREEN + 'PASSED!')
            print(Style.RESET_ALL)

            btnsetting = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, '/html/body/div/div/div[2]/div[1]/section[3]/div/div/div[4]/a')))
            btnsetting.click()
            
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()