from kivy.app import App
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp

store = JsonStore("estudiantes.json")

KV = """
#:import dp kivy.metrics.dp

<ModernButton@Button>:
    background_normal: ""
    background_color: 0.10, 0.35, 0.75, 1
    color: 1, 1, 1, 1
    font_size: dp(17)
    bold: True
    size_hint_y: None
    height: dp(55)

<CardLabel@Label>:
    color: 0.12, 0.16, 0.24, 1
    font_size: dp(16)

<Screen>:
    canvas.before:
        Color:
            rgba: 0.94, 0.96, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

ScreenManager:
    MenuScreen:
    RegisterScreen:
    StudentsScreen:
    GradesScreen:


<MenuScreen>:
    name: "menu"

    BoxLayout:
        orientation: "vertical"
        padding: dp(18)
        spacing: dp(12)

        # ENCABEZADO
        BoxLayout:
            orientation: "vertical"
            size_hint_y: None
            height: dp(105)

            Label:
                text: "🎓"
                font_size: dp(38)
                size_hint_y: None
                height: dp(45)

            Label:
                text: "GESTIÓN DE ESTUDIANTES"
                font_size: dp(25)
                bold: True
                color: 0.06, 0.25, 0.60, 1

            Label:
                text: "Control académico"
                font_size: dp(15)
                color: 0.35, 0.40, 0.50, 1

        # TARJETAS DE RESUMEN
        BoxLayout:
            spacing: dp(8)
            size_hint_y: None
            height: dp(105)

            BoxLayout:
                orientation: "vertical"
                padding: dp(8)
                canvas.before:
                    Color:
                        rgba: 0.82, 0.91, 1, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [15]

                Label:
                    text: "👥"
                    font_size: dp(25)

                Label:
                    id: total
                    text: "0"
                    font_size: dp(23)
                    bold: True
                    color: 0.05, 0.30, 0.70, 1

                Label:
                    text: "Estudiantes"
                    font_size: dp(12)
                    color: 0.25, 0.30, 0.40, 1

            BoxLayout:
                orientation: "vertical"
                padding: dp(8)
                canvas.before:
                    Color:
                        rgba: 0.84, 0.96, 0.88, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [15]

                Label:
                    text: "📈"
                    font_size: dp(25)

                Label:
                    id: promedio
                    text: "0.00"
                    font_size: dp(23)
                    bold: True
                    color: 0.05, 0.50, 0.25, 1

                Label:
                    text: "Promedio general"
                    font_size: dp(12)
                    color: 0.25, 0.30, 0.40, 1

        # BOTONES PRINCIPALES
        ModernButton:
            text: "👨‍🎓   REGISTRAR ESTUDIANTE"
            background_color: 0.08, 0.38, 0.78, 1
            on_release: root.manager.current = "register"

        ModernButton:
            text: "📋   VER ESTUDIANTES"
            background_color: 0.42, 0.25, 0.72, 1
            on_release: root.manager.current = "students"

        ModernButton:
            text: "📝   CALIFICACIONES"
            background_color: 0.08, 0.58, 0.38, 1
            on_release: root.manager.current = "grades"

        ModernButton:
            text: "📊   ESTADÍSTICAS DEL GRUPO"
            background_color: 0.90, 0.55, 0.08, 1
            on_release: root.manager.current = "students"


<RegisterScreen>:
    name: "register"

    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(12)

        Label:
            text: "👨‍🎓"
            font_size: dp(38)
            size_hint_y: None
            height: dp(45)

        Label:
            text: "REGISTRAR ESTUDIANTE"
            font_size: dp(24)
            bold: True
            color: 0.06, 0.25, 0.60, 1
            size_hint_y: None
            height: dp(45)

        TextInput:
            id: name
            hint_text: "👤  Nombre completo"
            multiline: False
            font_size: dp(17)
            padding: dp(12)

        TextInput:
            id: grade
            hint_text: "🏫  Grado / sección"
            multiline: False
            font_size: dp(17)
            padding: dp(12)

        TextInput:
            id: subject
            hint_text: "📚  Asignatura principal"
            multiline: False
            font_size: dp(17)
            padding: dp(12)

        Label:
            id: msg
            text: ""
            font_size: dp(16)
            color: 0.05, 0.55, 0.30, 1

        ModernButton:
            text: "💾   GUARDAR ESTUDIANTE"
            background_color: 0.08, 0.58, 0.38, 1
            on_release: root.save_student()

        ModernButton:
            text: "←   VOLVER AL MENÚ"
            background_color: 0.35, 0.40, 0.50, 1
            on_release: root.manager.current = "menu"


<StudentsScreen>:
    name: "students"

    BoxLayout:
        orientation: "vertical"
        padding: dp(12)
        spacing: dp(8)

        Label:
            text: "📋  ESTUDIANTES"
            font_size: dp(25)
            bold: True
            color: 0.06, 0.25, 0.60, 1
            size_hint_y: None
            height: dp(50)

        ScrollView:
            bar_width: dp(6)

            GridLayout:
                id: list_box
                cols: 1
                spacing: dp(10)
                padding: dp(4)
                size_hint_y: None
                height: self.minimum_height

        Button:
            text: "🏆  MEJOR PROMEDIO"
            background_normal: ""
            background_color: 0.95, 0.67, 0.08, 1
            color: 1, 1, 1, 1
            font_size: dp(16)
            bold: True
            size_hint_y: None
            height: dp(50)
            on_release: root.show_best_student()

        Label:
            id: best_student
            text: ""
            font_size: dp(17)
            bold: True
            color: 0.70, 0.45, 0.02, 1
            size_hint_y: None
            height: dp(55)

        Button:
            text: "📊  ESTADÍSTICAS DEL GRUPO"
            background_normal: ""
            background_color: 0.43, 0.26, 0.73, 1
            color: 1, 1, 1, 1
            font_size: dp(16)
            bold: True
            size_hint_y: None
            height: dp(50)
            on_release: root.show_statistics()

        Label:
            id: statistics
            text: ""
            font_size: dp(15)
            color: 0.18, 0.22, 0.30, 1
            size_hint_y: None
            height: dp(130)

        Button:
            text: "←  VOLVER"
            background_normal: ""
            background_color: 0.35, 0.40, 0.50, 1
            color: 1, 1, 1, 1
            size_hint_y: None
            height: dp(45)
            on_release: root.manager.current = "menu"


<GradesScreen>:
    name: "grades"

    BoxLayout:
        orientation: "vertical"
        padding: dp(20)
        spacing: dp(11)

        Label:
            text: "📝"
            font_size: dp(38)
            size_hint_y: None
            height: dp(45)

        Label:
            text: "CALIFICACIONES"
            font_size: dp(24)
            bold: True
            color: 0.06, 0.25, 0.60, 1
            size_hint_y: None
            height: dp(45)

        TextInput:
            id: student
            hint_text: "👤  Nombre exacto del estudiante"
            multiline: False
            font_size: dp(17)
            padding: dp(12)

        TextInput:
            id: n1
            hint_text: "📝  Nota 1 (0-100)"
            input_filter: "float"
            multiline: False
            font_size: dp(17)
            padding: dp(12)

        TextInput:
            id: n2
            hint_text: "📝  Nota 2 (0-100)"
            input_filter: "float"
            multiline: False
            font_size: dp(17)
            padding: dp(12)

        TextInput:
            id: n3
            hint_text: "📝  Nota 3 (0-100)"
            input_filter: "float"
            multiline: False
            font_size: dp(17)
            padding: dp(12)

        Label:
            id: result
            text: ""
            font_size: dp(19)
            bold: True
            size_hint_y: None
            height: dp(65)

        ModernButton:
            text: "💾   GUARDAR Y CALCULAR"
            background_color: 0.08, 0.58, 0.38, 1
            on_release: root.save_grades()

        ModernButton:
            text: "←   VOLVER AL MENÚ"
            background_color: 0.35, 0.40, 0.50, 1
            on_release: root.manager.current = "menu"
"""


