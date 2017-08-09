import requests
from bs4 import BeautifulSoup
import re

HTML_PARSER = "html.parser"
ROOT_URL = 'https://tw.buy.yahoo.com/?catitemid='
GDSALE_PATH = 'gdsale/'

def get_item_list():
	for catitemid in range(102319,102322):

	    list_req = requests.get(ROOT_URL + str(catitemid))

	    if list_req.status_code == requests.codes.ok:

	        soup = BeautifulSoup(list_req.content, HTML_PARSER)

	        title = soup.find('title')

	        print(title.text)
	        
	        item_links_a_tags = soup.find_all('div', attrs={'class': 'srp-pdtitle'})

	        if len(item_links_a_tags) > 3 :
	        	size = 3 
	        else :
	        	size = len(item_links_a_tags)

	        if size == 0 :
	        	print('no ranking')

	        for i in range(0, size):
	            
	            s = BeautifulSoup(item_links_a_tags[i].text, HTML_PARSER)
	            
	            print(s)

if __name__ == '__main__':
    get_item_list()