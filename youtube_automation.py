from selenium import webdriver

class YTube():
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver= webdriver.Chrome(options=options, executable_path='D:\Chromedriver\chromedriver.exe')

    def play_video(self,query):
        self.query=query
        self.driver.get(url="https://www.youtube.com/results?search_query=" +query)
        search=self.driver.find_element_by_xpath('//*[@id="video-title"]/yt-formatted-string')
        search.click()
