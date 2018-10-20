from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_string('''
#:import random random.random
#:import SlideTransition kivy.uix.screenmanager.SlideTransition

<CustomScreen>:
    Image:
        source:'Main_Background.jpg'
        
    Button:
        text: 'Back'
        size_hint: None, None
        size: 150, 50
        on_press:   root.manager.transition = \
                    SlideTransition(direction="right")
        on_release: root.manager.current = root.manager.previous()
        
    Button:
        text: 'Next'
        size_hint: None, None
        pos_hint: {'right': 1}
        size: 150, 50
        on_press:   root.manager.transition = \
                    SlideTransition(direction="left")
        on_release: root.manager.current = root.manager.next()
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