import flet as ft

class ConversorNumeros:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Convertidor de Numeros"
        self.page.window_width = 764
        self.page.window_height = 422
        self.page.window_resizable = False
        self.page.window_maximizable = False
        self.page.window.center()
        self.Interfaz()
        
    def Interfaz(self):
        ConTxt = ft.Container(
            content = ft.Text(
                value="Conversor de Números",
                size = 20),
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
            value = "Binario"
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
            value = "Hexadecimal"
        )
        self.tf1 = ft.TextField(
            hint_text="Escriba aqui...",
            multiline=True,
            min_lines=10,
            max_lines=10,
            width=300
        )
        self.tf2 = ft.TextField(
            hint_text="Aqui aparecerá el numero convertido",
            multiline=True,
            min_lines=10,
            max_lines=10,
            width=300,
            read_only = True
        )
        b1 = ft.IconButton(
            icon=ft.icons.ARROW_BACK,
            width = 108
        )
        b2 = ft.ElevatedButton(
            text="Convertir",
        )
        b3 = ft.ElevatedButton(
            text="Reiniciar",
            width = 107
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