from blog_func import blog_func

class blog_deploy(blog_func):
    def modify_nav(self):
        fname = '/blogs/' + self.category + '/' + self.title + '.html'
        template = '''
        <li><a href="{fname}"><span class="blogname">{title}</span><span class="fill"></span><span class="date">{date}</span></a></li>
        '''.format(fname = fname, title = self.title, date = self.post_time)
        keywords = '<!-- list start -->'
        path = './nav/'+ self.category + '.html'
        f = open(path,'r',encoding='utf-8')
        text = f.read()
        key = text.find(keywords)
        text = text[:key+len(keywords)] + template + text[key+len(keywords):]
        f = open(path,'w',encoding='utf-8')
        f.write(text)
        f.close()
