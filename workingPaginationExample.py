import requests
from bs4 import BeautifulSoup as bs


url = 'http://www.dabs.com/category/computing/11001'
base_url = 'https://www.dabs.com'
final_list = []

def get_next_link(link):
    r = requests.get(link)
    soup = bs(r.text, "html5lib")
    elm = soup.find('span',{'class':'current-page'})
#    print elm
    next_ = elm.findNext('a')
    next_page_link = base_url + next_['href']
    if next_page_link:
        print next_page_link
        final_list.append(next_page_link)
        get_next_link(next_page_link)

get_next_link(url)

print final_list

    



