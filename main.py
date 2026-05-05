import random
import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image as KivyImage
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.core.window import Window

# Вибрация (работает только на Android)
try:
    from plyer import vibrator
    VIBRATOR_AVAILABLE = True
except:
    VIBRATOR_AVAILABLE = False

Window.clearcolor = (0.9, 0.95, 1, 1)

class GuboshlepkaGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 20

        self.score = 0
        self.combo = 0
        self.max_combo = 0
        self.current_type = None
        self.image_path = None

        # Абсолютные пути к папкам
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.natural_dir = os.path.join(BASE_DIR, 'images', 'natural')
        self.filler_dir = os.path.join(BASE_DIR, 'images', 'filler')
        self.sound_dir = os.path.join(BASE_DIR, 'sounds')

        # Загрузка звуков
        self.pop_sound = self.load_sound('pop.wav')
        self.slap_sound = self.load_sound('slap.wav')
        self.like_sound = self.load_sound('like.wav')

        # Верхняя панель: очки и комбо
        top_panel = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        self.score_label = Label(text='Очки: 0', font_size='24sp', color=(0,0,0,1))
        self.combo_label = Label(text='Комбо: x1', font_size='24sp', color=(1,0.4,0,1))
        top_panel.add_widget(self.score_label)
        top_panel.add_widget(self.combo_label)
        self.add_widget(top_panel)

        # Изображение губ
        self.image_widget = KivyImage(size_hint=(1, 0.7))
        self.add_widget(self.image_widget)

        # Кнопки с кастомными иконками
        button_panel = BoxLayout(orientation='horizontal', size_hint=(1, 0.15), spacing=20)

        self.like_btn = Button(
            background_normal='images/ui/like_btn.png',
            background_down='images/ui/like_btn.png',
            size=(150, 150),
            size_hint=(None, None))
        self.like_btn.bind(on_press=self.on_like)
        button_panel.add_widget(self.like_btn)

        self.swat_btn = Button(
            background_normal='images/ui/swat_btn.png',
            background_down='images/ui/swat_btn.png',
            size=(150, 150),
            size_hint=(None, None))
        self.swat_btn.bind(on_press=self.on_swat)
        button_panel.add_widget(self.swat_btn)

        self.add_widget(button_panel)

        # Старт игры
        self.load_random_image()

    def load_sound(self, filename):
        path = os.path.join(self.sound_dir, filename)
        if os.path.exists(path):
            return SoundLoader.load(path)
        return None

    def load_random_image(self):
        if random.random() < 0.5:
            self.current_type = 'natural'
            folder = self.natural_dir
        else:
            self.current_type = 'filler'
            folder = self.filler_dir

        if os.path.exists(folder):
            files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            if files:
                self.image_path = os.path.join(folder, random.choice(files))
                self.image_widget.source = self.image_path
            else:
                self.image_widget.source = ''
        else:
            self.image_widget.source = ''

        self.like_btn.disabled = False
        self.swat_btn.disabled = False

    def play_sound(self, sound):
        if sound:
            sound.stop()
            sound.play()

    def vibrate(self, duration=0.2):
        if VIBRATOR_AVAILABLE:
            try:
                vibrator.vibrate(duration)
            except:
                pass

    def on_like(self, instance):
        if self.current_type == 'natural':
            self.correct_answer('like')
        else:
            self.wrong_answer('like')

    def on_swat(self, instance):
        if self.current_type == 'filler':
            self.correct_answer('swat')
        else:
            self.wrong_answer('swat')

    def correct_answer(self, action):
        self.like_btn.disabled = True
        self.swat_btn.disabled = True
        self.combo += 1
        if self.combo > self.max_combo:
            self.max_combo = self.combo
        points = 1 * self.combo
        self.score += points
        self.score_label.text = f'Очки: {self.score}'
        self.combo_label.text = f'Комбо: x{self.combo}'

        if action == 'swat':
            self.play_sound(self.pop_sound)
            # Эффект лопания: показываем спрайт взрыва на 0,4 сек
            effect_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images', 'pop_effect.png')
            if os.path.exists(effect_path):
                self.image_widget.source = effect_path
            Clock.schedule_once(lambda dt: self.load_random_image(), 0.4)
        else:
            self.play_sound(self.like_sound)
            Clock.schedule_once(lambda dt: self.load_random_image(), 1.0)

    def wrong_answer(self, action):
        self.like_btn.disabled = True
        self.swat_btn.disabled = True
        self.combo = 0
        self.combo_label.text = 'Комбо: x1'
        self.play_sound(self.slap_sound)
        self.vibrate(0.3)
        Clock.schedule_once(lambda dt: self.load_random_image(), 1.5)

class GuboshlepkaApp(App):
    def build(self):
        return GuboshlepkaGame()

if __name__ == '__main__':
    GuboshlepkaApp().run()