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
        
def main(page: ft.Page):
    ConversorNumeros(page)
ft.app(main)