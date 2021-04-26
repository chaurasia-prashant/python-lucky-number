from kivy.app import App
from kivy.lang import  Builder
from kivy.graphics import Color,Line,Rectangle,RoundedRectangle
from kivy.config import Config
from kivy.logger import Logger
from kivy.uix.screenmanager import ScreenManager,Screen


Config.set('graphics','resizable',True)

data1='c','e','f','h','i','m','o','q','w','y','z'
data2='b','k','l','t','v','x','p','u'
data3='a','d','g','i','n','s','r'
data4=1,2,3,4,5,6,7,8,9
class MainWindow1(Screen):
   def process(self):
       self.nam=self.ids.ip.text
       n=(self.nam)
       x=n.lower()
       if x!='':
           for i in data1:
               if i==x[0]:
                   y=int((len(x)*2-len(x)/2)/2)
                   self.ids.lb.text="[color=000000]                  Dear \n     {nam}\n   your lucky number is\n                 {num}[/color]".format(nam=x.title(),num=y)
                   return self.ids.lb.text
           for i in data2:
               if i==x[0]:
                   y=int((len(x)**2-(len(x)/2)/2))
                   self.ids.lb.text="[color=000000]                  Dear \n     {nam}\n   your lucky number is\n                 {num}[/color]".format(nam=x.title(),num=y)
                   return self.ids.lb.text
           for i in data3:
               if i==x[0]:
                   y=int(((len(x)/2)**2)/2)
                   self.ids.lb.text="[color=000000]                  Dear \n     {nam}\n   your lucky number is\n                 {num}[/color]".format(nam=x.title(),num=y)
                   return self.ids.lb.text
           for i in data3:
                self.ids.lb.text="[color=000000] Please Enter A Name[/color]"
                return self.ids.lb.text
       else:
           return ''

class MainWindow(ScreenManager):
    pass


kv=Builder.load_file('luckynumber.kv')
class MyApp(App):
    def build(self):
        self.title='Lucky Number'
        return kv

if __name__ == '__main__':
    MyApp().run()


