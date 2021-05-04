from blog_func import blog_func
from blog_gen import blog_gen
from blog_deploy import blog_deploy
choices = {
    '1':'dailyblog',
    '2':'updatelog',
    '3':'astro',
    '4':'olderposts'
}
title = input('please input the title of the blog:   ')
choice = input('''please input the category of the blog

categories:

1. dilyblog
2. updatelog
3. astro
4. olderposts

''')
category = choices.get(choice)

print('please paste the blog into input.txt')
input('enter to post the blog')


t1 = blog_gen(category,title)
t2 = blog_deploy(category,title)
t1.gen_html()
t2.modify_nav()

