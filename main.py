from random import shuffle  #se usará el shuffle para aleatorizar las preguntas
import time  #se usará para tiempo entre preguntas
import os   

clearConsole = lambda: os.system('cls'
                                 if os.name in ('nt', 'dos') else 'clear')
clearConsole()#comando para limpiar consola

def cuenta_regresiva():#cuenta regresiva desde el 5
  for i in range(1,6):
    print('\n',6-i)
    time.sleep(1)
    clearConsole()
    
    
#Listas dónde se encontrarán las preguntas, posibles respuestas, respuesta correcta y una acotación sobre la pregunta
#Se usará el siguiente formato: [Pregunta, Alternativa_1,Alternativa_2,Alternativa_3, Alternativa_correcta(número), acotación]
    
a = [ '¿Para qué usan las computadoras las variables?',
    'Para recordar información', 'Para dibujar imagenes en pantalla',
    'Para imprimir video en pantalla', '1',
    'Cada variable debe tener un nombre unico, llamado identificador']
b = ['¿Para qué usamos las snake case?',
    'Para crear nombres de variables con espacios',
    'Para crear nombres de variables con varias palabras', 'No las usamos',
    '2',
    'Una snake case es la convención que compone las palabras separadas por barra baja']
c = ['¿Cómo sabemos que un valor es una string?',
    'es una palabra entre comillas dobles', 'Contiene el signo"="',
    'Son números', '1',
    'Las string, son un tipo de datos compuestos por secuencias de carácteres que representan texto']
d = ['¿Cuál de estas lineas de código actualiza la variable "Status"?',
    'status == "Working out"', 'status += "Working out"',
    'status = "Working out"', '3',
    'Para modificar el valor de una variable en Python, basta con asignarle un nuevo valor en cualquier momento y lugar después de la definición']
e = ['¿Cuál es un buen uso para los valores "True" y "False"?',
    'Almacenamiento de valores de uno al cinco',
    'Mostrar si una función está activada o desactivada',
    'Repetir valores eternamente', '2',
    'En Python cualquier variable (en general, cualquier objeto) puede considerarse como una variable booleana. En general los elementos nulos o vacíos se consideran False y el resto se consideran True.']
f = ['Elige el que sea mejor para mostrar a un usuario que se dio de baja de un servicio.',
    'subscribed = False', 'subscribed = True', 'subscribed = 10', '1',
    'Una variable booleana es una variable que sólo puede tomar dos posibles valores: True (verdadero) o False (falso)']
    
#coloresbpara personalizar trivia
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
RESET = '\033[39m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'

iniciar_trivia = True  #boleano para empezar y terminar trivia
iniciar_respuestas = True  #boleano para cerrar el loop de respuestas

puntaje = 0
intentos = 0
puntajes = []

print(GREEN,'')
nombre=input('Para empezar, brindame tu nombre :D\n-')
clearConsole()
print(
    CYAN,
    '\nHola ',nombre,' y bienvenido a mi trivia!!!! \n\nEn esta trivia encontrarás preguntas básicas sobre la programación en phyton :D \n\nA continuación te explicaré las reglas:'
)
time.sleep(5)
clearConsole()
print(
    MAGENTA,
    'Aparecerá en pantalla una serie de preguntas, cada pregunta consta de 3 alternativas.')
time.sleep(3)
print('\n1. Usando números de 1 al 3 deberás escoger entre ellas la respuesta correcta.')
time.sleep(3)
print('\n2. Cuando aciertes una respuesta, se te sumarán 10 puntos!! :D, pero si fallas, se restarán 3 puntos del total acumulado D:',GREEN)
time.sleep(2)
input('\nPresiona cualquier tecla para continuar: ')
clearConsole()
print(MAGENTA,'Ahora que sabes las reglas, comencemos!!!')
time.sleep(2)
clearConsole()

while iniciar_trivia == True:
    intentos += 1
    puntaje = 0
    iniciar_respuestas = True
    preguntas = [a, b, c, d, e, f]  #Lista para preguntas random
    print(MAGENTA, '\nIntento n° ', intentos, GREEN)
    print(YELLOW, '\nPuntaje inicial: ', puntaje, GREEN)
    input('\nPresiona enter para continuar')
    clearConsole()
    cuenta_regresiva()
    while (len(preguntas) > 0):  #Al eliminarse todos los elementos de esta lista, se terminará el ciclo
        shuffle(preguntas)  #Aleatorizamos las preguntas
        print(BLUE, '\n', preguntas[0][0])
        print(GREEN, '\nSelecciona una de las siguientes alternativas: ')
        print(BLUE, '\n', '1.', preguntas[0][1])
        print(BLUE, '2.', preguntas[0][2])
        print(BLUE, '3.', preguntas[0][3], GREEN)
        respuesta = input('\nrespuesta: ')
        #Utilizo el while para recopilar las respuestas del usuario
        time.sleep(1)
        while iniciar_respuestas == True:
            if respuesta == preguntas[0][4]:
                print(GREEN, '\n Correcto')
                print(RESET, '\n', preguntas[0][5])
                puntaje += 10
                print(YELLOW, '\nGanaste 10 puntos')
                time.sleep(5)
                iniciar_respuestas = False
                clearConsole()
            elif respuesta in ('1', '2', '3'):
                print(RED, '\nIncorrecto')
                puntaje -= 3
                print(YELLOW, '\nPrediste 3 puntos')
                time.sleep(1)
                clearConsole()
                iniciar_respuestas = False
            else:
                respuesta = input('\nSeleccione una opción válida: ')
        iniciar_respuestas = True
        preguntas.pop(0)  #Esta linea elmina el primer elemento de la lista para evitar repeticiones
    print(YELLOW, '\nTu puntaje total fue: ', puntaje, ' puntos')
    print(CYAN, '\n¿Deseas intentar la trivia nuevamente?', GREEN)
    repetir_trivia = input('\ningresa "si" para repetir, o cualquier tecla para finalizar: ').lower()
    puntajes.append(puntaje)
    clearConsole()
    if repetir_trivia != 'si':
        print(CYAN, '\nTu mayor puntaje fué de: ', max(puntajes))
        print(CYAN,'\nEspero que lo hayas pasado bien y hayan aprendido algo sobre Phyton :D \n\nHasta pronto!!!')
        iniciar_trivia = False
        puntajes=[]