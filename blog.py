class Blog:

    def write_blog(self):
        print(“日付を入力してください”)
        self.date = input()
        print(“タイトルを入力してください”)
        self.title = input()
        print(“本文を入力してください”)
        self.contents = input()