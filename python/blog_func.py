class blog_func:
    from pathlib import Path
    import time
    import os

    def __init__(self, category='dailyblog', title=''):
        self.category = category
        self.title = title
        self.blog_path = './blogs/' + category
        self.post_time = self.time.strftime("%Y/%m/%d")
