import os
import sys
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

'''
modify search.json to don't let the search bar show the posts that need password
'''
search_ban_blogs=[
    'MidstreamBlog',
    '逐蛋者',
    '在这片土地上',
]

import json

with open('../docs/search.json','r',encoding='utf8') as f:
    search_dics=json.loads(f.read())

new_dics=[]
for search_dic in search_dics:
    if search_dic["title"] not in search_ban_blogs:
        new_dics.append(search_dic)

with open('../docs/search.json','w',encoding='utf8') as f:
    f.write(json.dumps(new_dics))


'''
modify index.xml to ban some blogs from rss feed
'''
from bs4 import BeautifulSoup

rss_ban_blogs=[
    '逐蛋者',
    '在这片土地上',
]

with open('../docs/index.xml','r',encoding='utf8') as f:
    raw_xml=f.read()

soup = BeautifulSoup(raw_xml,features="xml")
for i in soup.find_all('item'):
    if i.title.text in rss_ban_blogs:
        i.description.clear()

with open('../docs/index.xml','w', encoding='utf8') as f:
    f.write(str(soup))

