import time
from pageObjects.Login import Login
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/DataDriven.xlsx"


    time.sleep(3)
    logger = LogGen.loggen()
    # TO list


    def test_login_ddt(self, setup):
        self.logger.info("********Welcome to Test_002_DDT_Login**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(3)

        self.lp = Login(self.driver)
        self.rows=XLUtils.getRowCount(self.path,"Sheet1")
        print("Number of rows in the excel: ",self.rows)
        time.sleep(3)
        list_status=[]

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password=XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp=XLUtils.readData(self.path,"Sheet1",r,3)
            time.sleep(3)
            self.lp.setuserName(self.user)
            self.lp.setPassWord(self.password)
            self.lp.clickLogin()
            time.sleep(3)

            act_title=self.driver.title
            exp_title="Dashboard / nopcommerce administration"
            time.sleep(3)

            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("******Test is Passed*******")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                    time.sleep(3)

                elif self.exp=="Fail":
                    self.logger.info("*****Test is Failed*******")
                    self.lp.clickLogout()
                    list_status.append("Fail")
                    time.sleep(3)

            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("*****Test is Failed******")
                    list_status.append("Fail")
                    time.sleep(3)
                elif self.exp=="Fail":
                    self.logger.info("*****Passed*******")
                    list_status.append("Pass")
                    time.sleep(3)

            if "Fail" not in list_status:
                self.logger.info("Login DDT test is Passed........")
                self.driver.close()
                assert False

            else:
                self.logger.info("Login DDT test is Failed********")
                self.driver.close()
                assert True
                time.sleep(3)


        self.logger.info("******End of the Test Case*****")
        self.logger.info("*******Completed TC_Login DDt_002*******")



