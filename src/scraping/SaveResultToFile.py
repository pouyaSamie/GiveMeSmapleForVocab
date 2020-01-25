

class SaveResultToFile:
    location = ""
    paragraphs = ""

    def __init__(self, location, paragraphs):
        self.location = location
        self.paragraphs = paragraphs
        self.savePragraphsToFile()

    def savePragraphsToFile(self):
        with open(self.location, 'w', encoding="utf-8") as f:
            for item in self.paragraphs:
                f.write("%s\r\n" % item)

            f.close()
