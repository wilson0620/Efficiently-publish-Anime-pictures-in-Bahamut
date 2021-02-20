import tkinter as tk
#import ctypes

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
        
def act():
    Entry_out.delete(0,"end")
    url = Entry_in.get()
    def end():
        Entry_out.insert(0, url)
        Entry_in.delete(0,"end")
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
win.title('Chika Image Converter')
win.geometry('528x293')
win.resizable(width=0, height=0)
'''
#背景
photo = tk.PhotoImage(file="BK.png")
BK = tk.Label(image=photo)
BK.pack()
'''
#輸入網址框
Entry_in = tk.Entry()
Entry_in.place(x = 190, y = 50)

#輸入次序框
Entry_order = tk.Entry(width = 3)
Entry_order.place(x = 249, y = 82)

#輸出框
Entry_out = tk.Entry()
Entry_out.place(x = 190, y = 255)

#按鈕
Button = tk.Button(text = '轉換', command=act)
Button.place(x = 247, y = 220)



Entry_order.insert(0, '0')
##ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid") #可能造成windows defender作用
#win.iconbitmap('icone.ico')
win.mainloop()




