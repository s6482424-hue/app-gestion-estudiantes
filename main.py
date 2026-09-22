from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore

KV = r"""
#:import dp kivy.metrics.dp

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
        spacing: dp(15)
        Label:
            text: "GESTIÓN DE ESTUDIANTES"
            font_size: dp(25)
            bold: True
            size_hint_y: None
            height: dp(60)
        Button:
            text: "Registrar estudiante"
            on_release: root.manager.current = "register"
        Button:
            text: "Ver estudiantes"
            on_release: root.manager.current = "students"
        Button:
            text: "Registrar / ver calificaciones"
            on_release: root.manager.current = "grades"

<RegisterScreen>:
    name: "register"
    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(10)
        Label:
            text: "Registrar estudiante"
            font_size: dp(24)
            bold: True
            size_hint_y: None
            height: dp(55)
        TextInput:
            id: name
            hint_text: "Nombre completo"
            multiline: False
        TextInput:
            id: grade
            hint_text: "Grado / sección"
            multiline: False
        TextInput:
            id: subject
            hint_text: "Asignatura principal"
            multiline: False
        Label:
            id: msg
            text: ""
        Button:
            text: "Guardar estudiante"
            size_hint_y: None
            height: dp(50)
            on_release: root.save_student()
        Button:
            text: "Volver al menú"
            size_hint_y: None
            height: dp(50)
            on_release: root.manager.current = "menu"

<StudentsScreen>:
    name: "students"
    BoxLayout:
        orientation: "vertical"
        padding: dp(15)
        spacing: dp(10)
        Label:
            text: "Lista de estudiantes"
            font_size: dp(24)
            bold: True
            size_hint_y: None
            height: dp(55)
        ScrollView:
            GridLayout:
                id: list_box
                cols: 1
                spacing: dp(8)
                size_hint_y: None
                height: self.minimum_height
        Button:
            text: "Actualizar lista"
            size_hint_y: None
            height: dp(50)
            on_release: root.refresh()
        Button:
            text: "Volver al menú"
            size_hint_y: None
            height: dp(50)
            on_release: root.manager.current = "menu"

<GradesScreen>:
    name: "grades"
    BoxLayout:
        orientation: "vertical"
        padding: dp(15)
        spacing: dp(10)
        Label:
            text: "Calificaciones"
            font_size: dp(24)
            bold: True
            size_hint_y: None
            height: dp(55)
        TextInput:
            id: student
            hint_text: "Nombre exacto del estudiante"
            multiline: False
        TextInput:
            id: n1
            hint_text: "Nota 1 (0-100)"
            input_filter: "float"
            multiline: False
        TextInput:
            id: n2
            hint_text: "Nota 2 (0-100)"
            input_filter: "float"
            multiline: False
        TextInput:
            id: n3
            hint_text: "Nota 3 (0-100)"
            input_filter: "float"
            multiline: False
        Label:
            id: result
            text: ""
            font_size: dp(18)
        Button:
            text: "Guardar notas y calcular promedio"
            size_hint_y: None
            height: dp(55)
            on_release: root.save_grades()
        Button:
            text: "Volver al menú"
            size_hint_y: None
            height: dp(50)
            on_release: root.manager.current = "menu"
"""

store = JsonStore("estudiantes.json")

class MenuScreen(Screen):
    pass

class RegisterScreen(Screen):
    def save_student(self):
        name = self.ids.name.text.strip()
        grade = self.ids.grade.text.strip()
        subject = self.ids.subject.text.strip()
        if not name or not grade:
            self.ids.msg.text = "Completa nombre y grado."
            return
        key = name.lower().replace(" ", "_")
        if store.exists(key):
            self.ids.msg.text = "Ese estudiante ya existe."
            return
        store.put(key, name=name, grade=grade, subject=subject,
                  notes=[0, 0, 0], average=0)
        self.ids.msg.text = "Estudiante guardado correctamente."
        self.ids.name.text = ""
        self.ids.grade.text = ""
        self.ids.subject.text = ""

class StudentsScreen(Screen):
    def on_pre_enter(self):
        self.refresh()

    def refresh(self):
        box = self.ids.list_box
        box.clear_widgets()
        for key in store:
            data = store.get(key)
            notes = data.get("notes", [0,0,0])
            avg = data.get("average", 0)
            from kivy.uix.label import Label
            from kivy.uix.button import Button
            from kivy.uix.boxlayout import BoxLayout
            row = BoxLayout(size_hint_y=None, height=110, orientation="vertical")
            row.add_widget(Label(
                text=f"{data['name']} | {data['grade']}\n"
                     f"Asignatura: {data.get('subject','')}\n"
                     f"Notas: {notes[0]}, {notes[1]}, {notes[2]} | Promedio: {avg:.2f}"
            ))
            btn = Button(text="Eliminar", size_hint_y=None, height=40)
            btn.bind(on_release=lambda b, k=key: self.delete_student(k))
            row.add_widget(btn)
            box.add_widget(row)

    def delete_student(self, key):
        store.delete(key)
        self.refresh()

class GradesScreen(Screen):
    def save_grades(self):
        name = self.ids.student.text.strip()
        key = name.lower().replace(" ", "_")
        if not store.exists(key):
            self.ids.result.text = "No se encontró ese estudiante."
            return
        try:
            notes = [float(self.ids.n1.text), float(self.ids.n2.text), float(self.ids.n3.text)]
            if any(n < 0 or n > 100 for n in notes):
                raise ValueError
        except ValueError:
            self.ids.result.text = "Las notas deben estar entre 0 y 100."
            return
        avg = sum(notes) / 3
        data = store.get(key)
        store.put(key, name=data["name"], grade=data["grade"],
                  subject=data.get("subject",""), notes=notes, average=avg)
        estado = "Aprobado" if avg >= 60 else "Reprobado"
        self.ids.result.text = f"Promedio: {avg:.2f} — {estado}"

class EstudiantesApp(App):
    def build(self):
        return Builder.load_string(KV)

if __name__ == "__main__":
    EstudiantesApp().run()
