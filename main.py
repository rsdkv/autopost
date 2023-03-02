from instagrapi import Client
from config import USER, PASS
class InstaBot:
    cl=Client()
    cl.login(USER, PASS)
    PATH=''
    CAPTION='test'
    def main(self):
        self.cl.clip_upload(self.PATH,self.CAPTION)
    def run(self):
        self.main()

if __name__ == '__main__':
    bot=InstaBot()
    bot.run()
