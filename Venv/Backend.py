class Conversor:
    def __init__(self):
        pass
    
    def convertir_decimal(self,num,tipo1):
        if tipo1 == "Binario":
            decimal = int(num,2)
        elif tipo1 == "Hexadecimal":
            decimal = int(num, 16)
        elif tipo1 == "Ternario":
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
        elif tipo2 == "Hexadecimal":
            return hex(int(decimal))[2:]
        elif tipo2 == "Ternario":
            if decimal == 0:
                return "0"
            ternario = ""
            while decimal > 0:
                ternario = str(decimal % 3) + ternario
                decimal //= 3
            return ternario
        elif tipo2 == "Cuaternario":
            if decimal == 0:
                return "0"
            cuaternario = ""
            while decimal > 0:
                cuaternario = str(decimal%4) + cuaternario
                decimal //=4
            return cuaternario
        elif tipo2 == "Octal":
            return oct(decimal)[2:]
        else:
            return decimal
        
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