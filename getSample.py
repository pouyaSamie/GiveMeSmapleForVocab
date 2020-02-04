import argparse


from src.scraping.SaveResultToFile import SaveResultToFile
from src.scraping.ReadItLoad import ReadItLoad

from src.InitSearch import SearchFormFile, Search


class CommandLine:
    word = ""
    result = []
    wordList = []
    maxParagNumber = 1

    def __init__(self):
        parser = argparse.ArgumentParser(
            description="Get Sample sentences of a word from reliable sources like news page. this library can help students who are studing IELTS, PTE,TOFEL and so on. ")
        parser.add_argument(
            "-H", "--Help", help="Show Help Menu", required=False, default="")
        parser.add_argument(
            "-f", "--file", help="Read Word from single line csv", required=False, default="")
        parser.add_argument(
            "-o", "--out", help="save result in an output file", required=False, default="")

        parser.add_argument(
            "-tts", "--tts", help="Read out load The Result (this feature need internet access)", required=False, default=False, action='store_true')

        parser.add_argument(
            "-n", "--NumberOfParagraphs", type=int, help="Number of paragraphs that will return", required=False, default=1)

        parser.add_argument(
            "-SaveAudio", "--SaveAudio", help="Save Audio File", required=False, default=False, action='store_true')
        argument = parser.parse_args()
        readFormFile = False

        if argument.file:
            print("Mode : Read From File")
            readFormFile = True

        if argument.Help:
            print(
                "You have used '-h' or '--Help' with argument: {0}".format(argument.Help))

            return
        if argument.NumberOfParagraphs > 1:
            self.maxParagNumber = argument.NumberOfParagraphs

        if not readFormFile:
            word = input("Enter your word: ")
            self.result = Search(word, self.maxParagNumber)
        else:
            self.result = SearchFormFile(argument.file, self.maxParagNumber)

        if argument.out:
            if self.result:
                SaveResultToFile(argument.out, self.result)
                print(f"Result has been saved in {argument.out}")
            else:
                print("No Result has been found.")
        if argument.tts:
            ReadItLoad(self.result, argument.SaveAudio)


if __name__ == '__main__':
    app = CommandLine()
