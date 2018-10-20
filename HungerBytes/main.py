from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from functools import partial


class HBApp(App):

    def next_screen(self, *largs):
        pass

    def build(self):
        button1 = Button(text="B1")
                         #,on_press=partial(self.next_screen(self)))
        button2 = Button(text="B2")
        button3 = Button(text="B3")
        button4 = Button(text="B4")
        button5 = Button(text="B5")
        button6 = Button(text="B6")

        layout = BoxLayout(size_hint=(1, None), height=50)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        layout.add_widget(button5)
        layout.add_widget(button6)

        root = BoxLayout(orientation='vertical')
        root.add_widget(layout)

        filename = 'Main_Background.jpg'
        l1 = Image(source=filename, size=root.size)
        root.add_widget(l1)
        return root


if __name__ == '__main__':
    HBApp().run()