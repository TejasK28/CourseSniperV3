#this file focuses on pining the api endpoint
import webbrowser


#import statements that are necessary for requesting & parsing
import requests
from bs4 import BeautifulSoup
import re, lxml, json

OPEN_INDEX_NUMBERS = "https://sis.rutgers.edu/soc/api/openSections.json?year=2024&term=1&campus=NB"

def getRegLink(index):
    return f"https://sims.rutgers.edu/webreg/editSchedule.htm?login=cas&amp;semesterSelection=12024&amp;indexList={index}"

def getJSON():
    open_indexes = json.loads(BeautifulSoup(requests.get(OPEN_INDEX_NUMBERS).text, 'lxml').text)
    return open_indexes

def isIndexOpen(tindex):
    open_indexes = getJSON()
    if tindex in open_indexes:
        return True
    else:
        return False
    
def start_checking(dindex): 
    ignore_list = []   
    while True:
        for index in dindex :
            if isIndexOpen(index) and index not in ignore_list:
                print(f"{index} : open section")
                print(getRegLink(index))
                ignore_list.append(index)
                webbrowser.open(url, new=0, autoraise=True)

            else:   
                print(f"{index} : closed section")
        
        print("~~~~~~~~~~~~~~~~~~")

if __name__ == '__main__':
    start_checking(['17322', '17323']);