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
    in_str = input('検索対象文字列を入力 -> ')
    ng_list = input("NGワードを入力(複数の場合はスペース区切り) -> ").split(' ')
    rep_word = input("NGワードを置換する文字列を入力 -> ")

    my_filter = WordFilter(ng_list)

    print(my_filter.censor(in_str, rep_word))
    print(my_filter.censor('昨日のリバプールの試合アツかった！', rep_word))


if __name__ == '__main__':
    main()
