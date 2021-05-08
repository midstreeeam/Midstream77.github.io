from blog_func import blog_func
class blog_gen(blog_func):
    '''generate a html file for blog page'''

    def gen_template(self):
        ''' generate the content of the blogpage html file '''

        #read the conent in the input.txt and transfer all the space and tab into '&ensp;'
        f = open('./input.txt','r',encoding='utf-8')
        text = f.read()
        text_list = list(text)
        for i in range(len(text)):
            if text_list[i] == ' ':
                text_list[i] = '&ensp;'
            if text_list[i] == '\t':
                text_list[i] = '&ensp;&ensp;&ensp;&ensp;'

        #split the text by paragraphs
        text = ''.join(text_list).split('\n')

        #add '<article>' '</article>' tag to each line to make sure each paragraph is a seperated.
        for i in range(len(text)):
            text[i]='<article>\n'+text[i]+'\n</article>\n'
        text = ''.join(text)
            
        #generate and return the content of the blog html
        template = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{title}</title>
            <link rel="stylesheet" href="/css/reset.css">
            <link rel="stylesheet" href="/css/main.css">
            <link rel="stylesheet" href="/css/nav.css">
            <link rel="stylesheet" href="/css/blogs.css">
        </head>
        <body>
            <!-- wrapper -->
            <div class="wrapper">
                <!-- header -->
                <div class="nheader">
                    <h2 class="ntitle">Midstreamblog</h2>
                    <h1 class="ntitle">{title}</h1>
                    <h3 class="ntitle">{date}</h3>
                </div>
                <div class="divider"></div>
            </div>
            <div class="divider"></div>
            <div class="wrapper">
                <div class="divider"></div>
                {article}
            </div>
            <div class="divider"></div>
            <div class="divider"></div>
            <div class="divider"></div>
            <div class="divider"></div>
            <div class="divider"></div>
        </body>
        <div class="sidebar">
            <a href="/index.html"><img class="home" src="/img/logo/home.png" alt="home"></a>
            <a href="/nav/{prevpage}"><img class="back" src="/img/logo/back.png" alt="back"></a>
            <a href="#"><img class="back-top" src="/img/logo/top.png" alt="back to top"></a>
        </div>
        </html>
        '''.format(title=self.title,date=self.post_time,article=text,prevpage=self.category+'.html')
        f.close()
        return template


    def gen_html(self):
        '''generate the blogpage html file in the right position'''

        #generate the path of the html file
        fname = self.blog_path + '/' + self.title + '.html'

        #avoid wrong submittion to cover the older blogs
        blog = self.Path(fname)
        if blog.exists():
            print('blog existed')
            raise IndexError

        #generate the html file and write the content in it
        else:
            f = open(fname,'w',encoding='utf-8')
            template = self.gen_template()
            f.write(template)
            f.close()


