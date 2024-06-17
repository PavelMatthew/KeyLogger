from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

from project import Project
from doanalyze import DoAnalyze
from analizator import Analizator

from threading import Thread
import keyboard
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from kivy.core.window import Window



kv = '''
RelativeLayout:
    orientation: 'vertical'
    
    Label:
        size_hint:(1, .1)
        pos_hint:{'x': 0, 'top': 1}
        halign:'center'
        font_size:'33sp'
        text:' '
     
    Button:
        size_hint:(.40, .1)
        pos_hint:{'x': 0.1, 'top': 0.20}
        font_size:'33sp'
        halign:'center'
        background_color: 0, 1, 0, 1
        text: app.changeAnalyze
        on_press: app.startAnalyze(self)
        
    Button:
        size_hint:(.40, .1)
        pos_hint:{'x': 0.5, 'top': 0.20}
        font_size:'33sp'
        halign:'center'
        background_color: 0, 1, 0, 1
        text: app.changeShow
        on_press: app.startShow(self)
  
        
    
    Button:
        size_hint:(.15, .1)
        pos_hint:{'x':0.75, 'top': 0.90}
        font_size:'33sp'
        halign:'center'
        background_color: 0, 1, 0, 1
        text: app.pausePlay
        on_press: app.changePausePlay(self)
'''


class KeyLogApp(App):
    pausePlay = StringProperty('Старт')
    changeAnalyze = StringProperty('Анализ')
    changeShow = StringProperty('Показать')
    #changeKey = StringProperty('Key')
    #changeLog = StringProperty('Log')

    def __init__(self, **kwargs):
        super(KeyLogApp, self).__init__(**kwargs)


    def build(self):
        layout = Builder.load_string(kv)

        self.text_input = TextInput(hint_text='Введите имя пользователя',pos_hint = {'x': 0.1, 'top': 0.90}, multiline=False, size_hint=(.65, .1),font_size = '33sp')
        self.log_text = Label(size_hint =(.8, .6), pos_hint={'x': 0.18, 'center_y': 0.5},font_size = '66sp',halign='center',color=(0, 125, 0, 1),text='Log')
        self.key_text = Label(size_hint=(.8, .6), pos_hint={'x': 0.01, 'center_y': 0.5}, font_size='88sp',halign='center',color=(1, 1, 1, 1), text='Key',font_name='Comic')
        layout.add_widget(self.text_input)
        layout.add_widget(self.log_text)
        layout.add_widget(self.key_text)

        return layout

    def print_text(self, instance):
        print(self.text_input.text)


    def changePausePlay(self, button):



        if self.pausePlay == "Старт":
            name = self.text_input.text
            r = Project(name)
            self.print_text("")

            daemon = Thread(target=r.result_arr, daemon=True, name='Monitor1')
            self.pausePlay = "Стоп"

            #r.result_arr()

            #daemon = Thread(target=r.result_arr, daemon=True, name='Monitor')
            daemon.start()

        elif self.pausePlay == "Стоп":
           # daemon.terminate()



            keyboard.press("alt+f10")
            keyboard.release("alt+f10")

            self.pausePlay = "Старт"

    def startAnalyze(self, button):

        if self.changeAnalyze == "Анализ":

            r = DoAnalyze("Анализируемый")
            self.print_text("")

            daemon = Thread(target=r.result_arr, daemon=True, name='Monitor2')
            self.changeAnalyze = "Стоп"
            daemon.start()

        elif self.changeAnalyze == "Стоп":

            keyboard.press("alt+f10")
            keyboard.release("alt+f10")

            self.changeAnalyze = "Анализ"

    def startShow(self, button):

        if self.changeShow == "Показать":



            self.changeShow = "Скрыть"
            #self.changeKey = StringProperty(' ')
            #self.changeLog = StringProperty(' ')
            #Пасхалка
            if self.text_input.text == '<3':
                self.key_text.text = 'Love'
                self.log_text.text = '  You'
            else:
                self.key_text.text = ''
                self.log_text.text = ''
                a = Analizator()
                self.key_text.font_size = '12'
                self.key_text.pos_hint={'center_x': 0.5, 'center_y': 0.5}
                self.key_text.text = str(a.find_txt())+str(a.find_n_m())+'\n'+str(a.find_m_t_p())+'\n'+str(a.find_m_s())+'\n'+str(a.find_m_s_w_b_p())+'\n'+str(a.find_d_p())+'\n'+str(a.find_d_s())
                self.log_text.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
                self.log_text.text = str(a.most_common())

        elif self.changeShow == "Скрыть":



            self.changeShow = "Показать"
            self.key_text.pos_hint = {'x': 0.01, 'center_y': 0.5}
            self.log_text.pos_hint = {'x': 0.18, 'center_y': 0.5}
            self.key_text.text = 'Key'
            self.log_text.text = 'Log'
            self.key_text.font_size = '88'

            #self.changeKey = StringProperty('Key')
            #self.changeLog = StringProperty('Log')

if __name__ == "__main__":
    KeyLogApp().run()






