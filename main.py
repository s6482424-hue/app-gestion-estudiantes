from kivy.app import App
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label

store = JsonStore("estudiantes.json")

MATERIAS = [
    "Matemáticas",
    "Español",
    "Historia",
    "Inglés",
    "Ciencias"
]

GRUPOS = ["10.º A", "11.º A"]


KV = """
ScreenManager:
    MenuScreen:
    RegisterScreen:
    StudentsScreen:
    GradesScreen:
    SearchScreen:
    BestScreen:
    StatsScreen:


<MenuScreen>:
    name: "menu"

    BoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 10

        Label:
            text: "GESTIÓN DE ESTUDIANTES"
            font_size: 25

        Button:
            text: "Registrar estudiante"
            on_release: root.manager.current = "register"

        Button:
            text: "Calificaciones"
            on_release: root.manager.current = "grades"

        Button:
            text: "Ver estudiantes"
            on_release:
                root.manager.get_screen("students").actualizar()
                root.manager.current = "students"

        Button:
            text: "Buscar estudiante"
            on_release: root.manager.current = "search"

        Button:
            text: "Mejor promedio"
            on_release: root.manager.current = "best"

        Button:
            text: "Estadísticas"
            on_release: root.manager.current = "stats"


<RegisterScreen>:
    name: "register"

    ScrollView:
        BoxLayout:
            orientation: "vertical"
            padding: 20
            spacing: 10
            size_hint_y: None
            height: self.minimum_height

            Label:
                text: "REGISTRAR ESTUDIANTE"
                font_size: 24
                size_hint_y: None
                height: 50

            TextInput:
                id: nombre
                hint_text: "Nombre del estudiante"
                multiline: False
                size_hint_y: None
                height: 50

            Label:
                text: "Seleccione el grupo"
                size_hint_y: None
                height: 40

            Spinner:
                id: grupo
                text: "10.º A"
                values: ["10.º A", "11.º A"]
                size_hint_y: None
                height: 50

            Button:
                text: "Registrar"
                size_hint_y: None
                height: 55
                on_release: root.registrar()

            Button:
                text: "Volver"
                size_hint_y: None
                height: 50
                on_release: root.manager.current = "menu"


<GradesScreen>:
    name: "grades"

    ScrollView:
        BoxLayout:
            orientation: "vertical"
            padding: 20
            spacing: 10
            size_hint_y: None
            height: self.minimum_height

            Label:
                text: "CALIFICACIONES"
                font_size: 24
                size_hint_y: None
                height: 50

            Spinner:
                id: estudiante
                text: "Seleccione estudiante"
                values: []
                size_hint_y: None
                height: 50
                on_text: root.mostrar_campos()

            Label:
                id: info
                text: "Seleccione un estudiante"
                size_hint_y: None
                height: 40

            TextInput:
                id: nota1
                hint_text: "Matemáticas"
                input_filter: "float"
                multiline: False
                size_hint_y: None
                height: 50

            TextInput:
                id: nota2
                hint_text: "Español"
                input_filter: "float"
                multiline: False
                size_hint_y: None
                height: 50

            TextInput:
                id: nota3
                hint_text: "Historia"
                input_filter: "float"
                multiline: False
                size_hint_y: None
                height: 50

            TextInput:
                id: nota4
                hint_text: "Inglés"
                input_filter: "float"
                multiline: False
                size_hint_y: None
                height: 50

            TextInput:
                id: nota5
                hint_text: "Ciencias"
                input_filter: "float"
                multiline: False
                size_hint_y: None
                height: 50

            Button:
                text: "Guardar calificaciones"
                size_hint_y: None
                height: 55
                on_release: root.guardar_notas()

            Button:
                text: "Volver"
                size_hint_y: None
                height: 50
                on_release: root.manager.current = "menu"


<StudentsScreen>:
    name: "students"

    BoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 10

        Label:
            text: "ESTUDIANTES"
            font_size: 24
            size_hint_y: None
            height: 50

        Spinner:
            id: grupo
            text: "10.º A"
            values: ["10.º A", "11.º A"]
            size_hint_y: None
            height: 50
            on_text: root.actualizar()

        ScrollView:
            Label:
                id: lista
                text: ""
                text_size: self.width, None
                size_hint_y: None
                height: self.texture_size[1]

        Button:
            text: "Volver"
            size_hint_y: None
            height: 50
            on_release: root.manager.current = "menu"


<SearchScreen>:
    name: "search"

    BoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 10

        Label:
            text: "BUSCAR ESTUDIANTE"
            font_size: 24
            size_hint_y: None
            height: 50

        TextInput:
            id: buscar
            hint_text: "Escriba el nombre"
            multiline: False
            size_hint_y: None
            height: 50

        Spinner:
            id: grupo
            text: "Todos los grupos"
            values: ["Todos los grupos", "10.º A", "11.º A"]
            size_hint_y: None
            height: 50

        Button:
            text: "Buscar"
            size_hint_y: None
            height: 55
            on_release: root.buscar_estudiante()

        ScrollView:
            Label:
                id: resultado
                text: ""
                text_size: self.width, None
                size_hint_y: None
                height: self.texture_size[1]

        Button:
            text: "Volver"
            size_hint_y: None
            height: 50
            on_release: root.manager.current = "menu"


<BestScreen>:
    name: "best"

    BoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 10

        Label:
            text: "MEJOR PROMEDIO"
            font_size: 24
            size_hint_y: None
            height: 50

        Spinner:
            id: grupo
            text: "10.º A"
            values: ["10.º A", "11.º A"]
            size_hint_y: None
            height: 50

        Button:
            text: "Mostrar"
            size_hint_y: None
            height: 55
            on_release: root.mostrar_mejor()

        Label:
            id: resultado
            text: ""
            text_size: self.width, None

        Button:
            text: "Volver"
            size_hint_y: None
            height: 50
            on_release: root.manager.current = "menu"


<StatsScreen>:
    name: "stats"

    BoxLayout:
        orientation: "vertical"
        padding: 20
        spacing: 10

        Label:
            text: "ESTADÍSTICAS DEL GRUPO"
            font_size: 24
            size_hint_y: None
            height: 50

        Spinner:
            id: grupo
            text: "10.º A"
            values: ["10.º A", "11.º A"]
            size_hint_y: None
            height: 50

        Button:
            text: "Mostrar estadísticas"
            size_hint_y: None
            height: 55
            on_release: root.mostrar_estadisticas()

        ScrollView:
            Label:
                id: resultado
                text: ""
                text_size: self.width, None
                size_hint_y: None
                height: self.texture_size[1]

        Button:
            text: "Volver"
            size_hint_y: None
            height: 50
            on_release: root.manager.current = "menu"
"""


