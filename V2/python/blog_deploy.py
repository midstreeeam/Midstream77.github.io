from blog_func import blog_func


class blog_deploy(blog_func):
    ''' deploy the generated blog'''

    def modify_nav(self):
        '''
        this function will be called by blog_post.py and will modify the other pages to add link to the list in tags page and index page.
        '''

        # generate the path for blogpage
        fname = '/blogs/' + self.title + '.html'

        # generate html piece for tags
        tags_text = ''
        for i in range(len(self.tags)):
            tags_text += '<a href="{tag_link}" class = "blog_tag">#{tag_name}</a>\n'.format(
            tag_link='../html/'+self.tags[i]+'.html',
            tag_name=self.tags[i])

        # generate the template of link in tags page and index page
        template = '''
<div class="blog_block">
    <a href="{fname}">
        <h3 class="blog_title">{title}</h3>
    </a>
    <p class="blog_date">{date}</p>
    <a href="{fname}">
        <p class="blog_pre">
            {pre}
        </p>
    </a>
    {tags}
</div>
<div class="block_divider"></div>
        '''.format(fname=fname, title=self.title, date=self.post_time, pre=self.pre, tags=tags_text)

        # defind keywords which is the mark writed in index and tag html
        keywords = '<!-- list start -->'

        #for all tag pages
        for i in range(len(self.tags)):
            # generate the path of tag html and read all the content
            path = './html/' + self.tags[i] + '.html'
            f = open(path, 'r', encoding='utf-8')
            text = f.read()

            # add the template just after the keywords and write the content back to the html
            key = text.find(keywords)
            text = text[:key+len(keywords)] + template + text[key+len(keywords):]
            f = open(path, 'w', encoding='utf-8')
            f.write(text)

            # close the html file
            f.close()


        #for index.html
        path = './index.html'
        f = open(path, 'r', encoding='utf-8')
        text = f.read()

        # add the template just after the keywords and write the content back to the html
        key = text.find(keywords)
        text = text[:key+len(keywords)] + template + text[key+len(keywords):]
        f = open(path, 'w', encoding='utf-8')
        f.write(text)

        # close the html file
        f.close()
