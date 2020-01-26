import os
from gtts import gTTS
import pygame
from io import BytesIO


class ReadItLoad():
    filePath = ""

    def __init__(self, filePath):
        self.filePath = filePath
        print("Prepare the text to speach")
        print("this can take a while please be patient.....")

        self.TextToSpeach()

    def TextToSpeach(self):
        text_to_read = ""
        with open(self.filePath, 'r', encoding="utf-8") as file:
            text_to_read = file.read().replace('\n', '')

        language = 'en'
        slow_audio_speed = False
        audio_created = gTTS(text=text_to_read, lang=language,
                             slow=slow_audio_speed)

        fp = BytesIO()
        audio_created.write_to_fp(fp)
        fp.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(fp)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
