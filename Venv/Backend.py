class Conversor:
    def __init__(self):
        pass
    
    def convertir_binario(self,num,tipo1,tipo2):
        pass
    def convertir_final(self,decimal,tipo2):
        pass
        
    def filtro(self,tipo,txt):
        if str(tipo) == "Binario":
            filtrado = ''.join(filter(lambda char: char in '01', txt))
            return filtrado
        if str(tipo) == "Hexadecimal":
            filtrado = ''.join(filter(lambda char: char in '0123456789ABCDEFabcdef',txt))
            return filtrado
        if str(tipo) == "Decimal":
            filtrado = ''.join(filter(str.isdigit,txt))
            return filtrado
        if str(tipo) == "Ternario":
            filtrado = ''.join(filter(lambda char: char in '012', txt))
            return filtrado
        if str(tipo) == "Cuaternario":
            filtrado = ''.join(filter(lambda char: char in '0123', txt))
            return filtrado
        if str(tipo) == "Octal":
            filtrado = ''.join(filter(lambda char: char in '01234567', txt))
            return filtrado