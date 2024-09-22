class Conversor:
    def __init__(self):
        pass
    
    def convertir_decimal(self,num,tipo1):
        if tipo1 == "Binario":
            decimal = int(num,2)
        elif tipo1 == "Hexadecimal":
            decimal = int(num, 16)
        elif tipo1 == "Terciario":
            decimal = int(num, 3)
        elif tipo1 == "Cuaternario":
            decimal = int(num,4)
        elif tipo1 == "Octal":
            decimal = int(num,8)
        else:
            decimal = num
        return(decimal)
        
    def convertir_final(self,decimal,tipo2):
        if tipo2 == "Binario":
            return bin(int(decimal))[2:]
        
    def filtro(self,tipo,txt):
        if tipo == "Binario":
            filtrado = ''.join(filter(lambda char: char in '01', txt))
            return filtrado
        if tipo == "Hexadecimal":
            filtrado = ''.join(filter(lambda char: char in '0123456789ABCDEFabcdef',txt))
            return filtrado
        if tipo == "Decimal":
            filtrado = ''.join(filter(str.isdigit,txt))
            return filtrado
        if tipo == "Ternario":
            filtrado = ''.join(filter(lambda char: char in '012', txt))
            return filtrado
        if tipo == "Cuaternario":
            filtrado = ''.join(filter(lambda char: char in '0123', txt))
            return filtrado
        if tipo == "Octal":
            filtrado = ''.join(filter(lambda char: char in '01234567', txt))
            return filtrado