class MenuScreen(Screen):

    def on_pre_enter(self):
        total = len(list(store))
        suma = 0

        for key in store:
            suma += float(store.get(key).get("average", 0))

        promedio = suma / total if total else 0

        self.ids.total.text = str(total)
        self.ids.promedio.text = f"{promedio:.2f}"


class RegisterScreen(Screen):

    def save_student(self):

        name = self.ids.name.text.strip()
        grade = self.ids.grade.text.strip()
        subject = self.ids.subject.text.strip()

        if not name or not grade:
            self.ids.msg.text = "⚠️ Completa nombre y grado."
            return

        key = name.lower().replace(" ", "_")

        if store.exists(key):
            self.ids.msg.text = "⚠️ Ese estudiante ya existe."
            return

        store.put(
            key,
            name=name,
            grade=grade,
            subject=subject,
            notes=[0, 0, 0],
            average=0
        )

        self.ids.msg.text = "✅ Estudiante guardado correctamente."

        self.ids.name.text = ""
        self.ids.grade.text = ""
        self.ids.subject.text = ""


class StudentsScreen(Screen):

    def on_pre_enter(self):
        self.refresh()

    def refresh(self):

        from kivy.uix.label import Label
        from kivy.uix.button import Button
        from kivy.uix.boxlayout import BoxLayout

        box = self.ids.list_box
        box.clear_widgets()

        for key in store:

            data = store.get(key)

            avg = float(data.get("average", 0))
            notes = data.get("notes", [0, 0, 0])

            estado = "🟢 APROBADO" if avg >= 60 else "🔴 REPROBADO"

            row = BoxLayout(
                orientation="vertical",
                size_hint_y=None,
                height=125,
                padding=dp(8),
                spacing=dp(3)
            )

            # COLOR SEGÚN EL ESTADO
            if avg >= 60:
                bg = (0.86, 0.96, 0.89, 1)
            else:
                bg = (1, 0.89, 0.89, 1)

            with row.canvas.before:
                from kivy.graphics import Color, RoundedRectangle

                Color(rgba=bg)

                rect = RoundedRectangle(
                    pos=row.pos,
                    size=row.size,
                    radius=[15]
                )

                row.bind(
                    pos=lambda obj, value, r=rect:
                    setattr(r, "pos", value)
                )

                row.bind(
                    size=lambda obj, value, r=rect:
                    setattr(r, "size", value)
                )

            info = Label(
                text=
                f"👤  {data['name']}\n"
                f"🏫  {data['grade']}     📚 {data.get('subject', '')}\n"
                f"📝  {notes[0]:.0f}   {notes[1]:.0f}   {notes[2]:.0f}\n"
                f"⭐  Promedio: {avg:.2f}     {estado}",
                color=(0.12, 0.16, 0.24, 1),
                font_size=dp(15)
            )

            row.add_widget(info)

            btn = Button(
                text="🗑 Eliminar estudiante",
                background_normal="",
                background_color=(0.75, 0.18, 0.18, 1),
                color=(1, 1, 1, 1),
                size_hint_y=None,
                height=dp(32)
            )

            btn.bind(
                on_release=lambda b, k=key:
                self.delete_student(k)
            )

            row.add_widget(btn)

            box.add_widget(row)

    def delete_student(self, key):

        store.delete(key)
        self.refresh()

    def show_best_student(self):

        if not store:

            self.ids.best_student.text = (
                "No hay estudiantes registrados."
            )

            return

        best_name = None
        best_average = -1

        for key in store:

            data = store.get(key)

            average = float(
                data.get("average", 0)
            )

            if average > best_average:

                best_average = average
                best_name = data["name"]

        self.ids.best_student.text = (
            f"🏆  {best_name}  •  {best_average:.2f}"
        )

    def show_statistics(self):

        if not store:

            self.ids.statistics.text = (
                "No hay estudiantes registrados."
            )

            return

        total = 0
        approved = 0
        failed = 0
        sum_averages = 0

        highest = -1
        lowest = 101

        for key in store:

            data = store.get(key)

            average = float(
                data.get("average", 0)
            )

            total += 1
            sum_averages += average

            if average >= 60:
                approved += 1
            else:
                failed += 1

            if average > highest:
                highest = average

            if average < lowest:
                lowest = average

        general_average = (
            sum_averages / total
        )

        self.ids.statistics.text = (
            "📊  ESTADÍSTICAS DEL GRUPO\n\n"
            f"👥 Estudiantes: {total}\n"
            f"📈 Promedio general: {general_average:.2f}\n"
            f"🟢 Aprobados: {approved}\n"
            f"🔴 Reprobados: {failed}\n"
            f"🏆 Más alto: {highest:.2f}    "
            f"📉 Más bajo: {lowest:.2f}"
        )


