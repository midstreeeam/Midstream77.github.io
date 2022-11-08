class blog_func:
    from pathlib import Path
    import time
    import os

    def __init__(self, tags, title='', time=''):
        self.tags = tags
        self.title = title
        self.blog_path = './blogs'
        self.post_time = time

        if(time==''):
            self.post_time = self.time.strftime("%Y/%m/%d")

        f = open("input.txt", "r", encoding="utf-8")
        self.pre = f.read(100)+'……'
        f.close()
