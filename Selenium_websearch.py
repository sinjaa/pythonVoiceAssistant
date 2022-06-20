from selenium import webdriver

class info():
    def __init__(self):
        self.driver= webdriver.Chrome(executable_path="D:\Chromedriver\chromedriver.exe")
    def get_info(self, query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")

assist=info()
assist.get_info()
