#Implementa una clase 'calculadora' con metodos para sumar, restar, multiplicar y 
#dividir dos numeros


class calculadora:
    def sumar(self,num1,num2):
        return num1+num2
    
    def restar (self,num1,num2):
        return num1-num2
    
    def multiplicar(self,num1,num2):
        return num1*num2
    
    def dividir(self,num1,num2):
        if num2 != 0:
            return num1/num2
        else:
            return 'No es diivisible'
    
print('El resultado de la suma es:', calculadora.sumar(20, 80))
print('El resultado de la resta es:', calculadora.restar(20,80))
print('El resultado de la multiplicacion es:', calculadora.multiplicar(20,80))
print('El resultado de la division es:', calculadora.dividir(20,80))

        