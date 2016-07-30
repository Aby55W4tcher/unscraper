import requests
from bs4 import BeautifulSoup as bs
import time

url = 'http://www.wfp,org/publications/list'
base_url = 'http://www.wfp.org'
final_list = []


def get_next_link(link):
    time.sleep(3600)
    r = requests.get(link)
    soup = bs(r.text, "html5lib")
    elm = soup.find('span',{'class':'field-content'})
#    print elm
    next_ = elm.findNext('a')
    next_page_link = base_url + next_['href']
    if next_page_link:
        print next_page_link
        final_list.append(next_page_link)
        get_next_link(next_page_link)

get_next_link(url)
    

print final_list

