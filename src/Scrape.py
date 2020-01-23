import argparse
from scraping.SearchForWord import SearchForWord


class CommandLine:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Get Sample sentences of a word from reliable sources like news page. this library can help students who are studing IELTS, PTE,TOFEL and so on. ")
        parser.add_argument(
            "-H", "--Help", help="Example: Help argument", required=False, default="")
        parser.add_argument(
            "-f", "--file", help="Read Word from single line csv", required=False, default="")
        parser.add_argument(
            "-o", "--out", help="save result in an output file", required=False, default="")

        argument = parser.parse_args()
        status = False

        if argument.file:
            print("Mode : Read From File")
            status = True
        if argument.out:
            print("Mode : Save File to Desierd Location")
            status = True
        if argument.Help:
            print(
                "You have used '-p' or '--Help' with argument: {0}".format(argument.Help))
            status = True

        if not status:
            word = input("Enter your word: ")
            result = SearchForWord(word).paragraphs
            for item in result:
                print(item)


if __name__ == '__main__':
    app = CommandLine()
