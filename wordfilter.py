class WordFilter:
    def __init__(self, ng_word):
        self.ng_word = ng_word

    def detect(self, in_word):
        return self.ng_word in in_word

    def censor(self, in_word):
        cens_str = in_word.replace(self.ng_word, '<censored>')
        return cens_str


def main():
    in_str = "昨日のアーセナルの試合アツかった！"

    my_filter = WordFilter("アーセナル")

    # NGワードが含まれている場合
    my_filter.detect("昨日のアーセナルの試合アツかった！")  # Trueを返す ※出力されるわけではありません！

    # NGワードが含まれていない場合
    my_filter.detect("昨日のリバプールの試合アツかった！")  # Falseを返す ※出力されるわけではありません！

    # NGワードが含まれている場合
    print(my_filter.censor("昨日のアーセナルの試合アツかった！"))  # "昨日の<censored>の試合アツかった！" を返す ※出力されるわけではありません！

    # NGワードが含まれていない場合
    print(my_filter.censor("昨日のリバプールの試合アツかった！"))  # "昨日のリバプールの試合アツかった！" を返す ※出力されるわけではありません！


if __name__ == '__main__':
    main()
