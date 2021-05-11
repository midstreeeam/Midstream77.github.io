from blog_func import blog_func


class blog_deploy(blog_func):
    ''' deploy the generated blog'''

    def modify_nav(self):
        '''
        this function will be called by blog_post.py and will modify the previous page of the blogpage to add link to the list in navigation page.
        '''

        # generate the path for blogpage
        fname = '/blogs/' + self.category + '/' + self.title + '.html'

        # generate the template of link in the navigation page
        template = '''
        <li><a href="{fname}"><span class="blogname">{title}</span><span class="fill"></span><span class="date">{date}</span></a></li>
        '''.format(fname=fname, title=self.title, date=self.post_time)

        # defind keywords which is the mark writed in nav html program
        keywords = '<!-- list start -->'

        # generate the path of navigation html and read all the content
        path = './nav/' + self.category + '.html'
        f = open(path, 'r', encoding='utf-8')
        text = f.read()

        # add the template just after the keywords and write the content back to the html
        key = text.find(keywords)
        text = text[:key+len(keywords)] + template + text[key+len(keywords):]
        f = open(path, 'w', encoding='utf-8')
        f.write(text)

        # close the html file
        f.close()
