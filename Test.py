import requests
from bs4 import BeautifulSoup as bs


url = 'http://www.reliefweb.int/updates?sl=environment-report_listing%252Ctaxonomy_index_tid_source-1503%252Ctaxonomy_index_tid_content_format-8'
base_url = 'http://www.reliefweb.int'
final_list = []

def get_next_link(link):
    r = requests.get(link)
    soup = bs(r.text, "html5lib")
    elm = soup.find('div',{'class':'pager-current'})
    next_ = elm.findNext('a')
    next_page_link = base_url + next_['href']
    if next_page_link:
        print next_page_link
        final_list.append(next_page_link)
        get_next_link(next_page_link)

get_next_link(url)

print final_list

    



