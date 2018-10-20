from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


Builder.load_string('''
#:import random random.random
#:import NoTransition kivy.uix.screenmanager.NoTransition

<DemoScreen>:
    Button:
        text: 'Back'
        size_hint: None, None
        size: 150, 50
        on_press:   root.manager.transition = NoTransition()
        on_release: root.manager.current = root.manager.previous()
        
    Button:
        text: 'Next'
        size_hint: None, None
        pos_hint: {'right': 1}
        size: 150, 50
        on_press:   root.manager.transition = NoTransition()
        on_release: root.manager.current = root.manager.next()

    Button:
        text: 'test'
        size_hint: None, None
        size: 150, 50
        pos: root.children[0].size[0] ,root.size[1] / 10

<HomeScreen>:
    Image:
        source:'Main_Background.jpg'

<IntroScreen>:
    Image:
        source:'Intro.jpg'

''')

class DemoScreen(Screen):
    pass


class HomeScreen(DemoScreen):
    pass


class IntroScreen(DemoScreen):
    pass


class HBApp(App):

    def next_screen(self, *largs):
        pass

    def build(self):
        root = ScreenManager()
        root.add_widget(HomeScreen(name='what'))
        root.add_widget(IntroScreen(name='whatt'))
        return root


if __name__ == '__main__':
    HBApp().run()