'''
modify search.json to don't let the search bar show the posts that need password
'''

ban_blogs=[
    '逐蛋者',
    '在这片土地上',
]

import json

with open('docs/search.json','r') as f:
    search_dics=json.loads(f.read())

new_dics=[]
for search_dic in search_dics:
    if search_dic["title"] not in ban_blogs:
        new_dics.append(search_dic)

with open('docs/search.json','w') as f:
    f.write(json.dumps(new_dics))
