class WordFilter:
    def __init__(self, ng_word):
        self.ng_word = ng_word

    def detect(self, in_word):
        for i in self.ng_word:
            if i in in_word:
                return True

        return False

    def censor(self, in_word, rep):
        for i in self.ng_word:
            print(i)
            in_word = in_word.replace(i, rep)

        return in_word


def main():
    # 入力
    in_str = "昨日のアーセナルの試合アツかった！"
    rep_word = "<見せられないよ!>"
    ng_list = ['アーセナル', 'アツかった']

    my_filter = WordFilter(ng_list)

    # NGワードが含まれている場合
    my_filter.detect(in_str)  # Trueを返す ※出力されるわけではありません！

    # NGワードが含まれていない場合
    my_filter.detect(in_str)  # Falseを返す ※出力されるわけではありません！

    print(my_filter.censor(in_str, rep_word))
    print(my_filter.censor('昨日のリバプールの試合アツかった！', rep_word))


if __name__ == '__main__':
    main()
