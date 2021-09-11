from os import stat
from apis import *
from save_open_data import *

if __name__ == "__main__":

    all_stats = []
    NUMBER_OF_PAGES = 2

    testf = FantasyEPL()
    testf.open_website()
    time.sleep(1)
    testf.go_stats()

    for page in range(1, NUMBER_OF_PAGES + 1):

        stats = testf.nav_players(number_of_players=30)
        all_stats.extend(stats)
        testf.next_page_stats()
        time.sleep(1)

    testf.quit_website()

    print(all_stats[-1])
    print("List Size = ", len(all_stats))
    

    
