import csv


class ReadFromCsv():
    filePath = ""
    words = []

    def __init__(self, filePath):
        self.filePath = filePath

    def readCsv(self):
        with open(self.filePath, newline='') as f:
            reader = csv.reader(f)
            self.words = list(reader)
        f.close()

        return [item[0] for item in self.words]
