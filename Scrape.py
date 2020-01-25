import argparse
from src.scraping.SearchForWord import SearchForWord
from src.scraping.SaveResultToFile import SaveResultToFile


class CommandLine:
    word = ""
    result = []

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
        readFormFile = False

        if argument.file:
            print("Mode : Read From File")
            readFormFile = True

        if argument.Help:
            print(
                "You have used '-p' or '--Help' with argument: {0}".format(argument.Help))

            return

        if not readFormFile:
            word = input("Enter your word: ")
            result = SearchForWord(word).paragraphs
            for item in result:
                print(item)
        else:
            # Read CSV File
            pass

        if argument.out:
            SaveResultToFile(argument.out, result)
            print(f"Result has been saved in {argument.out}")


if __name__ == '__main__':
    app = CommandLine()
