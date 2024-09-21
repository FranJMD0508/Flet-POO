import flet as ft

class ConversorNumeros:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Convertidor de Numeros"
        self.page.window_width = 780
        self.page.window_height = 438
        self.Interfaz
        
    def Interfaz(self):
        Titulo = ft.Text(
            value="Conversor de Números",
            size=20
        )
        self.dd1 = ft.Dropdown(
            options=[
                ft.dropdown.Option("Binario"),
                ft.dropdown.Option("Hexadecimal"),
                ft.dropdown.Option("Decimal"),
                ft.dropdown.Option("Terciario"),
                ft.dropdown.Option("Cuaternario"),
                ft.dropdown.Option("Octal")
            ]
        )
        self.dd2 = ft.Dropdown(
            options=[
                ft.dropdown.Option("Binario"),
                ft.dropdown.Option("Hexadecimal"),
                ft.dropdown.Option("Decimal"),
                ft.dropdown.Option("Terciario"),
                ft.dropdown.Option("Cuaternario"),
                ft.dropdown.Option("Octal")
            ]
        )
        self.tf1 = ft.TextField(
            hint_text="Escriba aqui...",
            multiline=True,
            min_lines=10,
            width=300
        )
        self.tf2 = ft.TextField(
            hint_text="Aqui aparecera el numero convertido",
            multiline=True,
            min_lines=10,
            width=300
        )
        b1 = ft.IconButton(

        )
        b2 = ft.ElevatedButton(
            text="Convertir",
        )
        b3 = ft.ElevatedButton(
            text="Reiniciar",
        )
        
def main(page: ft.Page):
    ConversorNumeros(page)
ft.app(main)