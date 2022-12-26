""" 
#Ponto da carne

#Primeira forma de escrever

tem_cel = int(input("Qual é a temperatura da carne? "))
x = tem_cel

if x < 48:
    print("Cozinhar por mais alguns minutos")
elif 48 <= x < 53:
    print("Selada")
elif 54 <= x <59:
    print("Ao ponto para mal")
elif 60 <= x <64:
    print("Ao ponto")
elif 65 <= x <71:
    print("Ao ponto para bem")
else :
    print("Queimou")

#Segunda forma de escrever

tem_cel = int(input("Qual é a temperatura da carne? "))
x = tem_cel

if x < 48:
    print("Cozinhar por mais alguns minutos")
elif x in range(48,53):
    print("Selada")
elif x in range(54,59):
    print("Ao ponto para mal")
elif x in range(60,64):
    print("Ao ponto")
elif x in range(65,70):
    print("Ao ponto para bem")
else :
    print("Queimou")
"""

'''
#Programa de Tinta

rendimento = int(input("Qual é o rendimento da lata? "))
altura = int(input("Qual é a altura da parede? "))
largura = int(input("Qual é a largura da parede? "))

def calculo_tinta():
    area =   altura * largura
    total = area / rendimento
    print(f'Você precisa de {total} latas de tinta')

calculo_tinta()
'''

'''
#Desafio com 'Sets'

funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana','Marcos','Alice','Melissa']
turno_noite = ['Pedro','Sophia','Bruno',]
tem_carro = ['Marcos', 'Alice','Bruno', 'Melissa']

#Lista1
lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)
