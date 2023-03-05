import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=".\\Logs\\automation.log",
                        format="%(asctime): %(levelname)s: %(message)",datefmt="%m/%d/%Y %I:%M:%s %p")
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


# class LogGen:
#     @staticmethod
#     def loggen():
#         #logging.basicConfig(filename=".\\Logs\\"+"Automation",format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%y %I:%M:%S %p')
#         #logging.basicConfig(filename="C://Users//Dell//PycharmProjects//Commerce_Project//Logs//pavan.log",level=logging.INFO)
#         logging.basicConfig(filename="C:\\Users\\Dell\\PycharmProjects\\Commerce_Project\\Logs\\pavan.log",level=logging.INFO)
#
#         #logging.basicConfig(filename="E:\\Exper\\pavan1.log")
#         #logging.basicConfig(filename=".\\Logs\\"+"automation.log",
#                             #format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m%d%y %I:%M:%S %p')
#         logger = logging.getLogger()
#         logger.setLevel(logging.INFO)
#         return logger
#
# # def log(level,message,file):
# #     L.basicConfig(level=L.INFO,filename=file,filemode="a",format="%(asctime)-12s %(levelname)s %(message)",
# #                   datefmt="%d-%m-%")
#
#