def obtener_estudiantes():
    if not store.exists("datos"):
        return {}
    return store.get("datos")["estudiantes"]


def guardar_estudiantes(estudiantes):
    store.put("datos", estudiantes=estudiantes)


def promedio(estudiante):
    notas = estudiante.get("notas", [])

    if len(notas) != 5:
        return None

    return sum(notas) / 5


def estado(estudiante):
    p = promedio(estudiante)

    if p is None:
        return "Sin calificaciones"

    return "Aprobado" if p >= 60 else "Reprobado"


def mostrar_error(mensaje):
    Popup(
        title="Aviso",
        content=Label(text=mensaje),
        size_hint=(0.85, 0.35)
    ).open()


class MenuScreen(Screen):
    pass


class RegisterScreen(Screen):

    def registrar(self):
        nombre = self.ids.nombre.text.strip()
        grupo = self.ids.grupo.text

        if not nombre:
            mostrar_error("Escriba el nombre del estudiante.")
            return

        estudiantes = obtener_estudiantes()

        clave = nombre.lower()

        if clave in estudiantes:
            mostrar_error("Ese estudiante ya está registrado.")
            return

        estudiantes[clave] = {
            "nombre": nombre,
            "grupo": grupo,
            "notas": []
        }

        guardar_estudiantes(estudiantes)

        self.ids.nombre.text = ""

        mostrar_error(
            f"Estudiante registrado correctamente en {grupo}."
        )


class GradesScreen(Screen):

    def on_pre_enter(self):
        self.actualizar_lista()

    def actualizar_lista(self):
        estudiantes = obtener_estudiantes()

        nombres = [
            datos["nombre"]
            for datos in estudiantes.values()
        ]

        self.ids.estudiante.values = nombres

        if nombres:
            self.ids.estudiante.text = nombres[0]
        else:
            self.ids.estudiante.text = "No hay estudiantes"

    def mostrar_campos(self):
        nombre = self.ids.estudiante.text

        estudiantes = obtener_estudiantes()

        estudiante = None

        for datos in estudiantes.values():
            if datos["nombre"] == nombre:
                estudiante = datos
                break

        if not estudiante:
            return

        notas = estudiante.get("notas", [])

        self.ids.info.text = (
            f"{estudiante['nombre']} - {estudiante['grupo']}"
        )

        campos = [
            self.ids.nota1,
            self.ids.nota2,
            self.ids.nota3,
            self.ids.nota4,
            self.ids.nota5
        ]

        for campo in campos:
            campo.text = ""

        if len(notas) == 5:
            for campo, nota in zip(campos, notas):
                campo.text = str(nota)

    def guardar_notas(self):
        nombre = self.ids.estudiante.text

        estudiantes = obtener_estudiantes()

        estudiante = None
        clave = None

        for k, datos in estudiantes.items():
            if datos["nombre"] == nombre:
                estudiante = datos
                clave = k
                break

        if not estudiante:
            mostrar_error("Seleccione un estudiante.")
            return

        campos = [
            self.ids.nota1,
            self.ids.nota2,
            self.ids.nota3,
            self.ids.nota4,
            self.ids.nota5
        ]

        try:
            notas = [float(campo.text) for campo in campos]
        except ValueError:
            mostrar_error("Debe introducir las 5 calificaciones.")
            return

        for nota in notas:
            if nota < 0 or nota > 100:
                mostrar_error(
                    "Las calificaciones deben estar entre 0 y 100."
                )
                return

        estudiantes[clave]["notas"] = notas

        guardar_estudiantes(estudiantes)

        p = promedio(estudiantes[clave])

        mostrar_error(
            f"Calificaciones guardadas.\n\n"
            f"Promedio: {p:.2f}\n"
            f"Estado: {estado(estudiantes[clave])}"
        )


