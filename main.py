from apis import *
from save_open_data import *

if __name__ == "__main__":

    all_stats = []
    NUMBER_OF_PAGES = 10

    testf = FantasyEPL()
    testf.open_website()
    time.sleep(1)
    testf.go_stats()
    stats = testf.nav_players(number_of_players=30)
    all_stats.extend(stats)
    time.sleep(1)
    testf.quit_website()

    print("List = ", all_stats)
    print("Size : ", len(all_stats))

    

    
