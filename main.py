from kivy.app import App
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp

store = JsonStore("estudiantes.json")

KV = """
#:import dp kivy.metrics.dp

<Screen>:
    canvas.before:
        Color:
            rgba: 0.94, 0.96, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

<BlueButton@Button>:
    background_normal: ""
    background_color: 0.10, 0.40, 0.80, 1
    color: 1, 1, 1, 1
    font_size: dp(17)
    bold: True
    size_hint_y: None
    height: dp(55)

<GreenButton@Button>:
    background_normal: ""
    background_color: 0.10, 0.60, 0.35, 1
    color: 1, 1, 1, 1
    font_size: dp(17)
    bold: True
    size_hint_y: None
    height: dp(55)

<PurpleButton@Button>:
    background_normal: ""
    background_color: 0.45, 0.25, 0.75, 1
    color: 1, 1, 1, 1
    font_size: dp(17)
    bold: True
    size_hint_y: None
    height: dp(55)

<OrangeButton@Button>:
    background_normal: ""
    background_color: 0.90, 0.55, 0.08, 1
    color: 1, 1, 1, 1
    font_size: dp(17)
    bold: True
    size_hint_y: None
    height: dp(55)

<GrayButton@Button>:
    background_normal: ""
    background_color: 0.35, 0.40, 0.50, 1
    color: 1, 1, 1, 1
    font_size: dp(16)
    bold: True
    size_hint_y: None
    height: dp(50)

ScreenManager:
    MenuScreen:
    RegisterScreen:
    StudentsScreen:
    GradesScreen:


<MenuScreen>:
    name: "menu"

    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(12)

        Label:
            text: "GESTION DE ESTUDIANTES"
            font_size: dp(26)
            bold: True
            color: 0.05, 0.25, 0.60, 1
            size_hint_y: None
            height: dp(55)

        Label:
            text: "Sistema de control academico"
            font_size: dp(16)
            color: 0.30, 0.35, 0.45, 1
            size_hint_y: None
            height: dp(35)

        BoxLayout:
            size_hint_y: None
            height: dp(95)
            spacing: dp(10)

            BoxLayout:
                orientation: "vertical"

                Label:
                    text: "ESTUDIANTES"
                    font_size: dp(13)
                    color: 0.15, 0.30, 0.60, 1

                Label:
                    id: total
                    text: "0"
                    font_size: dp(27)
                    bold: True
                    color: 0.05, 0.35, 0.75, 1

            BoxLayout:
                orientation: "vertical"

                Label:
                    text: "PROMEDIO GENERAL"
                    font_size: dp(13)
                    color: 0.10, 0.45, 0.25, 1

                Label:
                    id: promedio
                    text: "0.00"
                    font_size: dp(27)
                    bold: True
                    color: 0.05, 0.55
                    """