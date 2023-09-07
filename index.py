import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpim
import os
from os import unlink

df = pd.read_csv('./info/imagenes/argentina.csv')
""" print(df) """
""" namePlayer = df['nombre'] + ' ' + df['apellido']
print (namePlayer) """
namePlayer=df.to_numpy().tolist()
""" print(namePlayer) """


for i in namePlayer:
    jugadores = i[2] + " " + i[1]
    try:
        img = mpim.imread('./info/imagenes/fotos/' + jugadores + '.jpg')
        """ plt.imshow(img)
        plt.axis('off')
        plt.title(jugadores)
        plt.show() """
        if len(img.shape) != 3:
            print(f"{jugadores} tiene una foto en blanco y negro.")
    except FileNotFoundError:
        namePlayer.remove(i)



def menu():
    select= input('Ingrese que desea ver:\nA.Ver un jugadores \nB.Ver todos los jugadores \nC.Borrar un jugador \nD.Salir\n').upper()
    if select == 'A':
        Ver()
        menu()
    elif select == 'B':
        Ver_Todos()
        input('\n(Presione Enter para ir al menu...)')
        menu()
    elif select == 'C':
        Borrar()
        input('\n(Presione Enter para ir al menu...)')
        menu()
    
    elif select == 'D':
        op = input('Estas seguro qe deseas salir: Y/N \n').upper()
        if op == 'Y':
            input('Gracias por su visita!!!\n(Presione Enter para seguir...)')
            exit()
        elif op == 'N':
            menu()
        else:
            input('La opcion seleccionada no es correcta \n(Presione Enter para seguir...)')
            menu()
    else:
        input('La opcion seleccionada no es correcta \n(Presione cualquier tecla para seguir...)')
        menu()

def Ver():
    selectNum=input(str('Ingrese el número de la camiseta del jugador:  '))
    player = None
    for i in namePlayer:
        if str(i[0]) == selectNum:
            player = i
            break
    
    if player:
        name = f"{player[2]} {player[1]}"
        img_path = f"./info/imagenes/fotos/{name}.jpg"
        """ img = mpim.imread('./info/imagenes/fotos/' + name + '.jpg') """
        
        if os.path.exists(img_path):
            img = mpim.imread(img_path)
            plt.imshow(img)
            plt.axis('off')
            plt.title(name)
            plt.show()
        else:
            print(f"No se encontró la foto de {name}.")
    else:
        print(f"No se encontró un jugador con el número de camiseta {selectNum}.")

def Ver_Todos():
    position = 1
    plt.subplots_adjust(hspace=0.5)
    for i in namePlayer:
        plt.subplot(4,3,position)
        img = mpim.imread('./info/imagenes/fotos/' + i[2]+" "+ i[1] + '.jpg')
        plt.imshow(img)
        plt.title(f"{i[2]} {i[1]}",fontsize=9)
        plt.axis('off')
        position = position + 1
        if i[1] == 'di maria':
            break
    plt.show()
    menu()
    
def Borrar():
    global df
    name= input("Ingrese el nombre del jugador a borrar: ")
    last_name = input("Ingrese el apellido: ")
    unlink('./info/imagenes/fotos/' + name +" "+ last_name + '.jpg')

    for i in namePlayer:
        if i[2]== name and i[1] == last_name:
            shirt = i[0]
            namePlayer.remove(i)
    df = df[df.num != shirt]
    df.to_csv('./info/imagenes/argentina.csv')
    print(namePlayer)
    menu()
menu()