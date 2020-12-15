from kivy.app import App
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty(voices, voices[1].id)
rae = engine.getProperty('rate')
newVoiceRate = 150
engine.setProperty('rate', newVoiceRate)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def speak_file(file):
    file_open = open(file)
    file_str = str(file_open.read())
    speak(file_str)
class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.cols = 6
        self.sans_serif = Button(text="Info About\n Sans Serif")
        self.sans_serif.bind(on_press=lambda x: self.serif())
        self.add_widget(self.sans_serif)
        self.comic_sans = Button(text="Info About\n Comic Sans")
        self.comic_sans.bind(on_press=lambda x: self.comic())
        self.add_widget(self.comic_sans)
        self.blackletter = Button(text="Info About\n BlackLetter")
        self.blackletter.bind(on_press=lambda x: self.black())
        self.add_widget(self.blackletter)
        self.source_code_pro = Button(text="Info About\n Source code pro")
        self.source_code_pro.bind(on_press=lambda x: self.code())
        self.add_widget(self.source_code_pro)
        self.ubuntu = Button(text="Info About\n Ubuntu")
        self.ubuntu.bind(on_press=lambda x: self.bunty())
        self.add_widget(self.ubuntu)
        self.old_medieval = Button(text="Info About\n Roboto")
        self.old_medieval.bind(on_press=lambda x: self.old())
        self.add_widget(self.old_medieval)
    def serif(self):
        speak_file('serif.txt')
    def comic(self):
        speak_file('comic_sans.txt')
    def black(self):
        speak_file('blackletter.txt')
    def code(self):
        speak_file('source code pro.txt')
    def bunty(self):
        speak_file('ubuntu.txt')
    def old(self):
        speak_file('roboto')
class myApp(App):
    def build(self):
        Layout = MyLayout()
        return Layout
if __name__ == "__main__":
    myApp().run()