from instagrapi import Client
from config import USER, PASS
import time
import random
import os

# dir_capt = caption
r = (random.randint(90, 200))



class InstaBot:
    cl = Client()
    cl.login(USER, PASS)
    def main(self):
        for i in os.listdir('C:\\Users\\Robert\\PycharmProjects\\autopost\\clips'):
            print(os.listdir("clips"))
            print(f'firstprint_{i}')
            PATH = f'C:\\Users\\Robert\\PycharmProjects\\autopost\\clips\\{i}'.strip()
            print(f'take C:\\Users\\Robert\\PycharmProjects\\autopost\\clips\\{i}')
            CAPTION = f'test{i}'.strip()
            print(f'caption test_{i}')
            print(f'secondprint_{i}')
            self.cl.clip_upload(PATH, CAPTION)
            time.sleep(r)
    def run(self):
        self.main()

if __name__ == '__main__':
    bot = InstaBot()
    bot.run()
# C:\Users\Robert\PycharmProjects\autopost\clips\first_file.mp4
#
#
# class InstaBot:
#     cl = Client()
#     cl.login(USER, PASS)
#     for i in os.listdir('C:\\Users\\Robert\\PycharmProjects\\autopost\\clips'):
#         print(os.listdir("clips"))
#         print(f'first_{i}')
#         PATH = f'C:\\Users\\Robert\\PycharmProjects\\autopost\\clips\\{i}'.strip()
#         print(f'take C:\\Users\\Robert\\PycharmProjects\\autopost\\clips\\{i}')
#         CAPTION = f'test{i}'.strip()
#         print(f'caption test_{i}')
#         print(f'second_{i}')
#     def main(self):
#         self.cl.clip_upload(self.PATH, self.CAPTION)
#         time.sleep(r)
#     def run(self):
#         self.main()
