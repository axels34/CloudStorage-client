from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import tkinter as tk
from tkinter import filedialog
from kivy.app import App
import alo
z = ""
from kivy.config import Config
Config.set('graphics', 'resizable', True)
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')
Config.write()


def get_path():
    root = tk.Tk()
    root.withdraw()

    return filedialog.askopenfilename()


class Login(Screen):
    def do_login(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="login")
        self.manager.current = 'login'
        app.config.read(app.get_application_config())
        app.config.write()

    def do_vhod(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'vhod'
        app.config.read(app.get_application_config())
        app.config.write()

    def do_reg(self):
        app = App.get_running_app()
        #app.username = loginText
        #app.password = passwordText
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'registration'
        app.config.read(app.get_application_config())
        app.config.write()


class registration(Screen):

    def do_reg2(self, login, password, email):
        alo.otprreg(login, email, password)
        self.ids['email'].text = ""
        self.ids['login'].text = ""
        self.ids['password'].text = ""
    def do_est(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'vhod'

    def do_nazad(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Login'


class vhod(Screen):

    def do_reg(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'registration'


    def do_vhod(self, password, email):
        global z
        #z = alo.otprvhod(email, password)
        #alo.otprtinf(z)
        print("Вы вошли,", email)
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'glavnoe'

        self.ids['email'].text = ""
        self.ids['password'].text = ""
    def do_nazad(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'Login'



class glavnoe(Screen):

    def do_reg(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'registration'

    def do_est(self):
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'vhod'

    def do_upload(self):
        path = ""
        while path =="":
            path = get_path()
        #print(z)
        alo.otprup(z, path)
        alo.otprtinf(z)
    def do_download(self):
        #print(z)
        alo.otprdown(z)
    def do_vihod(self):
        global z
        z = ""
        app = App.get_running_app()
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'vhod'

    def do_del(self):
        alo.otprdel(z)
        alo.otprtinf(z)


class LoginApp(App):

    def build(self):
        manager = ScreenManager()
        self.title = 'Cloud Storage'
        manager.add_widget(vhod(name='vhod'))
        manager.add_widget(registration(name='registration'))
        manager.add_widget(glavnoe(name='glavnoe'))
        return manager


if __name__ == '__main__':
    LoginApp().run()
