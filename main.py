from instagrapi import Client
from config import USER, PASS
import os

# dir_capt = caption

for i in os.listdir("clips"):
    class InstaBot:
        cl = Client()
        cl.login(USER, PASS)
        PATH = 'clips'
        CAPTION = ''

        def main(self):
            self.cl.clip_upload(self.PATH, self.CAPTION)

        def run(self):
            self.main()

if __name__ == '__main__':
    bot = InstaBot()
    bot.run()
