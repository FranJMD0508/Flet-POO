import flet as ft
import Backend as bc

class ConversorNumeros:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.window.center()
        self.page.title = "Convertidor de Numeros"
        self.page.window.width = 764
        self.page.window.height = 380
        self.page.window.resizable = False
        self.page.window.maximizable = False
        self.page.bgcolor = "#0E183A"
        self.page.fonts = {
            "Inter": "Inter-Regular.ttf"
        }
        self.Interfaz()
        
    def Interfaz(self):
        ConTit = ft.Container(
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
                ft.dropdown.Option("Ternario"),
                ft.dropdown.Option("Cuaternario"),
                ft.dropdown.Option("Octal")
            ],
            value = "Binario",
            color = "#8B8B8B",
            fill_color= "#d9d9d9",
            text_style=ft.TextStyle(
                weight=ft.FontWeight.BOLD
            ),
            on_change = self.Reiniciar
        )
        self.dd2 = ft.Dropdown(
            options=[
                ft.dropdown.Option("Binario"),
                ft.dropdown.Option("Hexadecimal"),
                ft.dropdown.Option("Decimal"),
                ft.dropdown.Option("Ternario"),
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
            fill_color= "#d9d9d9",
            on_change = self.Filtrar
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
        self.b1 = ft.IconButton(
            icon=ft.icons.ARROW_BACK,
            width = 108,
            on_click = self.Invertir
        )
        self.b2 = ft.ElevatedButton(
            text="Convertir",
            bgcolor = "#52A644",
            color = "#FFFFFF",
            on_click = self.Convertir
        )
        self.b3 = ft.ElevatedButton(
            text="Reiniciar",
            width = 107,
            bgcolor = "#FF4B4B",
            color = "#FFFFFF",
            on_click = self.Reiniciar
        )
        self.page.add(ft.Column([
            ConTit,ft.Column([
                ft.Row([
                    self.dd1,self.b1,self.dd2]),ft.Row([
                        self.tf1,ft.Column([
                            self.b2,self.b3]),self.tf2])])]))
    def Reiniciar(self,e):
        self.tf1.value = ""
        self.tf2.value = ""
        self.page.update()
    
    def Invertir(self,e):
        if self.dd1.value != self.dd2.value:
            self.Reiniciar(self.b1)
        op1 = self.dd1.value
        op2 = self.dd2.value
        
        self.dd1.value = op2
        self.dd2.value = op1
        self.page.update()
        
    def Filtrar(self,e):
        e.control.value = bc.Conversor.filtro(self,self.dd1.value,e.control.value)
        self.page.update()
        
    def Convertir(self,e):
        if self.tf1.value != "":
            decimal = bc.Conversor.convertir_decimal(self,self.tf1.value,self.dd1.value)
            self.tf2.value = bc.Conversor.convertir_final(self,decimal,self.dd2.value)
            self.page.update()
        
def main(page: ft.Page):
    ConversorNumeros(page)
ft.app(main)