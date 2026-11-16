llista = []
#Sense bucle
llista.append(input('Introdueix un nom: '))
llista.append(input('Introdueix un nom: '))
llista.append(input('Introdueix un nom: '))

#Amb bucle
for i in range(3):
    llista.append(input('Introdueix un nom: '))

print('')
print(llista)
print('')

#Bucle en un interval concret
for i in range(17, 101):
    if(i % 2 == 0):
        print(i, end=' ')
print("\n")

#Bucle en una llista
compt = 0
for i in llista[0]:
    if(i=='a'):
        compt += 1
print('El primer nom de la llista és', llista[0], 'i té', compt, 'lletres a')
print('')

#Bucle de bucle amb elements
notes=[[6,6,7,10,9],[10,7,6,7,7],[5,5,10,7,10]]
compt=0
for i in notes:
    for j in i:
        if(j==10):
            compt+=1
print('Hi ha', compt,'deus (10) a la classe.')

#Bucle de bucle amb índex
if(compt > 0):
    print ('estan asseguts:')
    for i in range (3):
        for j in range (5):
            if(notes[i][j]==10):
                print('En la fila',i,'columna',j)
print('') 

#Bucle amb while
secret = 22
while True:
    num = int(input('Introdueix un número del 0 al 30: '))
    if num == secret:
        print('Has encertat!')
        break
    else:
        print('Prova de nou!')