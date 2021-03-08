import tkinter as tk
#import ctypes

muti_times = 0
muti_list = []

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
      
        
def Bahamut_Source_get():
    Entry_out.delete(0,"end")
    url = Entry_in.get()
    
    if 'pbs.twimg.com' in url:
        item = Twitter(url)
    elif 'www.pixiv.net' in url:
        item = Pixiv(url)
    else:
        return '錯誤的請求格式'
    
    item.order = Entry_order.get()
    if item.order != '0':
        if item.tag  == 'pixiv':
            try:
                item.order = int(item.order)
                item.img = 'https://pixiv.cat/%s-%s.jpg' % (item.key, item.order)
            except ValueError:
                return '序列值必須為整數'
            except:
                return 'Pixiv序列讀取發生不明錯誤'

        elif item.tag  == 'twitter':
            return 'Twitter 目前不支援圖片序列選取'
    
    Bahamut_Source = str('[/div][div][img=%s][/div][div][url=%s]%s[/url][/div]' %(item.img, item.url, item.tag))
    return Bahamut_Source


def end(output):
    Entry_in.delete(0,"end")
    Entry_order.delete(0,"end")
    Entry_order.insert(0, '0')
    Entry_out.insert(0, output)



def act():
    global muti_times, muti_list
    if muti_times == 0:
        end(Bahamut_Source_get())
    else:
        Bahamut_Source = ''
        
        for i in range(0, len(muti_list)):
            Bahamut_Source += muti_list[i]
            if i < len(muti_list)-1:
                Bahamut_Source += '[hr]'

        Entry_out.delete(0,"end")
        end(Bahamut_Source)
        muti_times = 0
        muti_list = []

def muti():
    global muti_times, muti_list
    Bahamut_Source = Bahamut_Source_get()
    
    if '[/div]' in Bahamut_Source:
        muti_list.append(Bahamut_Source)
        muti_times += 1
        end('%s 筆資料已儲存' %muti_times)
        
    else:
        end(Bahamut_Source)
        

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
Button = tk.Button(text = '輸出', command=act)
Button.place(x = 220, y = 220)

#多次按鈕
Button_muti = tk.Button(text = '暫存', command=muti)
Button_muti.place(x = 264, y = 220)


Entry_order.insert(0, '0')
#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid") #可能造成windows defender作用
#win.iconbitmap('icone.ico')
win.mainloop()


