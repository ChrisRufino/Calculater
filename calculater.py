indice +=1 
numero1 = int(input('informe um numero para calcular: '))
numero2 = int(input('informe outro numero para calcular: '))
sinai_s = input('Escolha o sinal para realizar o calculo: (* + - / **): ')
print('Cálculo realizado com sucesso, resultado = ')  

calcular = numero1 + numero2
dividir = numero1 / numero2
subtrair = numero1 - numero2
multiplicar = numero1 * numero2
elevar = numero1 ** numero2

if sinai_s == '*':
     print(multiplicar)
elif sinai_s == '-':
    print(subtrair)
elif sinai_s == '+':
     print(calcular)
elif sinai_s == '/':
     print(dividir)
elif sinai_s =='**':
     print(elevar)    

else:
     print('Algo deu errado, retorne no seu código.')
