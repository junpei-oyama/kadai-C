class WordFilter:
    def __init__(self, ng_word):
        self.ng_word = ng_word

    def detect(self, in_word):
        return self.ng_word in in_word

    def censor(self, in_word, rep):
        cens_str = in_word.replace(self.ng_word, rep)
        return cens_str


def main():
    # 入力
    in_str = "昨日のアーセナルの試合アツかった！"
    rep_word = "<見せられないよ!>"

    my_filter = WordFilter("アーセナル")

    # NGワードが含まれている場合
    my_filter.detect(in_str)  # Trueを返す ※出力されるわけではありません！

    # NGワードが含まれていない場合
    my_filter.detect(in_str)  # Falseを返す ※出力されるわけではありません！

    print(my_filter.censor(in_str, rep_word))
    print(my_filter.censor('昨日のリバプールの試合アツかった！', rep_word))


if __name__ == '__main__':
    main()
