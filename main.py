import random
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window

Window.size = (400, 600)

class Game(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.bird_y = 300
        self.velocity = 0
        self.gravity = -0.5

        self.pipe_x = 400
        self.pipe_gap = 200
        self.pipe_height = random.randint(100, 400)

        Clock.schedule_interval(self.update, 1/60)

    def on_touch_down(self, touch):
        self.velocity = 10

    def update(self, dt):
        self.canvas.clear()

        # Птица
        self.velocity += self.gravity
        self.bird_y += self.velocity

        # Трубы
        self.pipe_x -= 3
        if self.pipe_x < -50:
            self.pipe_x = 400
            self.pipe_height = random.randint(100, 400)

        with self.canvas:
            Color(1, 1, 0)
            Rectangle(pos=(100, self.bird_y), size=(30, 30))

            Color(0, 1, 0)
            Rectangle(pos=(self.pipe_x, 0), size=(50, self.pipe_height))
            Rectangle(pos=(self.pipe_x, self.pipe_height + self.pipe_gap), size=(50, 600))

class FlappyApp(App):
    def build(self):
        return Game()

FlappyApp().run()