class GradesScreen(Screen):

    def save_grades(self):

        name = self.ids.student.text.strip()

        key = name.lower().replace(" ", "_")

        if not store.exists(key):

            self.ids.result.text = (
                "❌ No se encontró ese estudiante."
            )

            return

        try:

            notes = [
                float(self.ids.n1.text),
                float(self.ids.n2.text),
                float(self.ids.n3.text)
            ]

            if any(
                n < 0 or n > 100
                for n in notes
            ):

                raise ValueError

        except ValueError:

            self.ids.result.text = (
                "⚠️ Las notas deben estar "
                "entre 0 y 100."
            )

            return

        average = sum(notes) / 3

        data = store.get(key)

        store.put(
            key,
            name=data["name"],
            grade=data["grade"],
            subject=data.get("subject", ""),
            notes=notes,
            average=average
        )

        if average >= 60:

            self.ids.result.text = (
                f"⭐ Promedio: {average:.2f}\n"
                f"🟢 APROBADO"
            )

            self.ids.result.color = (
                0.05, 0.55, 0.25, 1
            )

        else:

            self.ids.result.text = (
                f"⭐ Promedio: {average:.2f}\n"
                f"🔴 REPROBADO"
            )

            self.ids.result.color = (
                0.75, 0.12, 0.12, 1
            )


class EstudiantesApp(App):

    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    EstudiantesApp().run()