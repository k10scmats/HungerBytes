from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from functools import partial
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import NumericProperty
from kivy.lang import Builder


Builder.load_string('''
#:import random random.random
#:import SlideTransition kivy.uix.screenmanager.SlideTransition

<CustomScreen>:
    Button:
        text: 'B1'
        size_hint: None, None
        pos_hint: {'right': 1}
        size: 150, 50
        on_press:   root.manager.transition = \
                    SlideTransition(direction="left")
        on_release: root.manager.current = root.manager.next()

    Button:
        text: 'B2'
        size_hint: None, None
        size: 150, 50
        on_press:   root.manager.transition = \
                    SlideTransition(direction="right")
        on_release: root.manager.current = root.manager.previous()

    BoxLayout:
        size_hint: .5, None
        height: 250
        pos_hint: {'center_x': .5}
        orientation: 'vertical'

        Button:
            text: 'B3'
            on_release: root.manager.transition = \
                        SlideTransition(direction="left")
''')


class CustomScreen(Screen):
    pass


class HBApp(App):

    def next_screen(self, *largs):
        pass

    def build(self):
        root = ScreenManager()
        for x in range(4):
            root.add_widget(CustomScreen(name='Screen %d' % x))
        return root


if __name__ == '__main__':
    HBApp().run()