from selenium import webdriver

class wiki():
    def __init__(self):
        self.driver= webdriver.Chrome(executable_path='D:\Chromedriver\chromedriver.exe')

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        searchwiki=self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        searchwiki.click()
        searchwiki.send_keys(query)
        entersearch=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        entersearch.click()

