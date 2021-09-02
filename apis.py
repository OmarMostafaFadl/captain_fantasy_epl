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
    PLAYER_X_BUTTON = (By.XPATH, "//*[@id='root-dialog']/div/dialog/div/div[1]/div[2]/button")
    NEXT_PAGE_STATS = (By.XPATH, "//*[@id='root']/div[2]/div/div[1]/div[3]/button[3]")
    LAST_PAGE_STATS = (By.XPATH, "//*[@id='root']/div[2]/div/div[1]/div[3]/button[2]")


    def __init__(self):
        self.driver = webdriver.Chrome(self.PATH)

    def open_website(self):
        self.driver.get(self.FANTASY_WEBSITE)

    def go_home(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.HOME)).click()

    def go_stats(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.STATS)).click()

    def drop_filter_players(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FILTER_PLAYERS)).click()
        
    def drop_sort_players(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SORT_PLAYERS)).click()

    def click_player(self, player_row):

        PLAYER = (By.XPATH, "//*[@id='root']/div[2]/div/div[1]/table/tbody/tr["+ str(player_row) +"]/td[1]/button")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(PLAYER)).click()

    def exit_player(self):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PLAYER_X_BUTTON)).click()

    def nav_players(self):

        player_rows = 31

        for player_row in range(1, player_rows):

            self.click_player(player_row)
            time.sleep(1)
            self.exit_player()
            time.sleep(1)

    def next_page_stats(self):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.NEXT_PAGE_STATS)).click()
        htmlelement= self.driver.find_element_by_tag_name('html')
        htmlelement.send_keys(Keys.END)
        htmlelement.send_keys(Keys.HOME)

    def last_page_stats(self):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.LAST_PAGE_STATS)).click()
        htmlelement= self.driver.find_element_by_tag_name('html')
        htmlelement.send_keys(Keys.END)
        htmlelement.send_keys(Keys.HOME)

    def quit_website(self):
        self.driver.quit()


if __name__ == "__main__":

    testf = FantasyEPL()

    testf.open_website()
    
    time.sleep(1)
    testf.go_stats()
    time.sleep(1)
    testf.nav_players()
    time.sleep(1)
    testf.next_page_stats()
    time.sleep(1)
    testf.nav_players()
    time.sleep(1000)

    


    
