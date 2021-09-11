import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    def nav_player_stats(self, gameweeks):

        all_stats = {"Player Name": [], "Player Position": [], "Gameweek": [], "Points":[], "Minutes Played": [], "Goals Scored": [], 
                     "Assists": [], "Clean Sheets": [], "Goals Conceded": [], "Own Goals": [], "Penalties Saved": [], 
                     "Penalties Missed": [], "Yellow Cards": [], "Red Cards": [], "Saves": [], "Bonus Points": [], 
                     "Bonus Points System": [], "Price": []}

        LOGO = (By.XPATH, "//*[@id='ism-dialog-title']/img")
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(LOGO))
        #player_name = self.driver.find_element_by_xpath("//h2[@attribute=ElementDialog__ElementHeading-gmefnd-2 llwlWO]")
        try: 
            player_name = self.driver.find_element_by_xpath("//*[@id='root-dialog']/div/dialog/div/div[2]/div[1]/div[1]/div/div[1]/h2").text
            player_position = self.driver.find_element_by_xpath("//*[@id='root-dialog']/div/dialog/div/div[2]/div[1]/div[1]/div/div[1]/span").text

            all_stats["Player Name"].append(player_name)
            all_stats["Player Position"].append(player_position)
        except:
            player_name = self.driver.find_element_by_xpath("//*[@id='root-dialog']/div/dialog/div/div[2]/div[2]/div[1]/div/div[1]/h2").text
            player_position = self.driver.find_element_by_xpath("//*[@id='root-dialog']/div/dialog/div/div[2]/div[2]/div[1]/div/div[1]/span").text

            all_stats["Player Name"].append(player_name)
            all_stats["Player Position"].append(player_position)
        

        for gameweek in range(1, gameweeks + 1):

            try:
                
                check = (By.XPATH, "//*[@id='root-dialog']/div/dialog/div/div[2]/div[2]/div/div/div[1]/div/table/tbody")
                WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located(check))

                stats_string = "//*[@id='root-dialog']/div/dialog/div/div[2]/div[2]/div/div/div[1]/div/table/tbody/tr["

                gw = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[1]").text
                points = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[3]").text
                minutes_played = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[4]").text
                goals = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[5]").text
                assists = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[6]").text
                clean_sheets = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[7]").text
                goals_conceded = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[8]").text
                own_goals = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[9]").text
                penalties_saved = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[10]").text
                penalties_missed = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[11]").text
                yellow_cards = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[12]").text
                red_cards = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[13]").text
                saves = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[14]").text
                bonus = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[15]").text
                bonus_point_system = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[16]").text
                price = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[23]").text

                all_stats["Gameweek"].append(gw)
                all_stats["Minutes Played"].append(minutes_played)
                all_stats["Points"].append(points)
                all_stats["Goals Scored"].append(goals)
                all_stats["Assists"].append(assists)
                all_stats["Clean Sheets"].append(clean_sheets)
                all_stats["Goals Conceded"].append(goals_conceded)
                all_stats["Own Goals"].append(own_goals)
                all_stats["Penalties Saved"].append(penalties_saved)
                all_stats["Penalties Missed"].append(penalties_missed)
                all_stats["Yellow Cards"].append(yellow_cards)
                all_stats["Red Cards"].append(red_cards)
                all_stats["Saves"].append(saves)
                all_stats["Bonus Points"].append(bonus)
                all_stats["Bonus Points System"].append(bonus_point_system)
                all_stats["Price"].append(price)
            
            except:
                
                check = (By.XPATH, "//*[@id='root-dialog']/div/dialog/div/div[2]/div[3]/div/div/div[1]/div/table/tbody")
                WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located(check))

                stats_string = "//*[@id='root-dialog']/div/dialog/div/div[2]/div[3]/div/div/div[1]/div/table/tbody/tr["

                gw = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[1]").text
                points = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[3]").text
                minutes_played = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[4]").text
                goals = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[5]").text
                assists = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[6]").text
                clean_sheets = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[7]").text
                goals_conceded = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[8]").text
                own_goals = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[9]").text
                penalties_saved = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[10]").text
                penalties_missed = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[11]").text
                yellow_cards = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[12]").text
                red_cards = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[13]").text
                saves = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[14]").text
                bonus = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[15]").text
                bonus_point_system = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[16]").text
                price = self.driver.find_element_by_xpath(stats_string + str(gameweek) +"]/td[23]").text

                all_stats["Gameweek"].append(gw)
                all_stats["Minutes Played"].append(minutes_played)
                all_stats["Points"].append(points)
                all_stats["Goals Scored"].append(goals)
                all_stats["Assists"].append(assists)
                all_stats["Clean Sheets"].append(clean_sheets)
                all_stats["Goals Conceded"].append(goals_conceded)
                all_stats["Own Goals"].append(own_goals)
                all_stats["Penalties Saved"].append(penalties_saved)
                all_stats["Penalties Missed"].append(penalties_missed)
                all_stats["Yellow Cards"].append(yellow_cards)
                all_stats["Red Cards"].append(red_cards)
                all_stats["Saves"].append(saves)
                all_stats["Bonus Points"].append(bonus)
                all_stats["Bonus Points System"].append(bonus_point_system)
                all_stats["Price"].append(price)

        return all_stats

    def exit_player(self):

        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.PLAYER_X_BUTTON)).click()

    def nav_players(self, number_of_players):

        all_players_stats = []

        for player in range(1, number_of_players + 1):

            self.click_player(player)
            stats = self.nav_player_stats(gameweeks=3)
            all_players_stats.append(stats)
            self.exit_player()

        return all_players_stats

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
