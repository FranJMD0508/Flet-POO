import flet as ft

class ConversorNumeros:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.center()
        self.page.title = "Convertidor de Numeros"
        self.page.window_width = 764
        self.page.window_height = 380
        self.page.window_resizable = False
        self.page.window_maximizable = False
        self.page.bgcolor = "#0E183A"
        self.page.fonts = {
            "Inter": "Inter-Regular.ttf"
        }
        self.Interfaz()
        
    def Interfaz(self):
        ConTxt = ft.Container(
            content = ft.Text(
                value="CONVERSOR DE NÚMEROS",
                size = 25,
                font_family = "Inter",
                weight = ft.FontWeight.BOLD,),
            alignment = ft.alignment.center
        )
        self.dd1 = ft.Dropdown(
            options=[
                ft.dropdown.Option("Binario"),
                ft.dropdown.Option("Hexadecimal"),
                ft.dropdown.Option("Decimal"),
                ft.dropdown.Option("Terciario"),
                ft.dropdown.Option("Cuaternario"),
                ft.dropdown.Option("Octal")
            ],
            value = "Binario",
            color = "#8B8B8B",
            fill_color= "#d9d9d9",
            text_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD
            )
        )
        self.dd2 = ft.Dropdown(
            options=[
                ft.dropdown.Option("Binario"),
                ft.dropdown.Option("Hexadecimal"),
                ft.dropdown.Option("Decimal"),
                ft.dropdown.Option("Terciario"),
                ft.dropdown.Option("Cuaternario"),
                ft.dropdown.Option("Octal")
            ],
            value = "Hexadecimal",
            color = "#8b8686",
            fill_color= "#d9d9d9",
            text_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD
            )
        )
        self.tf1 = ft.TextField(
            hint_text="Escriba aqui...",
            hint_style=ft.TextStyle(
                color = "#aeaeae",
            ),
            color = "#6c6b6b",
            multiline=True,
            min_lines=8,
            max_lines=8,
            width=300,
            fill_color= "#d9d9d9"
        )
        self.tf2 = ft.TextField(
            hint_text="Aqui aparecerá el numero convertido",
            hint_style=ft.TextStyle(
                color = "#aeaeae",
            ),
            color = "#6c6b6b",
            multiline=True,
            min_lines=8,
            max_lines=8,
            width=300,
            read_only = True,
            fill_color= "#d9d9d9"
        )
        b1 = ft.IconButton(
            icon=ft.icons.ARROW_BACK,
            width = 108
        )
        b2 = ft.ElevatedButton(
            text="Convertir",
            bgcolor = "#52A644",
            color = "#FFFFFF"
        )
        b3 = ft.ElevatedButton(
            text="Reiniciar",
            width = 107,
            bgcolor = "#FF4B4B",
            color = "#FFFFFF"
        )
        self.page.add(ft.Column([
            ConTxt,ft.Column([
                ft.Row([
                    self.dd1,b1,self.dd2]),ft.Row([
                        self.tf1,ft.Column([
                            b2,b3]),self.tf2])])]))
        
def main(page: ft.Page):
    ConversorNumeros(page)
ft.app(main)