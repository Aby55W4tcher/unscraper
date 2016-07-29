import csv
import urllib2
import requests
import re
import urlparse
from bs4 import BeautifulSoup as bs

#lists of pdf pages per site
list_Of_UNOCHA = ['http://www.unocha.org' , 'http://www.unocha.org/about-us/strategic-plan', 'http://www.unocha.org/about-us/publications', 'http://www.unocha.org/about-us/publications/humanitarian-reports', 'http://www.reliefweb.int/updates?sl=environment-report_listing%252Ctaxonomy_index_tid_source-1503%252Ctaxonomy_index_tid_content_format-8']
list_Of_UNHCR = ['http://www.unhcr.org/cgi-bin/texis/vtx/home', 'http://www.unhcr.org/resources-and-publications.html', 'http://www.unhcr.org/search?comid=56b086754&&cid=49aea93aba&scid=49aea93a5c&tags=midyear']
list_Of_UNICEF = ['http://www.unicef.org/', 'http://www.unicef.org/publications/index_82455.html', 'http://www.unicef.org/publications/']
list_Of_WFP = ['http://www.wfp.org/', 'http://www.wfp.org/publications/list', 'http://www.wfp.org/policy-resources/corporate?type=55&tid_2=All&tid_4=Allhttp://www.wfp.org/policy-resources/corporate?type=55&tid_2=All&tid_4=All']
list_Of_UNEP = ['http://www.unep.org/', 'http://www.unep.org/publications/', 'http://apps.unep.org/publications/index.php?option=com_pub&mid=8&ftype=Annual%20Report', 'http://apps.unep.org/publications/index.php?option=com_pub&mid=14&ftype=Infographics','http://apps.unep.org/publications/index.php?option=com_pub&mid=15&ftype=Factsheets']
list_Of_UNODC = ['http://www.unodc.org/', 'http://www.unodc.org/unodc/en/publications-by-date.html']
list_Of_OPCW = ['https://www.opcw.org/', 'https://www.opcw.org/documents-reports/fact-sheets/', 'https://www.opcw.org/documents-reports/annual-reports/']
list_Of_WTO = ['https://www.wto.org/', 'https://www.wto.org/english/res_e/publications_e/publications_e.htm']
list_Of_UNISDR = ['http://www.unisdr.org/', 'http://www.unisdr.org/we/inform/publications', 'http://www.unisdr.org/we/inform/publications/key']
list_Of_UNAIDS = ['http://www.unaids.org/en', 'http://www.unaids.org/en/resources/documents/2016/']
list_Of_IAEA = ['https://www.iaea.org/', 'https://www.iaea.org/publications/reports', 'https://www.iaea.org/publications/documents/infcircs', 'https://www.iaea.org/publications/documents', 'https://www.iaea.org/publications/booklets', 'https://www.iaea.org/publications/factsheets']
list_Of_FAO = ['http://www.fao.org/home/en/', 'http://www.fao.org/publications/en/', 'http://www.fao.org/publications/en/?page=2&ipp=10&no_cache=1&tx_dynalist_pi1[par]=YToxOntzOjE6IkwiO3M6MToiMCI7fQ==']
list_Of_ILO = ['http://www.ilo.org/global/lang--en/index.htm', 'http://www.ilo.org/global/publications/lang--en/index.htm']
list_Of_WHO = ['http://www.who.int/en/', 'http://www.who.int/publications/en/']
#list of lists
list_Of_UNLists = [list_Of_UNOCHA, list_Of_UNHCR, list_Of_UNICEF, list_Of_WFP, list_Of_UNEP, list_Of_UNODC, list_Of_OPCW, list_Of_WTO, list_Of_UNISDR, list_Of_UNAIDS, list_Of_IAEA, list_Of_FAO, list_Of_ILO, list_Of_WHO]

#site headings for csv file (as lists)
#unocha_Heading = ['UNOCHA', '', '', '', '']
#unhcr_Heading = ['UNHCR', '', '']
#unicef_Heading = ['UNICEF', '', '']
#wfp_Heading = ['WFP', '', '']
#unep_Heading = ['UNEP', '', '', '', '']
#unodc_Heading = ['UNODC', '']
#opcw_Heading = ['OPCW', '', '']
#wto_Heading = ['WTO', '']
#unisdr_Heading = ['UNISDR', '', '']
#unaids_Heading = ['UNAIDS', '']
#iaea_Heading = ['IAEA', '', '', '', '', '']
#fao_Heading = ['FAO', '', '']
#ilo_Heading = ['ILO', '']
#who_Heading = ['WHO', '']

#list of headings for csv file
#headings = [unocha_Heading, unhcr_Heading, unicef_Heading, wfp_Heading, unep_Heading, unodc_Heading, opcw_Heading, wto_Heading, unisdr_Heading, unaids_Heading, iaea_Heading, fao_Heading, ilo_Heading, who_Heading] 

#compiling the list
final_list = []
full_list = sum(list_Of_UNLists, [])
for item in full_list:
#    print '----->' + item                                                                          #remove '#' at beginning of line to print sources
    response = requests.get(item)
    html = response.content
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html)
    for url in urls:
        # pagination code

        
        clean_url = urlparse.urljoin(url, urlparse.urlparse(url).path)
        if clean_url.endswith('.pdf'):
            www = item.index('w.')
            if '.org' in item:
                dotsomething = item.index('.org')
            elif '.int' in item:
                dotsomething = item.index('.int')
            if 'https://' in item:
                file_name = item[www+1:dotsomething]    
            else:
                file_name = item[www+2:dotsomething]
                                    
            print file_name
            
            outfile = open('./' + file_name + '.csv', "ab")
            writer = csv.writer(outfile)
            writer.writerow([clean_url])
            #final_list.append(clean_url)

#print final_list                                                                                    #remove '#' at beginning of line to print all pdf urls

#creating the .csv files
            
#UNOCHA
#if clean_url =             

#    outfile = open("./UNOCHA_PDFS.csv", "wb")
#    writer = csv.writer(outfile)
    #writer.writerow(['UNOCHA', '', '', '', '', 'UNHCR', '', '', 'UNICEF', '', '', 'WFP', '', '', 'UNEP', '', '', '', '', 'UNODC', '', 'OPCW', '', '', 'WTO', '', 'UNISDR', '', '', 'UNAIDS', '', 'IAEA', '', '', '', '', '', 'FAO', '', '', 'ILO', '', 'WHO', ''])
 #   for pdf in final_list:
 #       writer.writerow(final_list)
        




        

               
