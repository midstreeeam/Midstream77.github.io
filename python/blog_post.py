from blog_func import blog_func
from blog_gen import blog_gen
from blog_deploy import blog_deploy

# the tags
choices = {
    '1': '日常',
    '2': '游记',
    '3': '旧日志',
    '4': '天文',
    '5': '学习笔记',
    '6': '抽象艺术',
    '7': '更新日志',
    '8': '投稿'
}
title = input('please input the title of the blog:   ')
choice = []
tags = []

for i in range(7):
    index = input('''
    please input the tag of the blog,
    press "s" to finish.

    tags:

    1. 日常
    2. 游记
    3. 旧日志
    4. 天文
    5. 学习笔记
    6. 抽象艺术
    7. 更新日志
    8. 投稿

    ''')
    if(index=='s'):
        break
    choice.append(index)

for i in range(len(choice)):
    tags.append(choices.get(choice[i]))


time = input('''please enter the first post time of the blog,
if the blog have never been post before,
just press enter

time: ''')

print('please paste the blog into input.txt')
input('enter to post the blog')


# init the class
t1 = blog_gen(tags, title, time)
t2 = blog_deploy(tags, title, time)

# generate the blog html file
t1.gen_html()

# modify the previous page of blog
t2.modify_nav()
