from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.utils import platform

if platform == 'android':
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Context = autoclass('android.content.Context')
    vibrator = PythonActivity.mActivity.getSystemService(Context.VIBRATOR_SERVICE)

Window.fullscreen = 'auto'

PASSWORD = "to chto"
MAX_ATTEMPTS = 10

class LockScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.attempts = 0

        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        self.label = Label(text="пиши пароль, или пока телефону:", font_size=28)
        self.input = TextInput(password=True, multiline=False, font_size=24, size_hint=(1, 0.2))
        btn = Button(text="Разблокировать", font_size=24, size_hint=(1, 0.3))
        btn.bind(on_press=self.check_password)

        layout.add_widget(self.label)
        layout.add_widget(self.input)
        layout.add_widget(btn)
        self.add_widget(layout)

    def check_password(self, instance):
        if self.input.text == PASSWORD:
            self.manager.current = 'rating'
        else:
            self.attempts += 1
            if self.attempts >= MAX_ATTEMPTS:
                self.show_popup("Ошибка", "Превышено число попыток! Перезапуск...")
                Clock.schedule_once(lambda dt: App.get_running_app().stop(), 2)
            else:
                self.show_popup("Ошибка", f"Неверный пароль! Осталось попыток: {MAX_ATTEMPTS - self.attempts}")

    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message, font_size=20),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

class RatingScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        self.layout.add_widget(Label(text="Оцени вирус То Что от 1 до 5 звёзд", font_size=28))

        for i in range(1, 6):
            btn = Button(text=f"{i} ★", font_size=28)
            btn.bind(on_press=lambda instance, rate=i: self.submit_rating(rate))
            self.layout.add_widget(btn)

        self.add_widget(self.layout)

    def submit_rating(self, rating):
        if rating == 1:
            self.trigger_vibration()
            self.show_fake_bsod("😈", "Оценка 1? Телефону конец!")
        elif rating == 2:
            self.trigger_vibration()
            self.show_fake_bsod("ну все гг))")
            Clock.schedule_once(lambda dt: App.get_running_app().stop(), 5)
        elif rating == 3:
            self.show_popup("Перезагрузка")
            Clock.schedule_once(lambda dt: App.get_running_app().stop(), 2)
        elif rating == 4:
            self.show_popup("Спасибо")
        elif rating == 5:
            self.show_popup("Удаление", "Удаляем себя... (почти)")
            Clock.schedule_once(lambda dt: App.get_running_app().stop(), 2)

    def trigger_vibration(self):
        if platform == 'android':
            try:
                vibrator.vibrate(500)
            except:
                pass

    def show_popup(self, title, message=""):
        popup = Popup(title=title,
                      content=Label(text=message, font_size=20),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def show_fake_bsod(self, title, message=""):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)
        layout.add_widget(Label(text="😵 СИСТЕМА СЛОМАНА 😵", font_size=32, color=(0, 0.5, 1, 1)))
        layout.add_widget(Label(text=message, font_size=24))
        self.add_widget(layout)

class VirusApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LockScreen(name='lock'))
        sm.add_widget(RatingScreen(name='rating'))
        return sm

if __name__ == '__main__':
    VirusApp().run()