from selenium import webdriver

class wiki():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver= webdriver.Chrome(options=options, executable_path='D:\Chromedriver\chromedriver.exe')

    def get_info(self,query):
        self.query=query
        self.driver.get(url="https://www.wikipedia.org")
        searchwiki=self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        searchwiki.click()
        searchwiki.send_keys(query)
        entersearch=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        entersearch.click()

