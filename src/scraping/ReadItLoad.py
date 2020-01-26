import os
from gtts import gTTS
import pygame
from io import BytesIO
import uuid


class ReadItLoad():
    parags = ""
    saveAudio = False

    def __init__(self, parags, saveAudio):
        self.parags = parags
        self.saveAudio = saveAudio
        print("Prepare the text to speech")
        print("this can take a while please be patient.....")
        for item in parags:
            self.TextToSpeech(item)

    def TextToSpeech(self, text_to_read):
        # with open(self.filePath, 'r', encoding="utf-8") as file:
        #     text_to_read = file.read().replace('\n', '')

        language = 'en'
        slow_audio_speed = False
        audio_created = gTTS(text=text_to_read, lang=language,
                             slow=slow_audio_speed)
        print("reading: " + text_to_read[0:50] + "...")
        if self.saveAudio:
            tempFileName = str(uuid.uuid4())
            audio_created.save(f"{text_to_read[0:10]}.mp3")

        fp = BytesIO()
        audio_created.write_to_fp(fp)
        fp.seek(0)
        pygame.mixer.init()
        pygame.mixer.music.load(fp)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
