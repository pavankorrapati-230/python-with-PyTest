import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\Dell\\PycharmProjects\\Commerce_Project\\Configurations\\config.ini")
#config.read(".\\Configurations\\config.ini")




class ReadConfig:
    # config = configparser.RawConfigParser()
    # config.read(".\\Configurations\\config.ini")

    @staticmethod
    def getApplicationURL():
        url = config.get("Common_info", "baseURL")
        return url

    @staticmethod
    def getUserEmail():
        username = config.get("Common_info", "username")
        return username

    @staticmethod
    def getPassWord():
        password = config.get("Common_info", "password")
        return password
