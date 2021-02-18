import requests
import time
import tkinter as tk
import tkinter.messagebox as msg
from PIL import Image
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from fake_useragent import UserAgent
from user_agent import generate_user_agent

def muti_pixiv_transfer():
    F = '油圖.txt'
    
    file = open(F,'r')
    
    for a in range(0,int((len(open(F,'r').readlines()) +1)/2)):
        number = file.readline()[-9:-1:1]
        print('[/div][div][img=https://pixiv.cat/', number,'.jpg][/div][div][url=https://www.pixiv.net/artworks/', number,']pixiv[/url][/div]', sep='')
        file.readline()
        
class Pixiv:
    def __init__(self, url):
        self.url = url
        self.key = self.url[-8:len(self.url)]
        self.img = 'https://pixiv.cat/%s.jpg' % self.key
        self.tag = 'pixiv'
        self.order = 0

class Twitter:
    def __init__(self, url):
        self.url = url
        self.key = self.url[28:self.url.find('?')]
        self.img = 'https://pbs.twimg.com/media/%s.jpg' % self.key
        self.tag = 'twitter'
        self.order = 0

def O():
    url = input('Enter URL :')
    if 'pbs.twimg.com' in url:
        item = Twitter(url)

    elif 'www.pixiv.net' in url:
        item = Pixiv(url)

    else:
        print ('Type not find.')
        return
    
    print('[/div][div][img=%s][/div][div][url=%s]%s[/url][/div]' %(item.img, item.url, item.tag))
    


def PIX():
   #url = input('Enter URL :')
   url = 'https://accounts.pixiv.net/login?return_to=https%3A%2F%2Fwww.pixiv.net%2F&lang=zh_tw&source=pc&view_type=page'
   options = Options()
   options.add_argument("--disable-notifications")
   chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
   chrome.get(url)
   

   email = chrome.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div[1]/div[1]/input")
   password = chrome.find_element_by_xpath("/html/body/div[4]/div[3]/div/form/div[1]/div[2]/input")
   
   email.send_keys('h89918011@yahoo.com.tw')
   password.send_keys('66276865')
   password.send_keys(Keys.ENTER)
   password.submit()

def TWI():
   #url = input('Enter URL :')
   url = 'https://twitter.com/en6cumxx0re6ffz/status/1346051774935781376'
   options = Options()
   options.add_argument("--disable-notifications")
   chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
   chrome.get(url)

   time.sleep(3)
   img = chrome.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/article/div/div/div/div[3]/div[2]/div/div/div/div/a/div/div[2]/div/img')
   print(img)
   
   soup = BeautifulSoup(chrome.page_source, 'html.parser')
   return soup.prettify()




def act():
    Entry_out.delete(0,"end")
    url = Entry_in.get()
    def end():
        Entry_out.insert(0, url)
        Entry_order.delete(0,"end")
        Entry_order.insert(0, '0')


    if 'pbs.twimg.com' in url:
        item = Twitter(url)

    elif 'www.pixiv.net' in url:
        item = Pixiv(url)

    else:
        url = 'Type not find.'
        end()
        return
    
    item.order = int(Entry_order.get())
    
    if item.order != 0:
        if item.tag  == 'pixiv':
            item.img = 'https://pixiv.cat/%s-%s.jpg' % (item.key, item.order)
        else:
            url = 'Twitter 目前不支援圖片序列選取'
            end()
            return
    
    url = str('[/div][div][img=%s][/div][div][url=%s]%s[/url][/div]' %(item.img, item.url, item.tag)) 
    end()

win = tk.Tk()
win.title('Chika')
win.geometry('384x288')


Button = tk.Button(text = '按鈕', command=act)
#Text = tk.Text()
Label = tk.Label(text = 'AAA')
Entry_in = tk.Entry()
Entry_out = tk.Entry()
Entry_order = tk.Entry(width = 3)

Entry_order.insert(0, '0')

Button.place(x = 180, y = 100)
#Text.place(x = 200, y = 300)
Label.place(x = 300, y = 400)
Entry_in.place(x = 125, y = 50)
Entry_out.place(x = 125, y = 200)
Entry_order.place(x = 125, y = 10)


win.mainloop()











