class StudentsScreen(Screen):

    def actualizar(self):
        estudiantes = obtener_estudiantes()
        grupo = self.ids.grupo.text

        texto = ""

        for datos in estudiantes.values():

            if datos["grupo"] != grupo:
                continue

            p = promedio(datos)

            texto += f"{datos['nombre']}\n"
            texto += f"Grupo: {grupo}\n"

            if p is None:
                texto += "Promedio: Sin calificaciones\n"
            else:
                texto += f"Promedio: {p:.2f}\n"
                texto += f"Estado: {estado(datos)}\n"

            texto += "\n"

        if not texto:
            texto = "No hay estudiantes registrados en este grupo."

        self.ids.lista.text = texto


class SearchScreen(Screen):

    def buscar_estudiante(self):
        texto_busqueda = self.ids.buscar.text.lower().strip()
        grupo = self.ids.grupo.text

        estudiantes = obtener_estudiantes()

        resultado = ""

        for datos in estudiantes.values():

            if texto_busqueda not in datos["nombre"].lower():
                continue

            if grupo != "Todos los grupos":
                if datos["grupo"] != grupo:
                    continue

            resultado += f"Nombre: {datos['nombre']}\n"
            resultado += f"Grupo: {datos['grupo']}\n"

            if datos.get("notas"):
                resultado += "Calificaciones:\n"

                for materia, nota in zip(
                    MATERIAS,
                    datos["notas"]
                ):
                    resultado += f"{materia}: {nota}\n"

                resultado += f"Promedio: {promedio(datos):.2f}\n"
                resultado += f"Estado: {estado(datos)}\n"
            else:
                resultado += "Sin calificaciones.\n"

            resultado += "\n"

        if not resultado:
            resultado = "No se encontró ningún estudiante."

        self.ids.resultado.text = resultado


class BestScreen(Screen):

    def mostrar_mejor(self):
        estudiantes = obtener_estudiantes()
        grupo = self.ids.grupo.text

        candidatos = []

        for datos in estudiantes.values():

            if datos["grupo"] != grupo:
                continue

            p = promedio(datos)

            if p is not None:
                candidatos.append((p, datos))

        if not candidatos:
            self.ids.resultado.text = (
                "No hay estudiantes con 5 calificaciones "
                "en este grupo."
            )
            return

        mejor = max(candidatos, key=lambda x: x[0])

        p, estudiante = mejor

        self.ids.resultado.text = (
            f"Estudiante: {estudiante['nombre']}\n"
            f"Grupo: {grupo}\n"
            f"Promedio: {p:.2f}"
        )


class StatsScreen(Screen):

    def mostrar_estadisticas(self):
        estudiantes = obtener_estudiantes()
        grupo = self.ids.grupo.text

        grupo_estudiantes = [
            datos
            for datos in estudiantes.values()
            if datos["grupo"] == grupo
        ]

        total = len(grupo_estudiantes)

        con_notas = [
            datos
            for datos in grupo_estudiantes
            if promedio(datos) is not None
        ]

        aprobados = sum(
            1 for datos in con_notas
            if estado(datos) == "Aprobado"
        )

        reprobados = sum(
            1 for datos in con_notas
            if estado(datos) == "Reprobado"
        )

        if con_notas:
            promedio_grupo = sum(
                promedio(datos)
                for datos in con_notas
            ) / len(con_notas)
        else:
            promedio_grupo = 0

        self.ids.resultado.text = (
            f"Grupo: {grupo}\n\n"
            f"Total de estudiantes: {total}\n"
            f"Con calificaciones completas: {len(con_notas)}\n"
            f"Aprobados: {aprobados}\n"
            f"Reprobados: {reprobados}\n"
            f"Promedio del grupo: {promedio_grupo:.2f}"
        )


class GestionEstudiantesApp(App):

    def build(self):
        return Builder.load_string(KV)


if __name__ == "__main__":
    GestionEstudiantesApp().run()