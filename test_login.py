import time
from pageObjects.Login import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassWord()


    time.sleep(3)
    logger = LogGen.loggen()
    # T list

    def test_homepage_title(self, setup):
        time.sleep(3)
        self.logger.info("*************Test_001_Login******************")
        time.sleep(3)
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        time.sleep(3)
        # self.driver.close()
        self.logger.info("==============Home page title test is passed==========")
        if actual_title == "Your store. Login":
            print(actual_title)
            assert True
        else:
            time.sleep(3)
            self.logger.info("*******Test case failed*************")
            # print(self.logger.info)
            time.sleep(3)
            self.driver.get_screenshot_as_file(".\\Screenshots\\" + "file2.png")
            self.logger.info("***********Home page title test is failed*********")
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setuserName(self.username)
        # self.lp.setuserName(self.username)
        self.lp.setPassWord(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            print(act_title)
        else:
            assert False
