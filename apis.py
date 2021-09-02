from selenium import webdriver
from selenium.webdriver.common.keys import Keys      #Allows us to use Enter, ESC, Space...
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class FantasyEPL():

    PATH = "C:\Program Files (x86)\chromedriver.exe"
    FANTASY_WEBSITE = "https://fantasy.premierleague.com/"
    STATS = (By.XPATH, "//a[contains(text(), 'Statistics')]")
    HOME = (By.XPATH, "//a[contains(text(), 'Home')]")
    FILTER_PLAYERS = (By.ID, "filter")
    SORT_PLAYERS = (By.ID, "sort")

    def __init__(self):
        self.driver = webdriver.Chrome(self.PATH)

    def open_website(self):
        self.driver.get(self.FANTASY_WEBSITE)

    def drop_filter_players(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FILTER_PLAYERS)).click()
        
    def drop_sort_players(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SORT_PLAYERS)).click()

    def go_home(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.HOME)).click()

    def go_stats(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.STATS)).click()

    def quit_website(self):
        self.driver.quit()


if __name__ == "__main__":

    testf = FantasyEPL()

    testf.open_website()
    
    time.sleep(1)
    testf.go_stats()
    time.sleep(1)
    testf.drop_filter_players()
    time.sleep(1)
    testf.drop_sort_players()
    time.sleep(10)
    
