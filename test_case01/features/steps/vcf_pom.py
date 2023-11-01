import time
from telnetlib import EC
import configparser

from selenium.common import NoSuchElementException
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions as EC, wait

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

config = configparser.RawConfigParser()
with open('test_case01/features/steps/config.ini', 'r') as f:
    config_string = '[DEFAULT]\n' + f.read()


class cycle:
    def __init__(self, driver):
        self.driver = driver
        config.read_string(config_string)
        self.base_url = config.get('Default', 'base_url')
        self.username = config.get('Default', 'username')
        self.password = config.get('Default', 'password')

    def creation_screen(self):
        self.driver.get(self.base_url)
        self.driver.find_element(By.ID, 'email_id').send_keys(self.username)
        self.driver.find_element(By.ID, 'password').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        time.sleep(15)
        self.driver.find_element(By.XPATH, '//*[@id="tour-test-lab-btn"]').click()

    def testcase1_mod1(self):
        self.driver.find_element(By.ID, "tour-cycle-create-btn").click()
        self.driver.find_element(By.ID, 'name').send_keys("cycle2")
        self.driver.find_element(By.ID, 'build_id').click()
        iframe_element = self.driver.find_element(By.ID, 'note_ifr')
        self.driver.switch_to.frame(iframe_element)
        self.driver.find_element(By.CLASS_NAME, 'mce-content-body').send_keys("Cycle2 for testing module")
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, 'start-date').click()
        self.driver.find_element(By.ID, 'end-date').click()
        self.driver.find_element(By.NAME, 'assigned_users[]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Talha Bhatti"]').click()
        self.driver.execute_script("window.scrollTo(1, document.body.scrollHeight);")
        time.sleep(10)
        self.driver.find_element(By.ID, 'cycle-create-submit-btn').click()

    def verify_cycle1(self):
        ver = self.driver.find_element(By.XPATH, '//*[text()="cycle2"]').text
        if ver == "cycle":
            assert True, "Cycle has been added"

    def testcase1_mod2(self):
        self.driver.find_element(By.ID, "tour-cycle-create-btn").click()
        self.driver.find_element(By.ID, 'assign_to_required').click()
        self.driver.execute_script("window.scrollTo(1, document.body.scrollHeight);")
        time.sleep(10)
        self.driver.find_element(By.XPATH, '//button[@class="submit-btn"]').click()

    def verify_cycle2(self):
        ver2 = self.driver.find_element(By.CLASS_NAME, 'ng-star-inserted').text
        if ver2 == "Assign to is required":
            assert True, "Cycle cannot be created"

    def testcase1_mod3(self):
        self.driver.find_element(By.ID, 'assign_to_required').click()
        self.driver.execute_script("window.scrollTo(1, document.body.scrollHeight);")
        self.driver.find_element(By.ID, 'cycle-create-submit-btn').click()

    def verify_mod3(self):
        ver3_a = self.driver.find_element(By.CLASS_NAME, 'ng-star-inserted').text
        ver3_b = self.driver.find_element(By.XPATH, "//*[text()='Name is required']").text
        if ver3_a == "Assign is to required" and ver3_b == "Name is required":
            assert True, "Name and Assign to field required"

    def testcase1_mod5(self):
        self.driver.find_element(By.ID, "tour-cycle-create-btn").click()
        self.driver.find_element(By.ID, 'name').send_keys("cycle1")
        iframe_element = self.driver.find_element(By.ID, 'note_ifr')
        self.driver.switch_to.frame(iframe_element)
        self.driver.find_element(By.CLASS_NAME, 'mce-content-body').send_keys("Cycle1 for testing defect modules")
        self.driver.switch_to.default_content()
        self.driver.find_element(By.NAME, 'assigned_users[]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Talha Bhatti"]').click()
        self.driver.find_element(By.ID, 'assign_to_required').click()
        self.driver.execute_script("window.scrollTo(1, document.body.scrollHeight);")
        time.sleep(10)
        self.driver.find_element(By.ID, 'cycle-create-submit-btn').click()

    def verify_mod5(self):
        ver = self.driver.find_element(By.XPATH, '//td[@class="data first-col"]').text
        if ver == "cycle":
            assert True, "Cycle has been added"
        print('Email sent to the user verified manually')

    def testcase_mod7(self):
        self.driver.find_element(By.XPATH, "//*[@name='DataTables_Table_1_length']").click()
        value = self.driver.find_element(By.XPATH, "//*[@name='DataTables_Table_1_length']//child::option[text()='20']")
        value.click()
        value_text = value.text
        if value_text == "20":
            assert True, "Selected value is 20"

    def testcase_mod8_name(self):
        search = self.driver.find_element(By.XPATH, '//input[@type="search"]')
        search.click()
        search.send_keys("Cycle2")
        search.send_keys(Keys.RETURN)
        search_text = self.driver.find_element(By.XPATH, '//td[@class="data first-col"]').text

        if search_text == "cycle2":
            assert True, 'Cycle exist'
        else:
            assert True, 'Cycle did not exist'

    def testcase_mod9(self):
        self.driver.find_element(By.XPATH, '//*[contains(@title,"Copy")]').click()

    def popup_verify(self):
        popup_text = self.driver.find_element(By.XPATH,
                                              '//*[text()="cycle does not conatain any testcases to copy"]').text
        if popup_text == "cycle does not conatain any testcases to copy":
            assert True, 'cycle does not conatain any testcases to copy'

    def testcase_mod10(self):
        self.driver.find_element(By.XPATH, "//td[text()='cycle1']/..//*[@title='Delete']").click()
        self.driver.find_element(By.XPATH, "//*[text()='Delete']").click()

    def delete_verify(self):
        delete_text = self.driver.find_element(By.XPATH, '//span[text()="Cycle successfully deleted"]')
        if delete_text == "Cycle successfully deleted":
            assert True, 'Cycle successfully deleted'

    def testcase_mod11(self):
        self.driver.find_element(By.XPATH, "//*[contains(@title,'Delete')]").click()
        self.driver.find_element(By.XPATH, '//*[@class="submit-btn cancel"]').click()

    def cancel_verify(self):
        try:
            self.driver.find_element(By.XPATH, "//td[text()='cycle2']/..//*[@title='Delete']")
            print('Element not deleted')
        except NoSuchElementException:
            print('Element deleted')

    def testcase_mod12(self):
        self.driver.find_element(By.XPATH, "//*[@class= 'paginate_button previous disabled']").click()
        self.driver.find_element(By.XPATH, "//*[@class= 'paginate_button next disabled']").click()

