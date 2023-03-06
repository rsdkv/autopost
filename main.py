from instagrapi import Client
from config import USER, PASS
import time
import random
import os

path = 'C:\\Users\\Robert\\PycharmProjects\\autopost\\test2\\'

# dir_capt = caption
r = (random.randint(90, 200))


class InstaBot:
    cl = Client()
    cl.login(USER, PASS)

    def main(self):
        for i in os.listdir(path):
            # print(os.listdir(path))
            print(f'firstprint_{i}')
            PATH = path + f'{i}'.strip()
            print('take' + path + f'{i}')
            # print(f'take C:\\Users\\Robert\\PycharmProjects\\autopost\\test2\\{i}')
            # CAPTION = f'Название фильма ищите в телеграм канале\n\n\n\n\nКод фильма:{i}'.strip()
            CAPTION = 'Название фильма ищите в телеграм канале\n' + '.\n' + '.\n' + '.\n' + '.\n' + '.\n' + '.\n' + '.\n' + '.\n' + f'Код фильма:{i}'.replace(
                '.mp4', '')
            print(f'Описание фильма которое публикуется:\nНазвание фильма ищите в телеграм канале\n Код фильма:{i}')
            print(f'secondprint_{i}')
            self.cl.clip_upload(PATH, CAPTION)
            time.sleep(r)
            # цикл удаляющий .jpg в отдельный файл

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
