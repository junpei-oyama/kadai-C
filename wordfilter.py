class WordFilter:
    def __init__(self, ng_word):
        self.ng_word = ng_word

    def detect(self, in_word):
        return self.ng_word in in_word


def main():
    in_str = '昨日のアーセナルの試合アツかった！'

    my_filter = WordFilter("アーセナル")

    # NGワードが含まれている場合
    my_filter.detect("昨日のアーセナルの試合アツかった！")  # Trueを返す ※出力されるわけではありません！

    # NGワードが含まれていない場合
    my_filter.detect("昨日のリバプールの試合アツかった！")  # Falseを返す ※出力されるわけではありません！


if __name__ == '__main__':
    main()
