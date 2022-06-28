from selenium import webdriver


class YouTube():
    def __init__(self):
        self.driver= webdriver.Chrome(executable_path='D:\Chromedriver\chromedriver.exe')

    def play_video(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query=" +query)
        search=self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        search.click()

