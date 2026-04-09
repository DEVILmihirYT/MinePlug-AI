from kivy.app import App
from kivy.uix.label import Label

class MinePlugApp(App):
    def build(self):
        return Label(text='MinePlug AI is Loading...')

if __name__ == '__main__':
    MinePlugApp().run()
  
