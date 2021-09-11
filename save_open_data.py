from apis import *
from csv import DictWriter

def save_list(the_list, filename):

    with open(filename, 'w') as fout:
        json.dump(the_list, fout)

def open_list(filename):

    with open(filename, "r") as fp:
        saved_list = json.load(fp)

    return saved_list